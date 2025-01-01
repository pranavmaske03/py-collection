using System;

enum Demo
{
    pranav = 41374,
    sagar = 41372,
    harsh = 41371,
    pratham = 41370
}

class Enumeration3
{
    public static void Main(string[] args)
    {
        Console.WriteLine((int)Demo.pranav);
        Console.WriteLine((int)Demo.sagar);
        Console.WriteLine((int)Demo.harsh);
        Console.WriteLine((int)Demo.pratham);
    }
}