using System;

abstract class AbstractProperty
{   
    // abstract properties
    public abstract int Age{get;set;}
    public abstract string Str{get;set;}
}

class Normal : AbstractProperty
{
    private int age;
    private string str;

    public Normal()
    {
        this.age = 11;
        this.str = "pranav";
    }

    public override int Age
    {
        get
        {
            return this.age;
        }
        set
        {
            this.age = value;
        }
    }

    public override string Str
    {
        get
        {
            return this.str;
        }
        set
        {
            this.str = value;
        }
    }
}

class MainClass
{
    public static void Main()
    {
        Normal obj = new Normal();

        obj.Age = 40;
        obj.Str = "Marvellous";
        
        Console.WriteLine(obj.Age);
        Console.WriteLine(obj.Str);
    }
}