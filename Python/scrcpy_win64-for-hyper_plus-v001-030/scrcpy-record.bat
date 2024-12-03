pushd "%~dp0"
set filename=%date:-=_%-%time::=%
set filename=%filename:.=%
set filename=%filename: =%

set "btitle=Hyper+ 화면 녹화 시작됨"
set "text=중단하려면 새로운 창을 닫으세요."
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