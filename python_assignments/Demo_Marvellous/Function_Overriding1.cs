using System;

class Base
{
    public virtual void Fun()
    {
        Console.WriteLine("Inside Fun of Base");
    }

    public virtual void Gun()
    {
        Console.WriteLine("Inside Gun of Base");
    }
    public virtual void Sun()
    {
        Console.WriteLine("Inside Sun of Base");
    }
    public void Run()
    {
        Console.WriteLine("Inside Run of Base");
    }
}
class Derived : Base
{
    public override void Fun()
    {
        Console.WriteLine("Inside Fun of Derived");
        base.Fun();
    }
    public override void Gun()
    {
        Console.WriteLine("Inside Gun of Derived");
    }
    public override void Sun()
    {
        Console.WriteLine("Inside Sun of Derived");
    }
}

class MainClass
{
    static void Main(string[] args)
    {
        Base obj = new Derived();
        obj.Fun();
        obj.Gun();
        obj.Sun();
        obj.Run();
    }
}