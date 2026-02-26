# Raspberry Pi 4 + GPIO18 (BCM) üzerinde RPi.GPIO ile SERVO KONTROLÜ
# Titremeyi azaltmak için: sadece hareket ederken PWM veriyoruz, sonra duty=0.

import RPi.GPIO as GPIO
import time

# --- PIN AYARI ---

SERVO_PIN = 18  # BCM 18 -> fiziksel pin 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

# 50 Hz PWM (standart servo frekansı)
_pwm = GPIO.PWM(SERVO_PIN, 50)
_pwm.start(0)

# --- AÇI / DUTY AYARI ---

# DİKKAT: Burada yönü ters çeviriyoruz
# Artık:
#   CLOSE_ANGLE = "kapı kapalı" açısı
#   OPEN_ANGLE  = "kapı açık" açısı
#
# Öncesinde 0° kapalı, 90° açık gibi düşünmüştük.
# Senin mekanikte tam tersi çıktığı için burayı tersine çevirdik.

CLOSE_ANGLE = 90   # bariyer KAPALI
OPEN_ANGLE  = 0    # bariyer AÇIK


def _angle_to_duty(angle: float) -> float:
    """
    0–180 dereceyi yaklaşık 2.5–12.5 duty aralığına map eder.
    Gerekirse küçük oynamalar yapabiliriz.
    """
    angle = max(0, min(180, angle))
    return 2.5 + (angle / 18.0)  # 0° -> 2.5, 90° -> 7.5, 180° -> 12.5


def _set_angle(angle: float, wait: float = 0.4):
    """
    Verilen açıya gitmesi için servoya kısa süre PWM ver,
    sonra duty'yi 0 yaparak sinyali kes (jitter azalır).
    """
    duty = _angle_to_duty(angle)
    print(f"[SERVO] angle={angle} duty={duty:.2f}")
    _pwm.ChangeDutyCycle(duty)
    time.sleep(wait)          # servo bu sürede hedefe gider
    _pwm.ChangeDutyCycle(0)   # sinyali kes -> titreme büyük ölçüde biter


def open_barrier():
    """
    Bariyeri AÇ (OPEN_ANGLE).
    (Artık OPEN_ANGLE = 0°, yani daha önceki kapalı açın.)
    """
    print("[SERVO] open_barrier()")
    _set_angle(OPEN_ANGLE)


def close_barrier():
    """
    Bariyeri KAPAT (CLOSE_ANGLE).
    (Artık CLOSE_ANGLE = 90°, yani mekanikte kapalıya denk gelen açı.)
    """
    print("[SERVO] close_barrier()")
    _set_angle(CLOSE_ANGLE)


def cleanup():
    """
    Program biterken PWM ve GPIO temizliği.
    """
    print("[SERVO] cleanup()")
    _pwm.ChangeDutyCycle(0)
    time.sleep(0.2)
    _pwm.stop()
    GPIO.cleanup()


if _name_ == "_main_":
    print("[DEBUG] _main_ bloğu çalıştı")
    main()
