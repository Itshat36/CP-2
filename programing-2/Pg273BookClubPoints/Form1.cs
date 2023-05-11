using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg273BookClubPoints
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            X.Text = "15";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            X.Text = "0";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            X.Text = "5";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            X.Text = "30";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            X.Text = "60";
        }
    }
}
