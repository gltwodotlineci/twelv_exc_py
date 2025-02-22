# Test de la classe Rectangle
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    # Area method
    def calculate_area(self):
        return self.width * self.length

    # Perimeter method
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)


rectangle = Rectangle(5, 3) # 5:width & 3:length
print("Largeur:", rectangle.width)
print("Longueur:", rectangle.length)
print("Aire:", rectangle.calculate_area())
print("Périmètre:", rectangle.calculate_perimeter())
