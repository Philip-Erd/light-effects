import json

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    
    r = int(hex_color[0:2], 16) / 255
    g = int(hex_color[2:4], 16) / 255
    b = int(hex_color[4:6], 16) / 255
    
    return (r, g, b)

def rgb_to_rgbw(rgb):
    r, g, b = rgb
    
    w = min(r, g, b)
    
    r -= w
    g -= w
    b -= w
    
    return (r, g, b, w)

    
def rgb_to_int(color):
        return (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))
def rgbw_to_int(color):
        return (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255), int(color[3] * 255))

class ColorRamp:
    
    def from_file(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
        colors = [tuple(c) for c in data["colors"]]
        return ColorRamp(colors) 
    
    def __init__(self, colors):
        self.colors = colors
        
        
    def getColor(self, t):
        if t <= 0:
            return self.colors[0]
        if t >= 1:
            return self.colors[-1]
        
        pos = t * (len(self.colors) - 1)
        i = int(pos)
        f = pos - i
        
        c1 = self.colors[i]
        c2 = self.colors[i + 1]
        
        r = c1[0] + (c2[0] - c1[0]) * f
        g = c1[1] + (c2[1] - c1[1]) * f
        b = c1[2] + (c2[2] - c1[2]) * f
        
        return (r, g, b)
        
    
    
class Effect:
    
    def from_file(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
        return Effect(
            data["values"],
            data["loop_start"],
            data["loop_end"])
    
    def __init__(self, values, loop_start, loop_end):
        self.values = values
        self.loop_start = loop_start
        self.loop_end = loop_end
        
        self.is_on = False
        self.value = values[0]
        
        self.frame = len(self.values)-1
        
    def increase_frame(self):
        self.frame = self.frame + 1
        
        #loop
        if self.frame == self.loop_end and self.is_on:
            self.frame = self.loop_start
           
        #end   
        if self.frame >= len(self.values):
            self.frame = len(self.values)-1
        
        
    def update(self, delta_frames):
        for _ in range(delta_frames):
            self.increase_frame()
            
    def on(self):
        self.is_on = True
        self.frame = 0
        
    def off(self):
        self.is_on = False
        
    def get_value(self):
        return self.values[self.frame]
        
        
    