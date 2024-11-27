import machine
import dht
import time

meric = machine.Pin(27)
led1 = machine.Pin(1,machine.Pin.OUT)
led2 = machine.Pin(2,machine.Pin.OUT)
led3 = machine.Pin(3,machine.Pin.OUT)
led4 = machine.Pin(4,machine.Pin.OUT)

buttton = machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_UP)

sensor = dht.DHT11(meric)

led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)

mereni = 1


while True:
    if buttton.value() == 0:
        if mereni == 1:
            mereni = 2
        else:
            mereni = 1
    
    sensor.measure() 
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    

    if mereni == 1:
            if temp < 20:
                led1.value(1)
                print('Temperature: %3.1f C' %temp)
                print('Temperature: %3.1f F' %temp_f)
                time.sleep(time.sleep(0.5))
                led1.value(0)
            elif temp < 25:
                led2.value(1)
                print('Temperature: %3.1f C' %temp)
                print('Temperature: %3.1f F' %temp_f)
                time.sleep(0.5)
                led2.value(0)
            elif temp < 27:
                led3.value(1)
                print('Temperature: %3.1f C' %temp)
                print('Temperature: %3.1f F' %temp_f)
                time.sleep(0.5)
                led3.value(0)
            elif temp < 30:
                led4.value(1)
                print('Temperature: %3.1f C' %temp)
                print('Temperature: %3.1f F' %temp_f)
                time.sleep(0.5)
                led4.value(0)


    if mereni == 2:
            if hum < 25:
                led1.value(1)
                print('Humidity: %3.1f %%' %hum)
                time.sleep(0.5)
                led1.value(0)
            elif hum < 50:
                led2.value(1)
                print('Humidity: %3.1f %%' %hum)
                time.sleep(0.5)
                led2.value(0)
            elif hum < 75:
                led3.value(1)
                print('Humidity: %3.1f %%' %hum)
                time.sleep(0.5)
                led3.value(0)
            elif hum < 100:
                led4.value(1)
                print('Humidity: %3.1f %%' %hum)
                time.sleep(0.5)
                led4.value(0)

        


































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
