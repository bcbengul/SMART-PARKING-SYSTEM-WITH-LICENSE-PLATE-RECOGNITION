# Raspberry Pi Main Code (Camera + Recognition + Logging + Servo)
import time
from datetime import datetime, timezone
from config import CAMERA_SOURCE, CAMERA_ID, EVENT_IMAGES_DIR
from recognizer import recognize_plate_from_frame, PlateRecognitionError
from file_store import log_event, ensure_dirs, load_authorized_plates
from servo_control import open_barrier, close_barrier, cleanup as servo_cleanup
def main(): print("[DEBUG] main() çağrıldı")
ensure_dirs()
print("[INFO] Kamera açılıyor...")
cap = cv2.VideoCapture(CAMERA_SOURCE)
# Logitech C310 için çözünürlük
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
if not cap.isOpened(): print("[ERROR] Kamera açılamadı! CAMERA_SOURCE =", CAMERA_SOURCE)
return
print("[INFO] Sistem çalışıyor. Pencereyi kapatmak için 'q' tuşuna bas.")
# Aynı plakayı sürekli loglamamak / servo’yu sürekli oynatmamak için
last_plate = None
last_ts = None
# Yetkili plakalar
authorized_set = load_authorized_plates() print(f"[INFO] Yüklenen yetkili plaka sayısı: {len(authorized_set)}")
try:
while True:
ret, frame = cap.read()
if not ret: print("[WARN] Kare okunamadı, tekrar deneniyor...")
continue
# Varsayılan overlay overlay_text = "No plate"
overlay_color = (0, 255, 255) # sarı
# Zaman bilgisini bir kez al
now = datetime.now(timezone.utc)
ts_str = now.isoformat()
try:
result = recognize_plate_from_frame(frame)
except PlateRecognitionError as e: print("[ERROR] OpenALPR hata:", e)
result = None
if result:
# 1) OpenALPR'ın en iyi tahmini base_plate = (result["plate"] or "").upper() confidence = result["confidence"] candidates = result.get("candidates", []) or []
# 2) Varsayılan: en iyi tahmin + UNAUTHORIZED
final_plate = base_plate status = "UNAUTHORIZED"
# 3) Adaylar içinde yetkili plaka var mı?
for cand in candidates: cand_plate = (cand.get("plate") or "").upper()
if cand_plate in authorized_set:
final_plate = cand_plate confidence = cand.get("confidence", confidence) status = "AUTHORIZED"
break
# 4) Hâlâ unauthorized ise, en iyi tahmini de kontrol et if status == "UNAUTHORIZED" and final_plate in authorized_set: status = "AUTHORIZED"
plate = final_plate or base_plate or ""
# Aynı plakayı 5 saniye içinde tekrar loglama + servo tetikleme
new_event = True
if plate and last_plate == plate and last_ts:
diff_sec = (now - last_ts).total_seconds()
if diff_sec < 5:
new_event = False
if new_event and plate:
last_plate = plate
last_ts = now
# Görüntüyü kaydet safe_ts = ts_str.replace(":", "-").replace(".", "-") image_filename = f"{safe_ts}_{plate}.jpg" image_path = f"{EVENT_IMAGES_DIR}/{image_filename}"
cv2.imwrite(image_path, frame)
# Event log
log_event(plate, confidence, status, CAMERA_ID, ts_str, image_path)
print( f"[{ts_str}] Camera={CAMERA_ID} Plate={plate} " f"Conf={confidence:.2f} Status={status}"
)
# Sadece YENİ bir AUTHORIZED event olduğunda servo çalışsın if status == "AUTHORIZED": print("[INFO] Servo: bariyer açılıyor")
open_barrier()
time.sleep(7.0) # 2 saniye açık kalsın (isteğe göre değiştir) print("[INFO] Servo: bariyer kapanıyor")
close_barrier()
# Overlay text & renk overlay_text = f"{plate} ({status}) {confidence:.1f}%" overlay_color = (0, 255, 0) if status == "AUTHORIZED" else (0, 0, 255)
# EKRANA GÖRÜNTÜ
cv2.putText(
frame,
overlay_text,
(20, 40),
cv2.FONT_HERSHEY_SIMPLEX,
1.0,
overlay_color,
2,
cv2.LINE_AA,
)
cv2.imshow("Plate Tracker", frame)
if cv2.waitKey(1) & 0xFF == ord('q'): print("[INFO] 'q' algılandı, çıkılıyor...")
break
except KeyboardInterrupt: print("\n[INFO] Kullanıcı tarafından durduruldu (Ctrl+C).")
finally:
cap.release()
cv2.destroyAllWindows()
servo_cleanup() print("[INFO] Sistem kapatıldı.")
if _name_ == "_main_": print("[DEBUG] _main_ bloğu çalıştı")
main()
