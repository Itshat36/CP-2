import System.Drawing
import System.Windows.Forms
import Form1

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._textBox7 = System.Windows.Forms.TextBox()
		self._textBox8 = System.Windows.Forms.TextBox()
		self._Cost = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._textBox8)
		self._groupBox1.Controls.Add(self._textBox7)
		self._groupBox1.Controls.Add(self._label8)
		self._groupBox1.Controls.Add(self._label7)
		self._groupBox1.Controls.Add(self._textBox6)
		self._groupBox1.Controls.Add(self._textBox5)
		self._groupBox1.Controls.Add(self._label6)
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._textBox4)
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(13, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(715, 194)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "groupBox1"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label1.Location = System.Drawing.Point(7, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Name"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label2.Location = System.Drawing.Point(7, 47)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Company"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label3.Location = System.Drawing.Point(7, 74)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Address"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label4.Location = System.Drawing.Point(7, 101)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "City"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(114, 24)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(114, 50)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(114, 76)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 6
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(114, 103)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 7
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label5.Location = System.Drawing.Point(312, 20)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 8
		self._label5.Text = "Phone"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label6.Location = System.Drawing.Point(312, 47)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 9
		self._label6.Text = "Email"
		# 
		# textBox5
		# 
		self._textBox5.Location = System.Drawing.Point(419, 20)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(100, 20)
		self._textBox5.TabIndex = 10
		# 
		# textBox6
		# 
		self._textBox6.Location = System.Drawing.Point(419, 47)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(100, 20)
		self._textBox6.TabIndex = 11
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label7.Location = System.Drawing.Point(281, 103)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(42, 23)
		self._label7.TabIndex = 12
		self._label7.Text = "State"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label8.Location = System.Drawing.Point(435, 101)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(37, 23)
		self._label8.TabIndex = 13
		self._label8.Text = "Zip"
		# 
		# textBox7
		# 
		self._textBox7.Location = System.Drawing.Point(329, 103)
		self._textBox7.Name = "textBox7"
		self._textBox7.Size = System.Drawing.Size(100, 20)
		self._textBox7.TabIndex = 14
		# 
		# textBox8
		# 
		self._textBox8.Location = System.Drawing.Point(478, 101)
		self._textBox8.Name = "textBox8"
		self._textBox8.Size = System.Drawing.Size(100, 20)
		self._textBox8.TabIndex = 15
		# 
		# Cost
		# 
		self._Cost.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._Cost.Location = System.Drawing.Point(491, 210)
		self._Cost.Name = "Cost"
		self._Cost.Size = System.Drawing.Size(100, 23)
		self._Cost.TabIndex = 1
		# 
		# label9
		# 
		self._label9.Location = System.Drawing.Point(385, 214)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 2
		self._label9.Text = "Total Camp"
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(22, 256)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(207, 134)
		self._button1.TabIndex = 16
		self._button1.Text = "Set confrencce Options"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(235, 256)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(207, 134)
		self._button2.TabIndex = 17
		self._button2.Text = "Reset"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(448, 256)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(207, 134)
		self._button3.TabIndex = 18
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(740, 443)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._Cost)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg479"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		form1 = Form1.Form1(self)
		form1.Show()
		self.Hide()