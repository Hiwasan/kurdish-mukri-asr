# Save this as: create_kurdish_project.ps1
Write-Host "🏗️ CREATING KURDISH WAV2GLOSS PROJECT STRUCTURE" -ForegroundColor Green
Write-Host "=" * 60

# Base directory for your Kurdish project
$kurdishProjectPath = "C:\Kurdish_WAV2GLOSS"
New-Item -ItemType Directory -Path $kurdishProjectPath -Force

# Create the main data structure
$dataStructure = @(
    "raw_audio",
    "processed_audio", 
    "transcriptions",
    "gloss_data",
    "wav2gloss_input\sorani\train",
    "wav2gloss_input\sorani\dev", 
    "wav2gloss_input\sorani\test",
    "wav2gloss_input\sorani\train\audio",
    "wav2gloss_input\sorani\dev\audio",
    "wav2gloss_input\sorani\test\audio",
    "wav2gloss_output"
)

foreach ($dir in $dataStructure) {
    New-Item -ItemType Directory -Path "$kurdishProjectPath\$dir" -Force
    Write-Host "✅ Created: $dir"
}

Write-Host "`n📁 Project structure created at: $kurdishProjectPath" -ForegroundColor Cyan

# Show the structure
Write-Host "`n📂 PROJECT STRUCTURE:" -ForegroundColor Yellow
Get-ChildItem $kurdishProjectPath -Recurse | Where-Object { $_.PSIsContainer } | Select-Object FullName

Write-Host "`n" + "=" * 60
Write-Host "✅ Kurdish project structure ready!" -ForegroundColor Green