import cv2
from pyzbar import pyzbar

rtsp_url = "your/rtsp/url/here"
cap = cv2.VideoCapture(rtsp_url)

while True:
    ret, frame = cap.read()
    cv2.imshow("QR Code Scanner", frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    decoded = pyzbar.decode(gray)

    for obj in decoded:
        print("Decoded QR: ", obj.data)

    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()