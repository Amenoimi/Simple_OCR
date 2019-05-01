import cv2
import numpy as np

# mouse callback function
def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image[y,x]

        #you might want to adjust the ranges(+-10, etc):
        upper =  np.array([pixel[0] + 20, pixel[1] + 50, pixel[2] + 50])
        lower =  np.array([pixel[0] - 20, pixel[1] - 50, pixel[2] - 50])
        print(pixel, lower, upper)

       


cap = cv2.VideoCapture(0)
while(True):
  # 從攝影機擷取一張影像
  ret, image = cap.read()
  cv2.setMouseCallback('image', pick_color)
  # 顯示圖片
  cv2.imshow('image', image)
  cv2.waitKey(1)
  if cv2.getWindowProperty('image', cv2.WND_PROP_AUTOSIZE) == -1:        
    break
# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()
