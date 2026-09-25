[CmdletBinding()]
param(
    [string]$DiagramTool = (Join-Path $PSScriptRoot "..\swd392-usecase-diagram-tool"),
    [string]$OutputDir = (Join-Path $PSScriptRoot "output")
)

$ErrorActionPreference = "Stop"
$dataDir = Join-Path $PSScriptRoot "data"
$diagramOutput = Join-Path $OutputDir "diagrams"

function Invoke-Checked {
    param(
        [Parameter(Mandatory)]
        [scriptblock]$Command,
        [Parameter(Mandatory)]
        [string]$Step
    )
    & $Command
    if ($LASTEXITCODE -ne 0) {
        throw "$Step failed with exit code $LASTEXITCODE."
    }
}

if (-not (Test-Path -LiteralPath (Join-Path $DiagramTool "package.json"))) {
    throw "Diagram tool not found: $DiagramTool"
}

Write-Host "[1/5] Validate Use Case descriptions"
Invoke-Checked -Step "Document validation" -Command {
    & py (Join-Path $PSScriptRoot "cli.py") --data-dir $dataDir validate
}

Push-Location $DiagramTool
try {
    Write-Host "[2/5] Validate Use Case diagrams"
    Invoke-Checked -Step "Diagram validation" -Command {
        & npm run cli -- validate --input $dataDir
    }

    Write-Host "[3/5] Generate SVG, PNG and DOT diagrams"
    Invoke-Checked -Step "Diagram generation" -Command {
        & npm run cli -- build --input $dataDir --output $diagramOutput --format svg,png,dot
    }
}
finally {
    Pop-Location
}

Write-Host "[4/5] Generate Markdown documentation"
Invoke-Checked -Step "Markdown generation" -Command {
    & py (Join-Path $PSScriptRoot "cli.py") --data-dir $dataDir build --format markdown --output-dir $OutputDir
}

Write-Host "[5/5] Generate DOCX with embedded diagrams"
Invoke-Checked -Step "DOCX generation" -Command {
    & py (Join-Path $PSScriptRoot "cli.py") --data-dir $dataDir build --format docx --output-dir $OutputDir --diagram-dir $diagramOutput
}

Write-Host "Build completed: $OutputDir"
