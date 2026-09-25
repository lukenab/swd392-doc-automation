[CmdletBinding()]
param(
    [string]$OutputDir = (Join-Path $PSScriptRoot "output")
)

$ErrorActionPreference = "Stop"
$dataDir = Join-Path $PSScriptRoot "data"

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

Write-Host "[1/3] Validate Use Case descriptions"
Invoke-Checked -Step "Document validation" -Command {
    & py (Join-Path $PSScriptRoot "cli.py") --data-dir $dataDir validate
}

Write-Host "[2/3] Generate Markdown documentation"
Invoke-Checked -Step "Markdown generation" -Command {
    & py (Join-Path $PSScriptRoot "cli.py") --data-dir $dataDir build --format markdown --output-dir $OutputDir
}

Write-Host "[3/3] Generate DOCX documentation"
Invoke-Checked -Step "DOCX generation" -Command {
    & py (Join-Path $PSScriptRoot "cli.py") --data-dir $dataDir build --format docx --output-dir $OutputDir
}

Write-Host "Build completed: $OutputDir"
