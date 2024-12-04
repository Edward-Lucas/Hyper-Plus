@echo off
:: Python 설치 여부 확인
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python이 설치되어 있지 않습니다.
    echo Python을 설치합니다...
    
    :: 안내 메시지 출력
    echo Python 설치 중...
    
    winget install -e --id Python.Python.3.10
    
    echo Python 설치가 완료되었습니다.
) else (
    echo Python이 이미 설치되어 있습니다.
)

:: 현재 위치에서 Python 폴더로 이동
cd /d %~dp0
cd Python
Python Main.py

pause