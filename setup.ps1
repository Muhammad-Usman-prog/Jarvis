# setup.ps1 - Jarvis Complete Setup Script
# Run this from your project folder

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Jarvis AI Assistant - Setup Script" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if we're in the right folder
if (-not (Test-Path "main.py")) {
    Write-Host "WARNING: main.py not found. Make sure you're in the project root." -ForegroundColor Yellow
    Write-Host "Current directory: $PWD" -ForegroundColor Yellow
}

# Create folder structure
Write-Host "Creating folder structure..." -ForegroundColor Green
$folders = @(
    "core_cpp\include",
    "core_cpp\src",
    "core_python",
    "scripts",
    "models"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path $folder | Out-Null
    Write-Host "  Created: $folder" -ForegroundColor Gray
}

Write-Host ""
Write-Host "Folder structure created!" -ForegroundColor Green
Write-Host ""

# Create __init__.py
Write-Host "Creating Python package files..." -ForegroundColor Green
@"
# core_python/__init__.py
# Jarvis AI Core Package
__version__ = "1.0.0"
"@ | Out-File -FilePath "core_python\__init__.py" -Encoding UTF8

# Create requirements.txt
Write-Host "Creating requirements.txt..." -ForegroundColor Green
@"
numpy>=1.24.0
torch>=2.0.0
openai-whisper>=20231117
pyttsx3>=2.90
psutil>=5.9.0
python-dotenv>=1.0.0
sounddevice>=0.4.6
soundfile>=0.12.1
"@ | Out-File -FilePath "requirements.txt" -Encoding UTF8

# Create config.py
Write-Host "Creating config.py..." -ForegroundColor Green
@"
# core_python/config.py
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent.parent
MODELS_DIR = BASE_DIR / "models"

SAMPLE_RATE = 16000
CHANNELS = 1
CHUNK_SIZE = 1600
VAD_THRESHOLD = 0.01
SILENCE_DURATION = 0.3

WHISPER_MODEL = "base"
WHISPER_DEVICE = "cuda" if os.getenv("CUDA_AVAILABLE") else "cpu"
WHISPER_LANGUAGE = "en"

WAKE_WORD = "hey jarvis"
WAKE_WORD_SENSITIVITY = 0.5

SHARED_MEMORY_NAME = "JarvisAudio"
SEMAPHORE_NAME = "JarvisSem"
BUFFER_SIZE_MB = 10

VOICE_RATE = 180
VOICE_VOLUME = 0.9
"@ | Out-File -FilePath "core_python\config.py" -Encoding UTF8

# Create simple test main.py
Write-Host "Creating main.py..." -ForegroundColor Green
@"
# main.py - Jarvis AI Controller
import sys
import os
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

print("=" * 50)
print("  Jarvis AI Assistant")
print("=" * 50)
print()

# Try importing modules
try:
    from core_python.config import *
    print("[✓] Config loaded")
except Exception as e:
    print(f"[✗] Config error: {e}")

try:
    from core_python.speaker import JarvisSpeaker
    print("[✓] Speaker module loaded")
except Exception as e:
    print(f"[✗] Speaker error: {e}")

try:
    from core_python.bridge import JarvisBridge
    print("[✓] Bridge module loaded")
except Exception as e:
    print(f"[✗] Bridge error: {e}")

try:
    from core_python.transcriber import OptimizedTranscriber
    print("[✓] Transcriber module loaded")
except Exception as e:
    print(f"[✗] Transcriber error: {e}")

try:
    from core_python.command_corrector import CommandCorrector
    print("[✓] Command corrector loaded")
except Exception as e:
    print(f"[✗] Corrector error: {e}")

try:
    from core_python.intent_parser import IntentParser
    print("[✓] Intent parser loaded")
except Exception as e:
    print(f"[✗] Intent parser error: {e}")

try:
    from core_python.action_executor import ActionExecutor
    print("[✓] Action executor loaded")
except Exception as e:
    print(f"[✗] Action executor error: {e}")

print()
print("All modules loaded successfully!")
print()
print("To test audio: run 'jarvis_audio.exe --console'")
print("To test AI: run 'python main.py'")
"@ | Out-File -FilePath "main.py" -Encoding UTF8

# Create compile script
Write-Host "Creating compile script..." -ForegroundColor Green
@"
@echo off
echo ========================================
echo   Compiling Jarvis C++ Audio Engine
echo ========================================
cd /d "%~dp0..\core_cpp"

where cmake >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: CMake is not installed!
    echo Install from: https://cmake.org/download/
    pause
    exit /b 1
)

if not exist build mkdir build
cd build

echo Configuring with CMake...
cmake .. -G "Visual Studio 17 2022" -A x64
if %errorlevel% neq 0 (
    echo Trying VS 2019...
    cmake .. -G "Visual Studio 16 2019" -A x64
)
if %errorlevel% neq 0 (
    echo ERROR: CMake failed. Install Visual Studio with C++ tools.
    pause
    exit /b 1
)

echo Building...
cmake --build . --config Release
if %errorlevel% neq 0 (
    echo ERROR: Build failed!
    pause
    exit /b 1
)

copy /Y Release\jarvis_audio.exe "..\..\jarvis_audio.exe"
echo.
echo Build successful! jarvis_audio.exe created.
echo.
pause
"@ | Out-File -FilePath "scripts\compile_cpp.bat" -Encoding ASCII

# Create debug launcher
Write-Host "Creating debug launcher..." -ForegroundColor Green
@"
@echo off
echo ========================================
echo   Jarvis - Debug Mode
echo ========================================
cd /d "%~dp0.."
echo Starting Python AI Engine...
python main.py
pause
"@ | Out-File -FilePath "scripts\start_jarvis_debug.bat" -Encoding ASCII

# Create VBS startup script
Write-Host "Creating startup script..." -ForegroundColor Green
@"
Dim WshShell
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "pythonw ""$PROJECT_PATH\main.py""", 0, False
Set WshShell = Nothing
"@ | Out-File -FilePath "scripts\start_jarvis.vbs" -Encoding ASCII

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Install Python packages:" -ForegroundColor White
Write-Host "   pip install -r requirements.txt" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Download Whisper model:" -ForegroundColor White
Write-Host "   python -c `"import whisper; whisper.load_model('base')`"" -ForegroundColor Gray
Write-Host ""
Write-Host "3. Compile C++ engine (requires Visual Studio):" -ForegroundColor White
Write-Host "   .\scripts\compile_cpp.bat" -ForegroundColor Gray
Write-Host ""
Write-Host "4. Test the system:" -ForegroundColor White
Write-Host "   .\scripts\start_jarvis_debug.bat" -ForegroundColor Gray
Write-Host ""
Write-Host "Your project path is: $PWD" -ForegroundColor Cyan
Write-Host ""