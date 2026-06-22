# light-effects
A pure Python library for lighting effects. It is specificaly created for micropython to controll LEDs or DMX lights but can be used on other platforms.

## usage

Simply copy the `lighteffect.py` file in to your project and import it. Check out the examples for micropython and desktop (using tkinter).


## How it works

An Effect is defined as a sequence of values from 0 to 1 with loop points. When updating, it advances to the next value/frame in the sequence. Initially, when the Effect is of the last value in the sequence is put out. when the Effect is turned on, it starts at the first frame and goes to the sequence. Once it reaches the loop_end frame it checks if the Effect is still on. If it is still on, it jumps to loop_start. Otherwise it will continue to the last frame and output its value until the Effect is turned on again.

This single value can be used to control a dimmer directly but often a RGB value is wanted. in this case value can be fed in to a ColorRamp, which maps it to RGB. The ColorRamp has a list of equally spaced colors along the 0 to 1 range. It finds the closest two and linear interpolates between them. The colors are defined as RGB tuples with values between 0 and 1.

There ar a couple of functions to convert the RGB tuple to a more suitable format (RGBW, RGB in the range between 0 and 255).

Effects and ColorRamps can be loaded from  json files.

To make it a bit easier to create effects there is a simple editor that can be opened in a web browser.

A typical update loop look like this:

read input -> turn Effect on or off -> update Effect -> get color from ColorRamp based on Effect value -> convert color tuple to suitable format -> write color to output -> wait for next frame