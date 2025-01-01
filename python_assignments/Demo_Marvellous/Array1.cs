using System;

class Array1
{
    public static void Main(string[] arg)
    {
        int[] Arr = new int[5]; 

        int[] Brr = {1,2,3,4,5}; // int[] array2 = [1, 2, 3, 4, 5, 6];

        string[] weekDays = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};

        Console.WriteLine(Arr.Length);
        Console.WriteLine(weekDays[0]);
        Console.WriteLine(weekDays[1]);
        Console.WriteLine(weekDays[2]);
        Console.WriteLine(weekDays[3]);
        Console.WriteLine(weekDays[4]);
        Console.WriteLine(weekDays[5]);
        Console.WriteLine(weekDays[6]);

        Console.WriteLine(Arr.Length);

        foreach(int iCnt in Brr)
        {
            Console.Write(iCnt+"\t");
        }
    }
}