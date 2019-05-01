
from PIL import Image

import cv2


# 選擇第二隻攝影機
cap = cv2.VideoCapture(0)
while(True):
  # 從攝影機擷取一張影像
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(frame, 100 , 200)
    # img_fc, contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # hierarchy = hierarchy[0]
    # found = []
    # for i in range(len(contours)):
    #     k = i
    #     c = 0
    # while hierarchy[k][2] != -1:
    #     k = hierarchy[k][2]
    #     c = c + 1
    # if c >= 5:
    #     found.append(i)
        
    # for i in found:
    #     cv2.drawContours(frame, contours, i, (0, 255, 0), 3)
    
    (_, cnts, _) = cv2.findContours(blurred.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) > 0:
        for cnt in cnts:
          # compute the (rotated) bounding box around then
          # contour and then draw it		
          rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
          cv2.drawContours(self.frame, [rect], -1, (0, 255, 0), 2)



     # 顯示圖片
    cv2.imshow('frame', edges)
    cv2.waitKey(1)
    if cv2.getWindowProperty('frame', cv2.WND_PROP_AUTOSIZE) == -1:        
        break
# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()