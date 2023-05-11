using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NameConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter your first name: ");
            string name = Console.ReadLine();
            Console.WriteLine("Hello, " + name);

            Console.Write("Enter your Last: ");
            int age = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("hello" + age + name);
        }
    }
}
