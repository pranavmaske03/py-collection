using System;

class Array2
{
    public static void Display(int[] Arr)
    {
        Console.WriteLine("Elements of the array are : ");

        int iCnt = 0;
        for(iCnt = 0; iCnt < Arr.Length; iCnt++)
        {
            Console.Write(Arr[iCnt]+"\t");
        }
        Console.WriteLine();

        Console.WriteLine("Array using foreach loop");
        foreach(int i in Arr)
        {
            Console.Write(i+"\t");
        }
        Console.WriteLine();
    }

    public static void Accept(int size)
    {
        int[] Arr = new int[size];
        int iCnt = 0;

        Console.WriteLine("Enter elements of the array");
        for(iCnt = 0; iCnt < Arr.Length; iCnt++)
        {
            Arr[iCnt] = Convert.ToInt32(Console.ReadLine());
        }

        Display(Arr);
    }

    public static void Main(string[] arg)
    {
        Console.WriteLine("Enter the number of elements");
        int size = Convert.ToInt32(Console.ReadLine());

        Accept(size);
    }
}