﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Prog88a
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

        private void button1_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            int num2 = int.Parse(textBox2.Text);

            int sum = num1 + num2;
            int diff = num1 - num2;
            int product = num1 * num2;
            double average = (double)sum / 2.0;
            int abs = Math.Abs(diff);
            int max = 0;
            int min = 0;

            if (num1 > num2)
            {
                max = num1;
            }
            else
            {
                max = num2;
            }

            if (num1 <= num2)
                min = num1;
            else min = num2;

            lblSum.Text = sum.ToString();
            lblMax.Text = max.ToString();
            LblMin.Text = min.ToString();
            lblDiff.Text = diff.ToString();
            lblave.Text = average.ToString();
            lblAbe.Text = abs.ToString();
            LblProd.Text = product.ToString();

        }

        private void button3_Click(object sender, EventArgs e)
        {
            lblSum.Text = "";
            lblMax.Text = "";
            LblMin.Text = "";
            lblDiff.Text = "";
            lblave.Text = "";
            lblAbe.Text = "";
            LblProd.Text = "";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
