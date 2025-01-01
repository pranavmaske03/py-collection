using System;

class Perimeter
{
    public enum Shapes
    {
        Circle,
        Square
    }

    public void Calculation(int value, Shapes sval)
    {
        if(sval == 0)
        {
            Console.WriteLine("Perimeter of the circle is : "+2 * 3.14 * value);
        }
        else
        {
            Console.WriteLine("Perimeter of the Square is : "+4 * value);
        }
    }
}

class Enumeration2
{
    public static void Main(string[] args)
    {
        int value = 11;
        Perimeter obj = new Perimeter();

        obj.Calculation(value,Perimeter.Shapes.Circle);
        obj.Calculation(value,Perimeter.Shapes.Square);
    }
}