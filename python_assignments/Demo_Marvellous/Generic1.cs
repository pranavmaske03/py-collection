using System;

class Generic<T>
{
    public T value;

    public Generic(T no)
    {
        this.value = no;
    }

    public void Display()
    {
        Console.WriteLine(value);
    }
}

class MainClass
{
    static void Main()
    {
        Generic<int> obj = new Generic<int>(11);
        Generic<float> obj1 = new Generic<float>(11.11f);
        Generic<char> obj2 = new Generic<char>('P');


        obj.Display();
        obj1.Display();
        obj2.Display();
    }
}