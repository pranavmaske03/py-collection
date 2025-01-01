using System;


class Error
{
    public int age;

    public Error(int no)
    {
        this.age = no;
    }

    public void CheckAge()
    {
        if(this.age < 0)
        {
            throw new ArgumentOutOfRangeException("Age can not be negative");
        }
    }
}

class MainClass
{
    static void Main()
    {
        int value = 0;

        Console.WriteLine("Enter your age :");
        value = int.Parse(Console.ReadLine());

        try
        {
            Error obj = new Error(value);
            obj.CheckAge();
        }
        catch(Exception eobj)
        {
            Console.WriteLine(eobj);
        }
    }
}