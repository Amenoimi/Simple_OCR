import cv2

# 選擇第二隻攝影機
cap = cv2.VideoCapture(0)
while(True):
  # 從攝影機擷取一張影像
  ret, frame = cap.read()
  cv2.putText(frame, "aaqqqqqqqqqqqq", (0,100), cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,0))
  # 顯示圖片
  cv2.imshow('frame', frame)
  cv2.waitKey(1)
  if cv2.getWindowProperty('frame', cv2.WND_PROP_AUTOSIZE) == -1:        
    break
# 釋放攝影機
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()