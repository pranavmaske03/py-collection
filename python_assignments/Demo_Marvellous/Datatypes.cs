
public struct Demo
{
    public int data;
    public float f;
    public double d;
    public string s;
    public bool b;
}

class first
{
    public int num;

    public first(int no)
    {
        this.num = no;
    }

    public void Display()
    {
        System.Console.WriteLine(this.num);
    }
}

class datatypes
{
    public static void Main()
    {
        System.Console.WriteLine("Inside Main function...");

        int i = 11;
        float f = 11.11f;
        double d = 45.5432;
        string s = "pranav";

        System.Console.WriteLine(i);
        System.Console.WriteLine(f);
        System.Console.WriteLine(d);
        System.Console.WriteLine(s);

        Demo obj;

        obj.data = 11;
        obj.f = 22.222f;
        obj.d = 44.44444334;
        obj.s = "Maske";
        obj.b = false;

        System.Console.WriteLine("Data of the structure..."); 
        System.Console.WriteLine(obj.data);
        System.Console.WriteLine(obj.f);
        System.Console.WriteLine(obj.d);
        System.Console.WriteLine(obj.s);
        System.Console.WriteLine(obj.b);

        first obj1 = new first(7);
        obj1.Display();
    }
}