from gtts import gTTS
from playsound import playsound
import os

#################################
# 텍스트를 음성으로 변환후 실행   #
# 2023.04.02                    #
#################################

# '지정한 장치가 열려 있지 않거나 MCI에서 인식되지 않습니다' 라고 에러가 떴지만,
# pip install playsound==1.2.2 로 다운그레이드시 실행되었다.
# 최신버전은 에러가 발생했던것! 2023.04.02 일 기준

# 경로를 .py 파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS(text=text, lang='ko')
tts.save("hi.mp3")

playsound("hi.mp3")