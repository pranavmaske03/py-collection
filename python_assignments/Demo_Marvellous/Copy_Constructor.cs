using System;

class CopyX
{
    public int num;
    public string str;
    public char ch;

    public int num1;
    public string str1;
    public char ch1;


    public CopyX(int no, string s, char ch)
    {
        this.num = no;
        this.str = s;
        this.ch = ch;
    }

    public CopyX(CopyX obj)
    {
        this.num1 = obj.num;
        this.str1 = obj.str;
        this.ch1 = obj.ch;
    }

    public void Display()
    {
        Console.WriteLine("INside Display...");
        Console.WriteLine(this.num1);
        Console.WriteLine(this.str1);
        Console.WriteLine(this.ch1);
    }
}

class Copy_Constructor
{
    public static void Main(String[] arg)
    {
        CopyX obj = new CopyX(11,"Pranav",'X');
        CopyX obj1 = new CopyX(obj);
        
        obj.Display();
        obj1.Display();
    }
}