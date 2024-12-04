import sys
import subprocess
import tkinter as tk
from pathlib import Path
from functools import partial
import os
import importlib


def install_setuptools():
    try:
        # setuptools가 이미 설치되어 있는지 확인
        importlib.import_module('setuptools')
        print("setuptools가 이미 설치되어 있습니다.")
    except ImportError:
        print("setuptools가 설치되지 않았습니다. 설치 중...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "setuptools"])

# 패키지 설치 함수
def install_package(package_name):
    try:
        __import__(package_name)
    except ImportError:
        # 패키지가 없으면 설치 시도
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# setuptools 설치
install_setuptools()

# pkg_resources 설치 시도 (setuptools에 포함되므로 setuptools 설치 후 시도)
install_package("pkg_resources")
import pkg_resources

# requests 설치 시도
install_package("requests")
import requests

# PyQt5 설치 시도
install_package("PyQt5")
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QProgressBar
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon  # QIcon 임포트 추가

# Pillow 설치 시도
install_package("pillow")
from PIL import Image, ImageTk

# 현재 파일의 경로를 기반으로 디렉터리 경로 얻기
base_dir = os.path.dirname(os.path.abspath(__file__))  # __file__ 사용
img_dir = os.path.abspath(os.path.join(base_dir, "..", "img"))
program_dir = os.path.abspath(os.path.join(base_dir, "scrcpy_win64-for-hyper_plus-v001-030"))


# 프로그램 바로가기 세팅 - 해당 파일을 바꾸면 원하는 대로 기능의 커스텀이 가능합니다.
scrcpy = os.path.join(program_dir, "scrcpy.exe")  # Scrcpy
adb = os.path.join(program_dir, "adb.exe")  # adb
record = os.path.join(program_dir, "scrcpy-record.bat")  # Record 2 경로

# 이미지 파일 경로를 상위 디렉터리의 img 폴더로 변경 - 해당 파일을 바꾸면 원하는 대로 커스텀이 가능합니다.
image_paths = [
    os.path.join(img_dir, "0.png"),
    os.path.join(img_dir, "1.png"),
    os.path.join(img_dir, "2.png"),
    os.path.join(img_dir, "3.png"),
    os.path.join(img_dir, "4.png"),
    os.path.join(img_dir, "5.png"),
    os.path.join(img_dir, "6.png"),
    os.path.join(img_dir, "7.png"),
    os.path.join(img_dir, "8.png")
]
hyper_icon = os.path.join(img_dir, "Hyper+.ico")

# 현재 배경 이미지 인덱스 (초기값 0번번)
current_background_index = 0

# 배경 이미지 로드
def load_background(index):
    global current_background_index
    pixmap = QPixmap(image_paths[index])
    background_label.setPixmap(pixmap)
    current_background_index = index  # 현재 배경 이미지 업데이트

    # 배경 이미지에 따라 버튼 표시 여부 결정
    if current_background_index in [1, 2, 4, 6, 7, 8]: # 검증해야 함!!!!
        show_icons(False)
        camera_button.hide()
        record_button.hide()
    else:
        show_icons(True)
        camera_button.show()
        record_button.show()

    # 카메라 선택 버튼 표시 여부 결정
    if current_background_index in [0, 2, 3, 5, 7, 8]:  # 1, 4, 6번 이미지에서만 표기
        main_button.hide()
        front_button.hide()
        cancel_button.hide()
    else:
        main_button.show()
        front_button.show()
        cancel_button.show()

    # L버튼과 R버튼 표시 여부 결정
    if current_background_index in [7]:  # 7번 이미지에서 LR버튼 숨기기
        L_button.hide()
        R_button.hide()
        more_button.show()
        close_button.show()
        show_shortcuts(False)
    else:
        L_button.show()
        R_button.show()
        more_button.hide()
        close_button.hide()
        show_shortcuts(True)

# L버튼 클릭 이벤트 핸들러 (배경 이미지 변경)
def on_L_button_click():
    global current_background_index
    if current_background_index == 0:
        print("L - 배경 0 에서 배경 2으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 2
        load_background(new_index)
    elif current_background_index == 1:
        print("L - 배경 1 에서 배경 2으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 2
        load_background(new_index)
    elif current_background_index == 2:
        print("L - 배경 2 에서 배경 5으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 5
        load_background(new_index)
        print("L - 프로그램 실행")
        subprocess.Popen([adb, "shell", "setprop", "service.adb.tcp.port", "5555"])  # 특정 프로그램 실행
        subprocess.Popen([scrcpy, "--tcpip", "--window-title=Hyper+", "--stay-awake", "--window-width=400", "--push-target=/storage/emulated/0/Download/"])  # 특정 프로그램 실행
    elif current_background_index == 3:
        print("L - 배경 3 에서 배경 5으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 5
        load_background(new_index)
        print("L - 프로그램 실행")
        subprocess.Popen([scrcpy, "--tcpip", "-e", "--window-title=Hyper+", "--stay-awake", "--window-width=400", "--push-target=/storage/emulated/0/Download/"])  # 특정 프로그램 실행
    elif current_background_index == 4:
        print("L - 배경 4 에서 배경 5으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 5
        load_background(new_index)
        print("L - 프로그램 실행")
        subprocess.Popen([scrcpy, "--tcpip", "-e", "--window-title=Hyper+", "--stay-awake", "--window-width=400", "--push-target=/storage/emulated/0/Download/"])  # 특정 프로그램 실행
    elif current_background_index == 5:
        print("L - 프로그램 실행")
        subprocess.Popen([scrcpy, "--tcpip", "-e", "--window-title=Hyper+", "--stay-awake", "--window-width=400", "--push-target=/storage/emulated/0/Download/"])  # 특정 프로그램 실행
    elif current_background_index == 6:
        print("L - 프로그램 실행")
        subprocess.Popen([scrcpy, "--tcpip", "-e", "--window-title=Hyper+", "--stay-awake", "--window-width=400", "--push-target=/storage/emulated/0/Download/"])  # 특정 프로그램 실행
    elif current_background_index == 8:
        print("L - 배경 8 에서 배경 0으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 0
        load_background(new_index)
    else:
        print(f"L - 배경 {current_background_index + 1} - 특정 작업 없음")

# R버튼 클릭 이벤트 핸들러 (프로그램 실행)
def on_R_button_click():
    global current_background_index
    if current_background_index == 0:
        print("R - 배경 0 에서 배경 3으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 3
        load_background(new_index)
    elif current_background_index == 1:
        print("R - 배경 1 에서 배경 3으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 3
        load_background(new_index)
    elif current_background_index == 2:
        print("R - 배경 2 에서 배경 0으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 0
        load_background(new_index)
    elif current_background_index == 3:
        print("R - 배경 3 에서 배경 2으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 2
        load_background(new_index)
    elif current_background_index == 4:
        print("R - 배경 4 에서 배경 2으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 2
        load_background(new_index)
    elif current_background_index == 5:
        print("R - 배경 5 에서 배경 7으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 7
        load_background(new_index)
    elif current_background_index == 6:
        print("R - 배경 6 에서 배경 7으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 7
        load_background(new_index)
    elif current_background_index == 8:
        print("R - 배경 8 에서 링크 열기")
        subprocess.Popen(["python", "-m", "webbrowser", "https://discord.gg/eZahSkRJJb"])
    else:
        print(f"R - 배경 {current_background_index + 1} - 특정 작업 없음")

# 카메라 버튼 클릭 이벤트 핸들러 (배경 이미지 변경) - 수정해야 함!!!!
def on_camera_button_click():
    if current_background_index == 0:
        print("배경 0 에서 배경 1으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 1
        load_background(new_index)
    elif current_background_index == 3:
        print("배경 3 에서 배경 4으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 4
        load_background(new_index)
    elif current_background_index == 5:
        print("배경 5 에서 배경 6으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 6
        load_background(new_index)
    else:
        print(f"배경 {current_background_index + 1} - 특정 작업 없음")

# record 버튼 클릭 이벤트 핸들러 (프로그램 실행) - 검증해야 함!!!
def on_record_button_click():
    if current_background_index == 5:
        print("Main - 프로그램 실행")
        subprocess.Popen([record], stdout=subprocess.PIPE)  # 특정 프로그램 실행
    elif current_background_index == 0 or 3:
        print("Main - 프로그램 실행")
        subprocess.Popen([scrcpy, "--no-playback", "--audio-source=mic", "--window-title=Mic", "-e"], stdout=subprocess.PIPE)  # 특정 프로그램 실행
    else:
        print(f"배경 {current_background_index + 1} - 특정 작업 없음")


# 카메라 선택 버튼 클릭 이벤트 핸들러 (특정 프로그램 실행) - 검증해야 함!!!!
def on_main_button_click():
    print("Main - 프로그램 실행")
    subprocess.call([scrcpy, "--video-source=camera", "-e", "--camera-facing=back", "--camera-size=1920x1440", "--window-title=Main_Camera", "--window-width=400"], stdout=subprocess.PIPE)  # 특정 프로그램 실행
def on_front_button_click():
    print("front - 프로그램 실행")
    subprocess.call([scrcpy, "--video-source=camera", "-e", "--camera-facing=front", "--camera-size=1920x1440", "--orientation=270", "--window-title=Selfie_Camera", "--window-width=400"], stdout=subprocess.PIPE)  # 특정 프로그램 실행
def on_cancel_button_click():
    if current_background_index == 1:
        print("배경 1 에서 배경 0으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 0
        load_background(new_index)
    elif current_background_index == 4:
        print("배경 4 에서 배경 3으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 3
        load_background(new_index)
    elif current_background_index == 6:
        print("배경 6 에서 배경 5으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 5
        load_background(new_index)
    else:
        print(f"배경 {current_background_index + 1} - 특정 작업 없음")

    

# 각 아이콘 버튼 클릭 시 실행할 프로그램 설정
def on_icon_button_click(icon_id):
    print(f"아이콘 {icon_id + 1} 버튼 클릭 - 해당 프로그램 실행")
    # 예시: 각 버튼에 맞는 프로그램 실행
    if icon_id == 0:
        subprocess.Popen([scrcpy, "--new-display=1080x1920", "--start-app=com.miui.notes", "-e", "--window-title=Note", "--stay-awake", "--window-width=400"], stdout=subprocess.PIPE)  # 첫 번째 아이콘 클릭 시 메모장 실행
    elif icon_id == 1:
        subprocess.Popen([scrcpy, "--new-display=1080x1920", "--start-app=com.android.fileexplorer", "-e", "--window-title=Explorer", "--stay-awake", "--window-width=400"], stdout=subprocess.PIPE)  # 두 번째 아이콘 클릭 시 웹 브라우저 실행
    elif icon_id == 2:
        subprocess.Popen([scrcpy, "--new-display=1080x1920", "--start-app=com.miui.calculator", "-e", "--window-title=Calculator", "--stay-awake", "--window-width=400"], stdout=subprocess.PIPE)  # 세 번째 아이콘 클릭 시 계산기 실행
    elif icon_id == 3:
        subprocess.Popen([scrcpy, "--new-display=1080x1920", "--start-app=cn.wps.moffice_eng", "-e", "--window-title=WPS", "--stay-awake", "--window-width=400"], stdout=subprocess.PIPE)  # 네 번째 아이콘 클릭 시 MSN 실행
    elif icon_id == 4:
        subprocess.Popen([scrcpy, "--new-display=1080x1920", "--start-app=com.android.email", "-e", "--window-title=Mail", "--stay-awake", "--window-width=400"], stdout=subprocess.PIPE)  # 다섯 번째 아이콘 클릭 시 메모장 실행
    elif icon_id == 5:
        subprocess.Popen([scrcpy, "--new-display=1080x1920", "--start-app=com.xiaomi.smarthome", "-e", "--window-title=Mi Home", "--stay-awake", "--window-width=400"], stdout=subprocess.PIPE)  # 여섯 번째 아이콘 클릭 시 웹 브라우저 실행
    elif icon_id == 6:
        subprocess.Popen([scrcpy, "--new-display=1080x1920", "--start-app=com.android.contacts", "-e", "--window-title=Contacts", "--stay-awake", "--window-width=400"], stdout=subprocess.PIPE)  # 일곱 번째 아이콘 클릭 시 계산기 실행
    elif icon_id == 7:
        subprocess.Popen([scrcpy, "--new-display=1080x1920", "--start-app=com.android.mms", "-e", "--window-title=Messages", "--stay-awake", "--window-width=400"], stdout=subprocess.PIPE)  # 여덟 번째 아이콘 클릭 시 MSN 실행
    elif icon_id == 8:
        subprocess.Popen([scrcpy, "--new-display=1080x1920", "--start-app=com.miui.gallery", "-e", "--window-title=Gallery", "--stay-awake", "--window-width=400"], stdout=subprocess.PIPE)  # 아홉 번째 아이콘 클릭 시 메모장 실행

# 각 shortcut 버튼 클릭 시 실행할 프로그램 설정
def on_shortcut_button_click(icon_id):
    print(f"아이콘 {icon_id + 1} 버튼 클릭 - 해당 프로그램 실행")
    # 예시: 각 버튼에 맞는 프로그램 실행
    if icon_id == 0:
        print("배경 0으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 0
        load_background(new_index)
    elif icon_id == 1:
        print("배경 3으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 3
        load_background(new_index)
    elif icon_id == 2:
        print("배경 5으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 5
        load_background(new_index)
    elif icon_id == 3:
        print("배경 8으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 8
        load_background(new_index)

# 3x3 아이콘 버튼 표시/숨기기
def show_icons(visible):
    if visible:
        for i in range(9):
            row = i // 3
            col = i % 3
            x = 822 + col * 88
            y = 342 + row * 100
            icon_buttons[i].setGeometry(x, y, 75, 75)
            icon_buttons[i].show()
    else:
        for button in icon_buttons:
            button.hide()

# 숏컷 아이콘 버튼 표시/숨기기
def show_shortcuts(visible):
    if visible:
        for i in range(4):
            x = 290 + i * 55
            y = 593
            shortcut_buttons[i].setGeometry(x, y, 50, 50)
            shortcut_buttons[i].show()
    else:
        for button in shortcut_buttons:
            button.hide()

# More 버튼 클릭 시 링크 실행 (우선 순위를 위하여 상위 배치)
def on_more_button_click():
    print("more - 배경 7 에서 링크 열기")
    subprocess.Popen(["python", "-m", "webbrowser", "https://github.com/Edward-Lucas/Hyper-Plus/blob/master/doc/shortcuts.md"])

# close 버튼 클릭 시 이미지 변경 (우선 순위를 위하여 하위 배치)
def on_close_button_click():
    print("배경 7 에서 배경 5으로 변경")
    # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
    new_index = 5
    load_background(new_index)

# about 버튼 클릭 이벤트 핸들러 (프로그램 실행) - 검증해야 함!!!
def on_about_button_click():
    if current_background_index == 8:
        print("more - 배경 8 에서 링크 열기")
        subprocess.Popen(["python", "-m", "webbrowser", "https://github.com/Edward-Lucas/Hyper-Plus"])
    else:
        print("아무 배경에서 배경 8으로 변경")
        # 새로운 배경 이미지 인덱스 (특정 이미지로 변경)
        new_index = 8
        load_background(new_index)

# PyQt 애플리케이션 설정
app = QApplication(sys.argv)

# 메인 윈도우 생성
window = QWidget()
window.setWindowTitle("Hyper+")
window.setWindowIcon(QIcon(hyper_icon))  # type: ignore # 아이콘 파일 경로
window.setFixedSize(1280, 800)  # 크기 설정 (1280x720)

# 배경 이미지 라벨 설정
background_label = QLabel(window)
background_label.setGeometry(0, 0, 1280, 800)  # 배경 이미지 크기 설정

# L버튼, R버튼 생성
L_button = QPushButton("", window)
L_button.setStyleSheet("background-color: transparent; border: none;")
L_button.clicked.connect(on_L_button_click)
L_button.setGeometry(175, 490, 210, 60)

R_button = QPushButton("", window)
R_button.setStyleSheet("background-color: transparent; border: none;")
R_button.clicked.connect(on_R_button_click)
R_button.setGeometry(410, 490, 210, 60)

# camera 버튼 생성
camera_button = QPushButton("", window)
camera_button.setStyleSheet("background-color: transparent; border: none;")
camera_button.clicked.connect(on_camera_button_click)
camera_button.setGeometry(910, 148, 163, 172)

# Record 버튼 생성
record_button = QPushButton("", window)
record_button.setStyleSheet("background-color: transparent; border: none;")
record_button.clicked.connect(on_record_button_click)
record_button.setGeometry(822, 147, 75, 174)

# camera 선택 버튼 생성
main_button = QPushButton("", window)
main_button.setStyleSheet("background-color: transparent; border: none;")
main_button.clicked.connect(on_main_button_click)
main_button.setGeometry(821, 165, 252, 50)

front_button = QPushButton("", window)
front_button.setStyleSheet("background-color: transparent; border: none;")
front_button.clicked.connect(on_front_button_click)
front_button.setGeometry(821, 228, 252, 50)

cancel_button = QPushButton("", window)
cancel_button.setStyleSheet("background-color: transparent; border: none;")
cancel_button.clicked.connect(on_cancel_button_click)
cancel_button.setGeometry(946, 296, 126, 41)


# 3x3 아이콘 버튼 생성
icon_buttons = []
for i in range(9):
    icon_button = QPushButton(f"", window)
    icon_button.setStyleSheet("background-color: transparent; border: none;")
    icon_button.clicked.connect(partial(on_icon_button_click, i))
    icon_buttons.append(icon_button)

shortcut_buttons = []
for i in range(4):
    shortcut_button = QPushButton(f"", window)
    shortcut_button.setStyleSheet("background-color: transparent; border: none;")
    shortcut_button.clicked.connect(partial(on_shortcut_button_click, i))
    shortcut_buttons.append(shortcut_button)

    
# close 버튼 생성
close_button = QPushButton("", window)
close_button.setStyleSheet("background-color: transparent; border: none;")
close_button.clicked.connect(on_close_button_click)
close_button.setGeometry(0, 0, 1280, 800)

# more 버튼 생성
more_button = QPushButton("", window)
more_button.setStyleSheet("background-color: transparent; border: none;")
more_button.clicked.connect(on_more_button_click)
more_button.setGeometry(891, 531, 256, 136)

# about 버튼 생성
about_button = QPushButton("", window)
about_button.setStyleSheet("background-color: transparent; border: none;")
about_button.clicked.connect(on_about_button_click)
about_button.setGeometry(1160, 750, 120, 50)

# 초기 배경 설정
load_background(0)

# 윈도우 표시
window.show()
sys.exit(app.exec_())
