@echo off
:: Python ��ġ ���� Ȯ��
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python�� ��ġ�Ǿ� ���� �ʽ��ϴ�.
    echo Python�� ��ġ�մϴ�...
    
    :: �ȳ� �޽��� ���
    echo Python ��ġ ��...
    
    winget install -e --id Python.Python.3.10
    
    echo Python ��ġ�� �Ϸ�Ǿ����ϴ�.
) else (
    echo Python�� �̹� ��ġ�Ǿ� �ֽ��ϴ�.
)

:: ���� ��ġ���� Python ������ �̵�
cd /d %~dp0
cd Python
Python Main.py

pause