
from PIL import Image
import numpy as np

import cv2


class color_see():
  def pick_color(self,event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
       self.pixel = self.frame[y,x]
    #you might want to adjust the ranges(+-10, etc):
    self.upper =  np.array([ self.pixel[0] + 20,  self.pixel[1] + 20,  self.pixel[2] + 20])
    self.lower =  np.array([ self.pixel[0] - 20,  self.pixel[1] - 20,  self.pixel[2] - 20])
    print( self.pixel, self.lower, self.upper)

  def __init__(self):
    self.lower = np.array([0, 0, 0])
    self.upper = np.array([0, 0, 0])
    # mouse callback function
   

    # 選擇第二隻攝影機
    cap = cv2.VideoCapture(0)
    while(True):
      # 從攝影機擷取一張影像
      ret, self.frame = cap.read()
      cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)

      cv2.setMouseCallback('frame', self.pick_color)

      filtered = cv2.inRange(self.frame, self.lower, self.upper)
      blurred = cv2.GaussianBlur(filtered, (25, 15), 0)

      # find contours in the image
      (_, cnts, _) = cv2.findContours(blurred.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      if len(cnts) > 0:
        for cnt in cnts:
          # compute the (rotated) bounding box around then
          # contour and then draw it		
          rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
          cv2.drawContours(self.frame, [rect], -1, (0, 255, 0), 2)

      # 顯示圖片
      cv2.imshow('frame', self.frame)
      cv2.waitKey(1)
      if cv2.getWindowProperty('frame', cv2.WND_PROP_AUTOSIZE) == -1:        
        break
    # 釋放攝影機
    cap.release()

    # 關閉所有 OpenCV 視窗
    cv2.destroyAllWindows()


if __name__ == '__main__':
  p = color_see()