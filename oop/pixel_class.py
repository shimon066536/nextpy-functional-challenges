class Pixel:
    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue) // 3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        colors = [self._red, self._green, self._blue]
        color_names = ["red", "green", "blue"]
        dominant = ""
        for i in range(3):
            if colors[i-1] == 0 and colors[(i+1)%3] == 0 and colors[i] > 50:
                dominant = color_names[i]
        print(f"X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue})", dominant)

p = Pixel(5, 57, 67)
p.print_pixel_info()
p.set_grayscale()
p.print_pixel_info()
