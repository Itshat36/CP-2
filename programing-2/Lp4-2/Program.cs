using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lp4_2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter weight: ");
            int weight = int.Parse(Console.ReadLine());
            Console.Write("Enter length: ");
            int length = int.Parse(Console.ReadLine());
            Console.Write("Enter width: ");
            int width = int.Parse(Console.ReadLine());
            Console.Write("Enter Height: ");
            int Height = int.Parse(Console.ReadLine());

            int volume = length * width * Height;

            if (weight > 27 && volume > 100000)
            {
                Console.WriteLine("Package is too heavy and too large");
            }
            else if (weight > 27)
            {
                Console.WriteLine("Package is too Large");
            }
            else
            {
                Console.WriteLine("Package is ok");
            }
            Console.ReadLine();

        }
    }
}
