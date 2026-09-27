[CmdletBinding()]
param(
    [string]$InputDir = (Join-Path $PSScriptRoot "..\diagrams\activity"),
    [string]$OutputDir = (Join-Path $PSScriptRoot "..\output\activity-diagrams"),
    [string]$PlantUmlJar
)

$ErrorActionPreference = "Stop"

function Get-PlantUmlJar {
    if ($PlantUmlJar) {
        return (Resolve-Path -LiteralPath $PlantUmlJar).Path
    }

    $extensionRoot = Join-Path $env:USERPROFILE ".vscode\extensions"
    $candidate = Get-ChildItem -Path $extensionRoot -Filter "plantuml.jar" -Recurse -File |
        Where-Object { $_.FullName -like "*jebbs.plantuml-*" } |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1

    if (-not $candidate) {
        throw "Cannot find plantuml.jar. Pass its path with -PlantUmlJar."
    }
    return $candidate.FullName
}

function Get-SwimlaneBounds {
    param([Parameter(Mandatory)][string]$SvgText)

    $pattern = '<line style="stroke:#000000;stroke-width:(?<width>[0-9.]+);" x1="(?<x1>[0-9.]+)" x2="(?<x2>[0-9.]+)" y1="(?<y1>[0-9.]+)" y2="(?<y2>[0-9.]+)"/>'
    $verticalLines = foreach ($match in [regex]::Matches($SvgText, $pattern)) {
        $x1 = [double]::Parse($match.Groups["x1"].Value, [Globalization.CultureInfo]::InvariantCulture)
        $x2 = [double]::Parse($match.Groups["x2"].Value, [Globalization.CultureInfo]::InvariantCulture)
        if ([math]::Abs($x1 - $x2) -gt 0.001) {
            continue
        }

        [pscustomobject]@{
            X = $x1
            Y1 = [double]::Parse($match.Groups["y1"].Value, [Globalization.CultureInfo]::InvariantCulture)
            Y2 = [double]::Parse($match.Groups["y2"].Value, [Globalization.CultureInfo]::InvariantCulture)
            Width = [double]::Parse($match.Groups["width"].Value, [Globalization.CultureInfo]::InvariantCulture)
        }
    }

    $laneGroup = $verticalLines |
        Group-Object { "{0}|{1}|{2}" -f $_.Y1, $_.Y2, $_.Width } |
        Where-Object Count -ge 2 |
        Sort-Object Count -Descending |
        Select-Object -First 1

    if (-not $laneGroup) {
        throw "Cannot identify the vertical swimlane borders in the generated SVG."
    }

    $lines = $laneGroup.Group
    return [pscustomobject]@{
        Left = ($lines.X | Measure-Object -Minimum).Minimum
        Right = ($lines.X | Measure-Object -Maximum).Maximum
        Top = $lines[0].Y1
        Bottom = $lines[0].Y2
        Width = $lines[0].Width
    }
}

function Add-ClosedFrameToSvg {
    param(
        [Parameter(Mandatory)][string]$SvgPath,
        [Parameter(Mandatory)]$Bounds
    )

    $culture = [Globalization.CultureInfo]::InvariantCulture
    $left = $Bounds.Left.ToString("0.####", $culture)
    $right = $Bounds.Right.ToString("0.####", $culture)
    $top = $Bounds.Top.ToString("0.####", $culture)
    $bottom = $Bounds.Bottom.ToString("0.####", $culture)
    $width = $Bounds.Width.ToString("0.####", $culture)
    $frameLines = '<line data-frame="swimlane-top" style="stroke:#000000;stroke-width:' + $width + ';" x1="' + $left + '" x2="' + $right + '" y1="' + $top + '" y2="' + $top + '"/>' +
        '<line data-frame="swimlane-bottom" style="stroke:#000000;stroke-width:' + $width + ';" x1="' + $left + '" x2="' + $right + '" y1="' + $bottom + '" y2="' + $bottom + '"/>'

    $svg = [IO.File]::ReadAllText($SvgPath)
    if (-not $svg.EndsWith("</g></svg>")) {
        throw "Unexpected SVG structure: $SvgPath"
    }
    $svg = $svg.Substring(0, $svg.Length - 10) + $frameLines + "</g></svg>"
    [IO.File]::WriteAllText($SvgPath, $svg, [Text.Encoding]::ASCII)
}

function Add-ClosedFrameToPng {
    param(
        [Parameter(Mandatory)][string]$PngPath,
        [Parameter(Mandatory)]$Bounds
    )

    Add-Type -AssemblyName System.Drawing
    $source = [Drawing.Bitmap]::FromFile($PngPath)
    $bitmap = New-Object Drawing.Bitmap $source
    $source.Dispose()
    $graphics = [Drawing.Graphics]::FromImage($bitmap)
    $graphics.SmoothingMode = [Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $pen = New-Object Drawing.Pen ([Drawing.Color]::Black), ([single]$Bounds.Width)
    try {
        $graphics.DrawLine($pen, [single]$Bounds.Left, [single]$Bounds.Top, [single]$Bounds.Right, [single]$Bounds.Top)
        $graphics.DrawLine($pen, [single]$Bounds.Left, [single]$Bounds.Bottom, [single]$Bounds.Right, [single]$Bounds.Bottom)
    }
    finally {
        $pen.Dispose()
        $graphics.Dispose()
    }

    $temporaryPath = "$PngPath.tmp.png"
    try {
        $bitmap.Save($temporaryPath, [Drawing.Imaging.ImageFormat]::Png)
    }
    finally {
        $bitmap.Dispose()
    }
    Move-Item -LiteralPath $temporaryPath -Destination $PngPath -Force
}

$sourceRoot = (Resolve-Path -LiteralPath $InputDir).Path
$outputRoot = [IO.Path]::GetFullPath($OutputDir)
$jarPath = Get-PlantUmlJar
$sources = @(Get-ChildItem -LiteralPath $sourceRoot -Filter "*.puml" -Recurse -File)

if ($sources.Count -eq 0) {
    throw "No .puml activity diagram found in: $sourceRoot"
}

foreach ($source in $sources) {
    $relativeDirectory = [IO.Path]::GetRelativePath($sourceRoot, $source.DirectoryName)
    $targetDirectory = if ($relativeDirectory -eq ".") {
        $outputRoot
    }
    else {
        Join-Path $outputRoot $relativeDirectory
    }
    New-Item -ItemType Directory -Path $targetDirectory -Force | Out-Null

    & java -jar $jarPath -checkonly $source.FullName
    if ($LASTEXITCODE -ne 0) {
        throw "PlantUML validation failed: $($source.FullName)"
    }
    & java -jar $jarPath -tsvg -o $targetDirectory $source.FullName
    if ($LASTEXITCODE -ne 0) {
        throw "Cannot render SVG: $($source.FullName)"
    }
    & java -jar $jarPath -tpng -o $targetDirectory $source.FullName
    if ($LASTEXITCODE -ne 0) {
        throw "Cannot render PNG: $($source.FullName)"
    }

    $svgPath = Join-Path $targetDirectory ($source.BaseName + ".svg")
    $pngPath = Join-Path $targetDirectory ($source.BaseName + ".png")
    $svg = [IO.File]::ReadAllText($svgPath)
    $bounds = Get-SwimlaneBounds -SvgText $svg
    Add-ClosedFrameToSvg -SvgPath $svgPath -Bounds $bounds
    Add-ClosedFrameToPng -PngPath $pngPath -Bounds $bounds

    Write-Host "Rendered: $svgPath"
    Write-Host "Rendered: $pngPath"
}
