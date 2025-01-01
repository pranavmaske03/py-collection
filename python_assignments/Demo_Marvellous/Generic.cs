using System;

class MainClass
{
    static void Display<T>(T[] Arr)
    {

        foreach(T iCnt in Arr)
        {
            Console.Write(iCnt+"\t");
        }
        Console.WriteLine();
    }

    static void Main()
    {
        int[] A = {1,2,3,4,5};
        float[] B = {1.1f,2.2f,3.3f,4.4f,5.5f};
        char[] C = {'P','R','A','N','A','V'};

        Display(A);
        Display(B);
        Display(C);
    }
}