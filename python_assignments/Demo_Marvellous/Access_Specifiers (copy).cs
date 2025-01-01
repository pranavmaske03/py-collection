using System;

namespace Pranav
{

    class Demo
    {
        public int No;
        protected String str;
        private protected char ch;

        public Demo()
        {
            this.No = 11;
            this.str = "Pranav_Maske";
        }

        public void Fun()
        {
            Console.WriteLine("Inside Fun from Demo..");
        }
    }

    class Hello
    {
        protected int No;
        public String str;

        public Hello()
        {
            this.No = 22;
            this.str = "Hello..";
        }

        public void Gun()
        {
            Console.WriteLine("Inside Gun from Hello");
        }
    }

    class Bye : Hello
    {
        public void Fun()
        {
            Console.WriteLine(this.No);
            Console.WriteLine(this.str);
            Console.WriteLine("Indie Fun from Bye...");
        }
    }

    class Access
    {
        public static void Main()
        {
            Bye obj = new Bye();
            obj.Fun();
            obj.Gun();
        }
    }
}