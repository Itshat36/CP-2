using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace strinterview18
{
    class Program
    {
        static void Main(string[] args)
        {
            string s1 = "Prince";
            string s2 = "princess";

            string s3 = s1.Remove(3);
            string s4 = s2.Remove(1);

            System.Console.WriteLine(s1);
            System.Console.WriteLine(s2);
            System.Console.WriteLine(s3);
            System.Console.WriteLine(s4);
            System.Console.ReadLine();
        }
    }
}
