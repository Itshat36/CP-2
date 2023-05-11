using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lang85c
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

            int S = A - 165;
            double b = S / 100;
            int R = S % 100;

            lblBirthday.Text = b.ToString();
            B.Text = ("/");
            C.Text = R.ToString();
        }

    }
}
