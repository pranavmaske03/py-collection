using System;

class Constants
{
    public const int No = 11;
    public const string Name = "Pranav";

    public static void Display()
    {
        const int Num = 21;

        Console.WriteLine(Num);
        Console.WriteLine(No);
        Console.WriteLine(Name);
    }
}

class MainClass
{
    static void Main()
    {
        Constants obj = new Constants();
        Constants.Display();
    }
}