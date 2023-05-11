namespace Prog88a
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.lblSum = new System.Windows.Forms.Label();
            this.lblDiff = new System.Windows.Forms.Label();
            this.LblProd = new System.Windows.Forms.Label();
            this.lblave = new System.Windows.Forms.Label();
            this.lblAbe = new System.Windows.Forms.Label();
            this.lblMax = new System.Windows.Forms.Label();
            this.LblMin = new System.Windows.Forms.Label();
            this.label15 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(103, 157);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(181, 23);
            this.button1.TabIndex = 0;
            this.button1.Text = "Calculate";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(209, 102);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 1;
            this.button2.Text = "Exit";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(209, 131);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(75, 23);
            this.button3.TabIndex = 2;
            this.button3.Text = "Clear";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.button3_Click);
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(103, 104);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(100, 20);
            this.textBox1.TabIndex = 3;
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(103, 131);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(100, 20);
            this.textBox2.TabIndex = 4;
            // 
            // label1
            // 
            this.label1.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.label1.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.label1.Location = new System.Drawing.Point(100, 207);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(100, 23);
            this.label1.TabIndex = 5;
            this.label1.Text = "Sum";
            // 
            // label2
            // 
            this.label2.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.label2.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.label2.Location = new System.Drawing.Point(100, 230);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(100, 23);
            this.label2.TabIndex = 6;
            this.label2.Text = "Differnence";
            // 
            // label3
            // 
            this.label3.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.label3.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.label3.Location = new System.Drawing.Point(100, 253);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(100, 23);
            this.label3.TabIndex = 7;
            this.label3.Text = "product";
            // 
            // label4
            // 
            this.label4.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.label4.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.label4.Location = new System.Drawing.Point(100, 276);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(100, 23);
            this.label4.TabIndex = 10;
            this.label4.Text = "Average";
            // 
            // label5
            // 
            this.label5.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.label5.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.label5.Location = new System.Drawing.Point(100, 299);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(100, 23);
            this.label5.TabIndex = 9;
            this.label5.Text = "Abs. Value";
            // 
            // label6
            // 
            this.label6.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.label6.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.label6.Location = new System.Drawing.Point(100, 345);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(100, 23);
            this.label6.TabIndex = 8;
            this.label6.Text = "Minimum";
            // 
            // label7
            // 
            this.label7.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.label7.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.label7.Location = new System.Drawing.Point(100, 322);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(100, 23);
            this.label7.TabIndex = 13;
            this.label7.Text = "Maximum";
            // 
            // lblSum
            // 
            this.lblSum.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.lblSum.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.lblSum.Location = new System.Drawing.Point(284, 207);
            this.lblSum.Name = "lblSum";
            this.lblSum.Size = new System.Drawing.Size(100, 23);
            this.lblSum.TabIndex = 12;
            // 
            // lblDiff
            // 
            this.lblDiff.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.lblDiff.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.lblDiff.Location = new System.Drawing.Point(284, 230);
            this.lblDiff.Name = "lblDiff";
            this.lblDiff.Size = new System.Drawing.Size(100, 23);
            this.lblDiff.TabIndex = 11;
            // 
            // LblProd
            // 
            this.LblProd.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.LblProd.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.LblProd.Location = new System.Drawing.Point(284, 253);
            this.LblProd.Name = "LblProd";
            this.LblProd.Size = new System.Drawing.Size(100, 23);
            this.LblProd.TabIndex = 16;
            // 
            // lblave
            // 
            this.lblave.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.lblave.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.lblave.Location = new System.Drawing.Point(284, 276);
            this.lblave.Name = "lblave";
            this.lblave.Size = new System.Drawing.Size(100, 23);
            this.lblave.TabIndex = 15;
            // 
            // lblAbe
            // 
            this.lblAbe.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.lblAbe.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.lblAbe.Location = new System.Drawing.Point(284, 299);
            this.lblAbe.Name = "lblAbe";
            this.lblAbe.Size = new System.Drawing.Size(100, 23);
            this.lblAbe.TabIndex = 14;
            // 
            // lblMax
            // 
            this.lblMax.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.lblMax.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.lblMax.Location = new System.Drawing.Point(284, 322);
            this.lblMax.Name = "lblMax";
            this.lblMax.Size = new System.Drawing.Size(100, 23);
            this.lblMax.TabIndex = 19;
            // 
            // LblMin
            // 
            this.LblMin.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.LblMin.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.LblMin.Location = new System.Drawing.Point(284, 345);
            this.LblMin.Name = "LblMin";
            this.LblMin.Size = new System.Drawing.Size(100, 23);
            this.LblMin.TabIndex = 18;
            // 
            // label15
            // 
            this.label15.Location = new System.Drawing.Point(517, 83);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(100, 23);
            this.label15.TabIndex = 17;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(647, 423);
            this.Controls.Add(this.lblMax);
            this.Controls.Add(this.LblMin);
            this.Controls.Add(this.label15);
            this.Controls.Add(this.LblProd);
            this.Controls.Add(this.lblave);
            this.Controls.Add(this.lblAbe);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.lblSum);
            this.Controls.Add(this.lblDiff);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label lblSum;
        private System.Windows.Forms.Label lblDiff;
        private System.Windows.Forms.Label LblProd;
        private System.Windows.Forms.Label lblave;
        private System.Windows.Forms.Label lblAbe;
        private System.Windows.Forms.Label lblMax;
        private System.Windows.Forms.Label LblMin;
        private System.Windows.Forms.Label label15;
    }
}

