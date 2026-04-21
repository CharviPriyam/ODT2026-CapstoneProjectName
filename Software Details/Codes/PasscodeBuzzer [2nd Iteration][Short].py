from machine import Pin, PWM
import time

#Initialisation using lists
button=[13,12,14,27,26,4,5,18,19,21]
buttons=[Pin(p, Pin.IN, Pin.PULL_UP) for p in button]
b=PWM(Pin(23, Pin.OUT))

#Defined function
def PushButton(index, start_freq):
    if buttons[index].value()==0:
        b.duty(512)
        for freq in range(start_freq, start_freq + 100):
            b.freq(freq)
            time.sleep(0.001)
        print(index + 1)
        return True # Signal that a button was pressed
    return False

#Main Loop
while True:
    any_pressed = False
    
    for i in range(len(buttons)):
        # Each button starts 100Hz higher: 800, 900, 1000...
        freq_start = 800 + (i * 100)
        if PushButton(i, freq_start):
            any_pressed = True
            
    # If no buttons are held down, turn off the buzzer
    if not any_pressed:
        b.duty(0)
