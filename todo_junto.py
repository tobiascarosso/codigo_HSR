import RPi.GPIO as GPIO
import time
import keyboard


A_TRIG_PIN = 8 
A_ECHO_PIN = 10 
D_TRIG_PIN = 12 
D_ECHO_PIN = 16 
I_TRIG_PIN = 18 
I_ECHO_PIN = 22

motor_di_marcha = 3
motor_di_cmarcha = 5
motor_dd_marcha = 7
motor_dd_cmarcha = 11
motor_ti_marcha = 13
motor_ti_cmarcha = 15
motor_td_marcha = 19
motor_td_cmarcha = 21
pin_nada = 23

GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)

pared_atras = False
pared_derecha = False
pared_izquierda = False



def setup():
    
    GPIO.setmode(GPIO.BOARD)  
    GPIO.setup(A_TRIG_PIN, GPIO.OUT)
    GPIO.setup(A_ECHO_PIN, GPIO.IN)
    GPIO.setup(D_TRIG_PIN, GPIO.OUT)
    GPIO.setup(D_ECHO_PIN, GPIO.IN)
    GPIO.setup(I_TRIG_PIN, GPIO.OUT)
    GPIO.setup(I_ECHO_PIN, GPIO.IN)
    GPIO.setup(motor_di_marcha, GPIO.OUT)
    GPIO.setup(motor_di_cmarcha, GPIO.OUT)
    GPIO.setup(motor_dd_marcha, GPIO.OUT)
    GPIO.setup(motor_dd_cmarcha, GPIO.OUT)
    GPIO.setup(motor_ti_marcha, GPIO.OUT)
    GPIO.setup(motor_ti_cmarcha, GPIO.OUT)
    GPIO.setup(motor_td_marcha, GPIO.OUT)
    GPIO.setup(motor_td_cmarcha, GPIO.OUT)
    GPIO.setup(pin_nada, GPIO.OUT)

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






def controlar_motores():
    
    tecla_w = keyboard.is_pressed('w')
    tecla_a = keyboard.is_pressed('a')
    tecla_s = keyboard.is_pressed('s')
    tecla_d = keyboard.is_pressed('d')
    tecla_q = keyboard.is_pressed('q')
    tecla_e = keyboard.is_pressed('e')
    tecla_z = keyboard.is_pressed('z')
    tecla_x = keyboard.is_pressed('x')
    tecla_1 = keyboard.is_pressed('1')
    tecla_3 = keyboard.is_pressed('3')
     
    if tecla_w :
        GPIO.output(motor_di_marcha, GPIO.HIGH)
        GPIO.output(motor_dd_marcha, GPIO.HIGH)
        GPIO.output(motor_ti_marcha, GPIO.HIGH)
        GPIO.output(motor_td_marcha, GPIO.HIGH)
        GPIO.output(motor_di_cmarcha, GPIO.LOW)
        GPIO.output(motor_dd_cmarcha, GPIO.LOW)
        GPIO.output(motor_ti_cmarcha, GPIO.LOW)
        GPIO.output(motor_td_cmarcha, GPIO.LOW)
        GPIO.output(pin_nada, GPIO.LOW)
        print("ADELANTE!")
    elif tecla_a and pared_izquierda == False:
        GPIO.output(motor_di_marcha, GPIO.HIGH)
        GPIO.output(motor_dd_marcha, GPIO.LOW)
        GPIO.output(motor_ti_marcha, GPIO.HIGH)
        GPIO.output(motor_td_marcha, GPIO.LOW)
        GPIO.output(motor_di_cmarcha, GPIO.LOW)
        GPIO.output(motor_dd_cmarcha, GPIO.HIGH)
        GPIO.output(motor_ti_cmarcha, GPIO.LOW)
        GPIO.output(motor_td_cmarcha, GPIO.HIGH)
        GPIO.output(pin_nada, GPIO.LOW)
        print("IZQUIERDA!")
    elif tecla_s and pared_atras == False:
        GPIO.output(motor_di_marcha, GPIO.LOW)
        GPIO.output(motor_dd_marcha, GPIO.LOW)
        GPIO.output(motor_ti_marcha, GPIO.LOW)
        GPIO.output(motor_td_marcha, GPIO.LOW)
        GPIO.output(motor_di_cmarcha, GPIO.HIGH)
        GPIO.output(motor_dd_cmarcha, GPIO.HIGH)
        GPIO.output(motor_ti_cmarcha, GPIO.HIGH)
        GPIO.output(motor_td_cmarcha, GPIO.HIGH)
        GPIO.output(pin_nada, GPIO.LOW)
        print("ATRAS!")
    elif tecla_d and pared_derecha == False:
        GPIO.output(motor_di_marcha, GPIO.LOW)
        GPIO.output(motor_dd_marcha, GPIO.HIGH)
        GPIO.output(motor_ti_marcha, GPIO.LOW)
        GPIO.output(motor_td_marcha, GPIO.HIGH)
        GPIO.output(motor_di_cmarcha, GPIO.HIGH)
        GPIO.output(motor_dd_cmarcha, GPIO.LOW)
        GPIO.output(motor_ti_cmarcha, GPIO.HIGH)
        GPIO.output(motor_td_cmarcha, GPIO.LOW)
        GPIO.output(pin_nada, GPIO.LOW)
        print("DERECHA!")
    elif tecla_q and pared_derecha == False:
        GPIO.output(motor_di_marcha, GPIO.LOW)
        GPIO.output(motor_dd_marcha, GPIO.HIGH)
        GPIO.output(motor_ti_marcha, GPIO.HIGH)
        GPIO.output(motor_td_marcha, GPIO.LOW)
        GPIO.output(motor_di_cmarcha, GPIO.LOW)
        GPIO.output(motor_dd_cmarcha, GPIO.LOW)
        GPIO.output(motor_ti_cmarcha, GPIO.LOW)
        GPIO.output(motor_td_cmarcha, GPIO.LOW)
        GPIO.output(pin_nada, GPIO.LOW)
        
    elif tecla_e and pared_izquierda == False:
        GPIO.output(motor_di_marcha, GPIO.HIGH)
        GPIO.output(motor_dd_marcha, GPIO.LOW)
        GPIO.output(motor_ti_marcha, GPIO.LOW)
        GPIO.output(motor_td_marcha, GPIO.HIGH)
        GPIO.output(motor_di_cmarcha, GPIO.LOW)
        GPIO.output(motor_dd_cmarcha, GPIO.LOW)
        GPIO.output(motor_ti_cmarcha, GPIO.LOW)
        GPIO.output(motor_td_cmarcha, GPIO.LOW)
        GPIO.output(pin_nada, GPIO.LOW)
        
    elif tecla_z and pared_izquierda == False and pared_atras == False:
        GPIO.output(motor_di_marcha, GPIO.LOW)
        GPIO.output(motor_dd_marcha, GPIO.LOW)
        GPIO.output(motor_ti_marcha, GPIO.LOW)
        GPIO.output(motor_td_marcha, GPIO.LOW)
        GPIO.output(motor_di_cmarcha, GPIO.HIGH)
        GPIO.output(motor_dd_cmarcha, GPIO.LOW)
        GPIO.output(motor_ti_cmarcha, GPIO.LOW)
        GPIO.output(motor_td_cmarcha, GPIO.HIGH)
        GPIO.output(pin_nada, GPIO.LOW)
        
    elif tecla_x and pared_derecha == False and pared_atras == False:
        GPIO.output(motor_di_marcha, GPIO.LOW)
        GPIO.output(motor_dd_marcha, GPIO.LOW)
        GPIO.output(motor_ti_marcha, GPIO.LOW)
        GPIO.output(motor_td_marcha, GPIO.LOW)
        GPIO.output(motor_di_cmarcha, GPIO.LOW)
        GPIO.output(motor_dd_cmarcha, GPIO.HIGH)
        GPIO.output(motor_ti_cmarcha, GPIO.HIGH)
        GPIO.output(motor_td_cmarcha, GPIO.LOW)
        GPIO.output(pin_nada, GPIO.LOW)
    
    elif tecla_1:#IZQUIERDA
        GPIO.output(motor_di_marcha, GPIO.LOW)
        GPIO.output(motor_dd_marcha, GPIO.HIGH)
        GPIO.output(motor_ti_marcha, GPIO.LOW)
        GPIO.output(motor_td_marcha, GPIO.HIGH)
        GPIO.output(motor_di_cmarcha, GPIO.HIGH)
        GPIO.output(motor_dd_cmarcha, GPIO.LOW)
        GPIO.output(motor_ti_cmarcha, GPIO.HIGH)
        GPIO.output(motor_td_cmarcha, GPIO.LOW)
        GPIO.output(pin_nada, GPIO.LOW)
        
    elif tecla_3:#DERECHA
        GPIO.output(motor_di_marcha, GPIO.HIGH)
        GPIO.output(motor_dd_marcha, GPIO.LOW)
        GPIO.output(motor_ti_marcha, GPIO.HIGH)
        GPIO.output(motor_td_marcha, GPIO.LOW)
        GPIO.output(motor_di_cmarcha, GPIO.LOW)
        GPIO.output(motor_dd_cmarcha, GPIO.HIGH)
        GPIO.output(motor_ti_cmarcha, GPIO.LOW)
        GPIO.output(motor_td_cmarcha, GPIO.HIGH)
        GPIO.output(pin_nada, GPIO.LOW)
    
    else:
       
        GPIO.output(motor_di_marcha, GPIO.LOW)
        GPIO.output(motor_di_cmarcha, GPIO.LOW)
        GPIO.output(motor_dd_marcha, GPIO.LOW)
        GPIO.output(motor_dd_cmarcha, GPIO.LOW)
        GPIO.output(motor_ti_marcha, GPIO.LOW)
        GPIO.output(motor_ti_cmarcha, GPIO.LOW)
        GPIO.output(motor_td_marcha, GPIO.LOW)
        GPIO.output(motor_td_cmarcha, GPIO.LOW)
        GPIO.output(pin_nada, GPIO.HIGH)

def loop():
    try:
        while True:
            distancia_atras = measure_distance(A_TRIG_PIN, A_ECHO_PIN)
            distancia_derecha = measure_distance(D_TRIG_PIN, D_ECHO_PIN)
            distancia_izquierda = measure_distance(I_TRIG_PIN, I_ECHO_PIN)
            if distancia_atras < 6:
                print("pared atras!")
                pared_atras = True
            else:
                print(f"Atrás: {distancia_atras:.2f} cm")
                pared_atras = False
            
            if distancia_derecha < 6:
                print("pared derecha!")
                pared_derecha = True
            else:
                print(f"Derecha: {distancia_derecha:.2f} cm")
                pared_derecha = False
            if distancia_izquierda < 6:
                print("pared izquierda!")
                pared_izquierda = True
            else:
                print(f"Izquierda: {distancia_izquierda:.2f} cm")
                pared_izquierda = False
            controlar_motores()
            time.sleep(0.1)  
            if keyboard.is_pressed('p'):
                break
            time.sleep(0.25) 
    except KeyboardInterrupt:
        print("Measurement stopped by User")
    finally:
        GPIO.cleanup() 
        print('\nTerminado!')

if __name__ == '__main__':
    setup()
    loop()