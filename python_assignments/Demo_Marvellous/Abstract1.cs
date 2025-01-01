using System;

abstract class RBI
{
    public abstract float CalculateROI();

    public void DisplayRules()
    {
        Console.WriteLine("You have to submit Aadhar card and PAN card");
        Console.WriteLine("Minimum balance is 10,000");
    }
}

class SBI : RBI
{
    public override float CalculateROI()
    {
        return 5.4f;    
    }
}

class BOM : RBI
{
    public override float CalculateROI()
    {
        return 7.7f;
    }
}

class MainClass
{
    public static void Main()
    {
        RBI robj = new SBI(); // upcasting
        RBI robj1 = new BOM(); // upcasting

        SBI sobj = new SBI();
        BOM bobj = new BOM();

        Console.WriteLine(sobj.CalculateROI());
        Console.WriteLine(bobj.CalculateROI());

        sobj.DisplayRules();
        bobj.DisplayRules();
    }
}