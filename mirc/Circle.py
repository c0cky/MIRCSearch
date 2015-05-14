import math
class Circle:

    def add_entry(self, entry):
        self.entries.append(entry)
        self.current_entries = self.current_entries + 1

    def remove_entry(self):
        self.entries.pop()
        self.current_entries= self.current_entries - 1

    def is_full(self):
        if self.MAX == self.current_entries:
            return True
        else:
            return False

    def compute(self):
        if self.MAX == 1:
            self.entries[0]['x_axis'] = self.xcenter - self.xcenter/20
            self.entries[0]['y_axis'] = self.ycenter - self.ycenter/20
            self.entries[0]['root'] = True
        else:
            step = 360/self.MAX
            angle = 0
            for i in range (0,self.current_entries):
                self.entries[i]['x_axis'] = self.xcenter + (self.xradius * math.cos(math.radians(angle)))
                self.entries[i]['y_axis'] = self.ycenter + (self.yradius * math.sin(math.radians(angle)))
                self.entries[i]['root'] = False
                angle += step



    def to_list(self):
        return self.entries

    def __init__(self, maximum, xr, yr, xc, yc):
        self.entries = []
        self.current_entries = 0
        self.MAX = maximum
        self.xradius = xr
	self.yradius = yr
	self.xcenter = xc
        self.ycenter = yc


