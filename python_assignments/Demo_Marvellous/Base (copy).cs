using System;

class Base
{
    public int Num;
    public string str;
    public int age;

    public int Age
    {
        get
        {
            return this.age;
        }
    }

    public Base()
    {
        Console.WriteLine("Inside base class constructor");
        this.Num = 21;
        this.str = "Marvellous";
        this.age = 20;
    }

    public void Fun()
    {
        Console.WriteLine("Inside Fun of base");
    }
}

class Derived : Base
{
    public int Num;
    public string str;
    public int age;

    public int Age
    {
        get
        {
            return this.age;
        }
    }

    public Derived() : base() 
    {
        Console.WriteLine("Inside derived class constructor");
        this.Num = 11;
        this.str = "Infosystems";
        this.age = 10;
    }

    public void Fun()
    {
        Console.WriteLine("Inside Fun of derived");
        base.Fun();
        Console.WriteLine(base.Num);    // base class field
        Console.WriteLine(this.Num);    // derived class field
        Console.WriteLine(base.str);    // base class field
        Console.WriteLine(this.str);    // derved class field
        Console.WriteLine(base.Age);    // base class property
        Console.WriteLine(this.Age);    // derived class property
    }
}

class MainClass
{
    static void Main()
    {   
        Derived obj = new Derived();
        obj.Fun();
    }
}