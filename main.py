import machine
import dht
import time

# Nastavení GPIO pinů
dht_pin = machine.Pin(0)
led_pin = machine.Pin(1)

# Inicializace DHT11 senzoru
dht_sensor = dht.DHT11(dht_pin)

# Inicializace PWM pro LED
led_pwm = machine.PWM(led_pin)
led_pwm.freq(1000)  # 1 kHz frekvence

def map_value(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while True:
    try:
        # Čtení hodnoty teploty z DHT11
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        
        # Mapování hodnoty teploty na rozsah PWM (0-65535)
        duty_cycle = map_value(temperature, 0, 40, 0, 65535)  # předpokládáme teplotní rozsah 0-40°C
        
        # Nastavení PWM pro LED podle teploty
        led_pwm.duty_u16(duty_cycle)
        
        print(f'Teplota: {temperature}°C | PWM: {duty_cycle}')
        
    except OSError as e:
        print('Chyba při čtení z DHT11:', e)
    
    time.sleep(2)
