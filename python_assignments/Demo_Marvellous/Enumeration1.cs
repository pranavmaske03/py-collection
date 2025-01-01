using System;

enum days
{
    Monday,
    Tuesday,
    Wedenesday,
    Thirsday,
    Friday,
    Saturday,
    Sunday
}

class Enumeration1
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Demonstration of Enumeration");

        Console.WriteLine(days.Monday+" with the value : "+ (int)days.Monday);
        Console.WriteLine(days.Tuesday+" with the value : "+ (int)days.Tuesday);
        Console.WriteLine(days.Wedenesday+" with the value : "+ (int)days.Wedenesday);
        Console.WriteLine(days.Thirsday+" with the value : "+ (int)days.Thirsday);
        Console.WriteLine(days.Friday+" with the value : "+ (int)days.Friday);
        Console.WriteLine(days.Saturday+" with the value : "+ (int)days.Saturday);
        Console.WriteLine(days.Sunday+" with the value : "+ (int)days.Sunday);

    }
}