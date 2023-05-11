using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FavClubConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter your Favoite club: ");
            string name = Console.ReadLine();
            Console.WriteLine("Your Favoite club is, " + name);
            Console.ReadLine();
        }
    }
}
