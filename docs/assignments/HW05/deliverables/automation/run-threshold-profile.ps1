param(
  [Parameter(Mandatory=$true)][string]$Plan,
  [Parameter(Mandatory=$true)][string]$Profile
)

$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$repo = (Resolve-Path (Join-Path $root '..\..\..\..')).Path
$jmeter = Join-Path $repo '.tools\apache-jmeter-5.6.3\bin\jmeter.bat'
$data = Join-Path $root 'test-data\workflow.csv'
$resultDir = Join-Path $root "raw-results\threshold\$Profile"
$htmlDir = Join-Path $root "html-reports\threshold\$Profile"
$monitor = Join-Path $resultDir 'node-resource-samples.csv'
$jtl = Join-Path $resultDir "$Profile.jtl"
New-Item -ItemType Directory -Force -Path $resultDir | Out-Null
New-Item -ItemType Directory -Force -Path (Split-Path $htmlDir -Parent) | Out-Null
if (Test-Path $htmlDir) { throw "HTML output already exists: $htmlDir" }

$node = Start-Process -FilePath 'node.exe' -ArgumentList 'server.js' -WorkingDirectory (Join-Path $repo 'backend') -WindowStyle Hidden -PassThru
Start-Sleep -Seconds 2
$monitorJob = Start-Job -ArgumentList $node.Id -ScriptBlock {
  param($nodeProcessId)
  $lastCpu = 0.0
  $lastAt = Get-Date
  while ($true) {
    $process = Get-Process -Id $nodeProcessId -ErrorAction SilentlyContinue
    if ($null -eq $process) { break }
    $now = Get-Date
    $elapsed = ($now - $lastAt).TotalSeconds
    $cpu = if ($elapsed -gt 0) { [math]::Round((($process.CPU - $lastCpu) / $elapsed) * 100, 2) } else { 0 }
    [pscustomobject]@{Timestamp=$now.ToString('o');NodePid=$nodeProcessId;CpuPercentOneCore=$cpu;WorkingSetMiB=[math]::Round($process.WorkingSet64/1MB,2);PrivateMemoryMiB=[math]::Round($process.PrivateMemorySize64/1MB,2)}
    $lastCpu = $process.CPU
    $lastAt = $now
    Start-Sleep -Seconds 1
  }
}
try {
  & $jmeter -n -t $Plan "-JdataFile=$data" -l $jtl -e -o $htmlDir
  if ($LASTEXITCODE -ne 0) { throw "JMeter failed with exit code $LASTEXITCODE" }
} finally {
  Stop-Process -Id $node.Id -Force -ErrorAction SilentlyContinue
  Wait-Job $monitorJob | Out-Null
  Receive-Job $monitorJob | Export-Csv -NoTypeInformation -Encoding utf8 $monitor
  Remove-Job $monitorJob -Force
}
Write-Output "JTL=$jtl"
Write-Output "MONITOR=$monitor"
