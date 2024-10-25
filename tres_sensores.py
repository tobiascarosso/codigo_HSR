import RPi.GPIO as GPIO
import time


A_TRIG_PIN = 8 
A_ECHO_PIN = 10 
D_TRIG_PIN = 11 
D_ECHO_PIN = 12 
I_TRIG_PIN = 13 
I_ECHO_PIN = 16 


GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)


GPIO.setup(A_TRIG_PIN, GPIO.OUT)
GPIO.setup(A_ECHO_PIN, GPIO.IN)
GPIO.setup(D_TRIG_PIN, GPIO.OUT)
GPIO.setup(D_ECHO_PIN, GPIO.IN)
GPIO.setup(I_TRIG_PIN, GPIO.OUT)
GPIO.setup(I_ECHO_PIN, GPIO.IN)


def measure_distance(trigger_pin, echo_pin):

    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.005)


    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.00001)  
    GPIO.output(trigger_pin, GPIO.LOW)


    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()
    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()


    pulse_duration = pulse_end - pulse_start
    distance = (pulse_duration * 34300) / 2  
    return distance

while True:

    distancia_atras = measure_distance(A_TRIG_PIN, A_ECHO_PIN)
    distancia_derecha = measure_distance(D_TRIG_PIN, D_ECHO_PIN)
    distancia_izquierda = measure_distance(I_TRIG_PIN, I_ECHO_PIN)

 
    print(f"Atrás: {distancia_atras:.2f} cm")
    print(f"Derecha: {distancia_derecha:.2f} cm")
    print(f"Izquierda: {distancia_izquierda:.2f} cm")

    time.sleep(0.5)
