using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HelloName
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter your first name: ");
            string name = Console.ReadLine();
            Console.WriteLine("Hello, " + name);

            Console.Write("Enter your Age: ");
            int age = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("hello" + age + "you are this many years old");

            Console.ReadKey();
        }
    }
}
