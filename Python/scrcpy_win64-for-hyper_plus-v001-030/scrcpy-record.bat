pushd "%~dp0"
set filename=%date:-=_%-%time::=%
set filename=%filename:.=%
set filename=%filename: =%

set "btitle=Hyper+ ȭ�� ��ȭ ���۵�"
set "text=�ߴ��Ϸ��� ���ο� â�� ��������."
set "icon=info"

(echo [void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms"^)
echo $objNotifyIcon = New-Object System.Windows.Forms.NotifyIcon
echo $objNotifyIcon.Icon = [System.Drawing.SystemIcons]::Information
echo $objNotifyIcon.BalloonTipIcon = "%icon%"
echo $objNotifyIcon.BalloonTipTitle = "%btitle%"
echo $objNotifyIcon.BalloonTipText = "%text%"
echo $objNotifyIcon.Visible = $True
echo $objNotifyIcon.ShowBalloonTip(10000^))>%temp%\notification.ps1
powershell -noprofile -executionpolicy bypass -file %temp%\notification.ps1 | more
del /q %temp%\notification.ps1

scrcpy --no-playback --record C:\Users\%username%\Videos\Hyper+\%filename%-hyper+record.mkv --window-title="Close Window, Stop Record"
pause