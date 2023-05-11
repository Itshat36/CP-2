import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(147, 59)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 17)
		self._label1.TabIndex = 0
		self._label1.Text = "num1"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(147, 82)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 17)
		self._label2.TabIndex = 1
		self._label2.Text = "num2"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(147, 105)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 20)
		self._label3.TabIndex = 2
		self._label3.Text = "num3"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(147, 131)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 20)
		self._label4.TabIndex = 3
		self._label4.Text = "num4"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(253, 59)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(253, 82)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(253, 105)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 6
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(253, 131)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 7
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Red
		self._button1.Location = System.Drawing.Point(102, 181)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(381, 80)
		self._button1.TabIndex = 8
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Red
		self._button2.Location = System.Drawing.Point(102, 350)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(186, 47)
		self._button2.TabIndex = 9
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(297, 350)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(186, 47)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(297, 279)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 11
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(297, 306)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 12
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.White
		self._label7.Location = System.Drawing.Point(130, 279)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 13
		self._label7.Text = "sum"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.White
		self._label8.Location = System.Drawing.Point(130, 306)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 14
		self._label8.Text = "average"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(934, 438)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang52b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
		num4 = int(self._textBox4.Text)
		Sum = num1 + num2 + num3 + num4 
		average = Sum / 4.0
		self._label5.Text = str(Sum)
		self._label6.Text = str(average)
		
		#length = int(self._textBox1.Text)
        #width = int(self._textBox2.Text)
        #area = length * width
        #perim = 2 * length + 2 * width
        #self._label5.Text = str(area)
        #self._label6.Text = str(perim)

	def Button2Click(self, sender, e):
		self._textBox1.Text= ""
		self._textBox2.Text= ""
		self._textBox3.Text= ""
		self._textBox4.Text= ""
		self._label5.Text= ""
		self._label6.Text= ""
		self._label7.Text= ""
		self._label8.Text= ""

	def Button3Click(self, sender, e):
		Application.Exit()

