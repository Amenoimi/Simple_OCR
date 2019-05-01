import pytesseract
from PIL import Image
# #1.引入Tesseract程式
# pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\\tesseract.exe'
# #2.使用Image模組下的Open()函式開啟圖片
# image = Image.open('APPLE.jpg',mode='r')
# print(image)
# #3.識別圖片文字
# code= pytesseract.image_to_string(image)
# print(code)


import cv2

# 引入Tesseract程式
pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\\tesseract.exe'

show_text=""
# 選擇第二隻攝影機
cap = cv2.VideoCapture(0)
while(True):
  # 從攝影機擷取一張影像
  ret, frame = cap.read()
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#   frame =cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
  text = Image.fromarray(frame)
  code= pytesseract.image_to_string(text)
  if code!="":
    print("t:", code.encode("utf8").decode("cp950", "ignore"))
    show_text=code.encode("utf8").decode("cp950", "ignore")
  cv2.putText(frame,show_text, (0,100), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,0))
  # 顯示圖片
  cv2.imshow('frame', frame)
  cv2.waitKey(1)
  if cv2.getWindowProperty('frame', cv2.WND_PROP_AUTOSIZE) == -1:        
    break
# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()