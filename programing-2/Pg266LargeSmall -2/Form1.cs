using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg266LargeSmall__2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int A = int.Parse(textBox1.Text);
            int b = int.Parse(textBox2.Text);

            if (A > b)
            {
                label2.Text = "Value A is greater than Value B";
            }
            else if (b > A)
            {
                label2.Text = "Value B is greater than Value A";
            }
            else
            {
                label2.Text = "they are the same number";
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            label2.Text = " ";
            textBox1.Text = " ";
            textBox2.Text = " ";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}