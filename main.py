import cv2
import numpy as np

# 비디오 파일 열기
cap = cv2.VideoCapture(0)

while True:
    # 프레임 읽기
    ret, frame = cap.read()

    if not ret:
        break

    # 이미지 처리 코드
    lane_image = np.copy(frame)
    gray = cv2.cvtColor(lane_image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)

    # 결과 화면에 표시
    cv2.imshow("result", canny)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 파일 닫기
cap.release()
cv2.destroyAllWindows()
