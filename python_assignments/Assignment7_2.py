
class Circle:
    PI = 3.14

    def __init__(self):
        area = 0.0
        radius = 0.0
        circumference = 0.0
    
    def Accept(self):
        print("Enter radius :")
        self.radius = int(input())

    def CalculateArea(self):
        self.area = Circle.PI * self.radius * self.radius

    def CalculateCircumference(self):   
        self.circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print("Radius of the circle is : ",self.radius)
        print("Area of the circle is : ",self.area)
        print("Circumference of the circle is : ",self.circumference)

def main():

    obj = Circle()

    obj.Accept()
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.Display()

if __name__ == "__main__":
    main()