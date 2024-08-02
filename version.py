import cv2
import face_recognition
import time

frame_skip = 5
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    if frame_count % frame_skip == 0:
        # Yüz tespiti işlemlerini burada yapın
        face_locations = face_recognition.face_locations(frame)
        # Diğer yüz tespiti işlemleri
    else:
        # Yüz tespiti yapılmadan sadece FPS hesaplama
        new_frame_time = time.time()
        fps = 1 / (new_frame_time - prev_frame_time)
        prev_frame_time = new_frame_time
        fps_text = f'FPS: {fps:.2f}'
        cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Çerçeveyi göster
    cv2.imshow('Kamera', frame)

    # 'q' tuşuna basılınca çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
