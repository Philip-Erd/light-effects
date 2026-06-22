import tkinter as tk

from lighteffect import Effect, ColorRamp


#define your effect here
EFFECT="effects/neon_light.json"
RAMP="color_ramps/white.json"
FPS=30


def rgb_to_hex(c):
    r = int(c[0] * 255)
    g = int(c[1] * 255)
    b = int(c[2] * 255)
    return f"#{r:02x}{g:02x}{b:02x}"

# load effect and color ramp
effect = Effect.from_file(EFFECT)
ramp = ColorRamp.from_file(RAMP)


root = tk.Tk()
root.title("Effect Preview")

canvas = tk.Canvas(root, width=200, height=200, bg="black")
canvas.pack()

button_on = tk.Button(root, text="on", command=effect.on)
button_on.pack()

button_off = tk.Button(root, text="off", command=effect.off)
button_off.pack()

circle = canvas.create_oval(50, 50, 150, 150, fill="black", outline="")


delay = int(1000 / FPS)

def update():
    
    effect.update(1)
    t = effect.get_value()
    color = ramp.getColor(t)
    
    canvas.itemconfig(circle, fill=rgb_to_hex(color))
    
    root.after(delay, update)

update()
root.mainloop()