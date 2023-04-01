from gtts import gTTS
from playsound import playsound
import os

##############################################
# 파일에서 문자를 읽어 음성으로 출력하는 코드    #
# 2023.04.02                                 #
##############################################

# '지정한 장치가 열려 있지 않거나 MCI에서 인식되지 않습니다' 라고 에러가 떴지만,
# pip install playsound==1.2.2 로 다운그레이드시 실행되었다.
# 최신버전은 에러가 발생했던것! 2023.04.02 일 기준

# 경로를 .py 파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 개인적으로, 파일 읽어오는 절차가 자바와 비교해서 굉장히 편하다고 생각한다.
file_path = '나의텍스트.txt'
with open(file_path, 'rt', encoding= 'UTF8') as f:
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')
tts.save("hi.mp3")

playsound("hi.mp3")