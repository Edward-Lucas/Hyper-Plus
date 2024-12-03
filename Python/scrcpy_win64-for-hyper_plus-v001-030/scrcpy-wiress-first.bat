pushd "%~dp0"
adb shell setprop service.adb.tcp.port 5555
scrcpy --tcpip --window-title=Hyper+ --push-target=/storage/emulated/0/Download/Hyper+/
pause