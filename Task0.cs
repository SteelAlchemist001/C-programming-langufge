using System;
 
namespace kvadrat
{
    class Program
    {
        static void Main()
        {
            Console.Write("Ведите число: ");
            double a = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("{0} в квадрате {1}", a, Math.Pow(a, 2));
            Console.ReadLine();
        }
    }
}
