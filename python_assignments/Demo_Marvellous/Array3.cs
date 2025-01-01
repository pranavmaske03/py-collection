using System;
/*
namespace UnsafeCodeApplication 
{
   class TestPointer 
   {
      public unsafe static void Main() 
      {
         int[] list = {5, 25, 56, 43, 98, 56};
         fixed(int *ptr = list)

         for (int i = 0; i < list.Length; i++) 
         {
           // Console.WriteLine("Address of list[{0}]={1}",i,(int)(ptr + i));
            //Console.WriteLine("Value of list[{0}]={1}", i, *(ptr + i));

            Console.WriteLine(*(ptr + i));

         }
      }
   }
}
*/

unsafe class ArrayX
{
    public int[] Arr;
    public int Length;

    public ArrayX(int size)
    {
        this.Length = size;
        this.Arr = new int[Length];
    }
    
    public void Accept()
    {
        Console.WriteLine("Enter the elements of the array : -");

        for(int iCnt = 0; iCnt < Arr.Length; iCnt++)
        {
            this.Arr[iCnt] = int.Parse(Console.ReadLine());
        }
    }

    public void Display()
    {
        Console.WriteLine("Elements of the array are : ");

        for(int iCnt = 0; iCnt < Arr.Length; iCnt++)
        {
            Console.Write(Arr[iCnt]+"\t");
        }
        Console.WriteLine();
    }

    public void AcessData()
    {
        Console.WriteLine("Display elements using pointer : ");
        fixed(int* ptr = this.Arr)
        {
            for(int i = 0; i < Length; i++)
            {
                Console.Write(*(ptr+i)+"\t");
            }
            Console.WriteLine();
        }
    }
}

class Array3
{
    public static void Main(string[] args)
    {
        int size = 5;
        
        ArrayX obj = new ArrayX(size);
        obj.Accept();
        obj.Display();
        obj.AcessData();
    }
}