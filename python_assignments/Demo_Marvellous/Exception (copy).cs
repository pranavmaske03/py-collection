using System;

class MainClass
{
    static void Main()
    {
        int No1 = 0;
        int No2 = 0;
        int Ans = 0;

        Console.WriteLine("Enter first number :");
        No1  = int.Parse(Console.ReadLine());

        Console.WriteLine("Enter second number :");
        No2 = int.Parse(Console.ReadLine());

        try
        {
            Ans = No1 / No2;            
        }
        catch(DivideByZeroException dobj)
        {
            Console.WriteLine("Exception Occured : "+dobj);
        }
        finally
        {
            Console.WriteLine("Division is : "+Ans);
        }
    }
}