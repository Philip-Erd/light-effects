import neopixel
import time
from machine import Pin
from lighteffect import Effect, ColorRamp, rgb_to_int


# output to neopixel
p = Pin(4)
n = neopixel.NeoPixel(p, 1)


# turn effect on by holding a button    
button = Pin(5, Pin.IN, Pin.PULL_UP)
button_value = False


# effect and color ramp are defined in json files
# dont forgeet to copy them to your device
candle_effect = Effect.from_file("candle_effect.json")
candle_ramp = ColorRamp.from_file("candle_ramp.json")


while True:
    
    # read button an turn effect on or off
    if button.value() == 0 and not button_value:
        #on
        candle_effect.on()
        button_value = True
    elif button.value() == 1 and button_value:
        #off
        candle_effect.off()
        button_value = False

    # update effect by one frame
    candle_effect.update(1)

    # read color from effect and write it to the neopixel    
    color = candle_ramp.getColor(candle_effect.get_value())
    n[0] = rgb_to_int(color)
    n.write()

    time.sleep(0.1)
    