using System;
using demo;

namespace demo
{
    class DefaultX
    {
        public int num;
        public string str;
        public char ch;

        public DefaultX()
        {
            this.num = 7;
            this.str = "Jay Ganesh...";
            this.ch = 'F';
        }

        public void Display()
        {
            Console.WriteLine("INside Display...");
        }
    }
}

class Default_Constructor
{
    public static void Main()
    {
        DefaultX obj = new DefaultX();

        Console.WriteLine(obj.num);
        Console.WriteLine(obj.str);
        Console.WriteLine(obj.ch);
    }
}
