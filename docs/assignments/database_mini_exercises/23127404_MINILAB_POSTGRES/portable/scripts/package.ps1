$ErrorActionPreference = "Stop"
$portableRoot = Split-Path -Parent $PSScriptRoot
$labRoot = Split-Path -Parent $portableRoot
$parent = Split-Path -Parent $labRoot
$folderName = Split-Path -Leaf $labRoot
$zipPath = Join-Path $parent "$folderName.zip"
$stageRoot = Join-Path ([IO.Path]::GetTempPath()) "minilab-23127404-package"
$stageLab = Join-Path $stageRoot $folderName

$resolvedTemp = [IO.Path]::GetFullPath($stageRoot)
$systemTemp = [IO.Path]::GetFullPath([IO.Path]::GetTempPath())
if (-not $resolvedTemp.StartsWith($systemTemp, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing to use a staging directory outside the system temporary directory."
}

if (Test-Path -LiteralPath $stageRoot) {
    Remove-Item -LiteralPath $stageRoot -Recurse -Force
}
New-Item -ItemType Directory -Force -Path $stageRoot | Out-Null
Copy-Item -LiteralPath $labRoot -Destination $stageLab -Recurse

@(
    (Join-Path $stageLab "portable\node_modules")
) | ForEach-Object {
    if (Test-Path -LiteralPath $_) {
        Remove-Item -LiteralPath $_ -Recurse -Force
    }
}

if (Test-Path -LiteralPath $zipPath) {
    Remove-Item -LiteralPath $zipPath -Force
}
Compress-Archive -LiteralPath $stageLab -DestinationPath $zipPath -CompressionLevel Optimal
Remove-Item -LiteralPath $stageRoot -Recurse -Force

Write-Host "Created portable archive: $zipPath"
