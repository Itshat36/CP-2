using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lang54c
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter length: ");
            int num1 = int.Parse(Console.ReadLine());
            double num2 = 3.14159;
            int num3 = 2;
            double num4 = num2 * num3;
            double Radius = num1 / num4;

            Console.WriteLine("Radius: " + Radius);
            Console.ReadLine();
        }
    }
}