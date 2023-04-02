# pip install qrcode로 먼저 라이브러리 설치할것!
import qrcode

qr_data = 'www.naver.com'
qr_img = qrcode.make(qr_data)

save_path = '4. QR코드 생성기\\' + qr_data + '.png'

# 코드를 생성해서 저장
qr_img.save(save_path)