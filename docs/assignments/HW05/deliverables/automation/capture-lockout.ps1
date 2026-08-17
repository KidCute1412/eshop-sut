param([ValidateSet('invalid','valid')][string]$Mode)

$url = 'http://localhost:3000/api/login'
function Invoke-LoginEvidence([string]$password) {
  $body = @{ email = 'test@eshop.com'; password = $password } | ConvertTo-Json -Compress
  try {
    $response = Invoke-WebRequest -Uri $url -Method Post -ContentType 'application/json' -Body $body -ErrorAction Stop
    Write-Host "HTTP $($response.StatusCode)" -ForegroundColor Cyan
    Write-Output $response.Content
  } catch {
    $response = $_.Exception.Response
    if ($null -eq $response) { throw }
    $reader = New-Object System.IO.StreamReader($response.GetResponseStream())
    $content = $reader.ReadToEnd()
    Write-Host "HTTP $([int]$response.StatusCode)" -ForegroundColor Cyan
    Write-Output $content
  }
}
if ($Mode -eq 'invalid') {
  1..3 | ForEach-Object {
    Write-Host "ATTEMPT $_" -ForegroundColor Yellow
    Invoke-LoginEvidence 'WrongPassword123!'
    Write-Host ''
  }
  exit
}

Write-Host 'RESET VERIFICATION' -ForegroundColor Green
Invoke-LoginEvidence 'Test1234!'
