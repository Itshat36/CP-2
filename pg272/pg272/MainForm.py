import System.Drawing
import System.Windows.Forms
import math

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._Final = System.Windows.Forms.Label()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._groupBox2.SuspendLayout()
		self._groupBox4.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._radioButton3)
		self._groupBox2.Controls.Add(self._radioButton2)
		self._groupBox2.Controls.Add(self._radioButton1)
		self._groupBox2.Location = System.Drawing.Point(11, 12)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(236, 107)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "time of day"
		# 
		# groupBox4
		# 
		self._groupBox4.Controls.Add(self._label2)
		self._groupBox4.Controls.Add(self._textBox1)
		self._groupBox4.Controls.Add(self._Final)
		self._groupBox4.Controls.Add(self._label1)
		self._groupBox4.Location = System.Drawing.Point(253, 12)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(235, 107)
		self._groupBox4.TabIndex = 0
		self._groupBox4.TabStop = False
		self._groupBox4.Text = "Cost "
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(6, 57)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(69, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "cost"
		# 
		# Final
		# 
		self._Final.BackColor = System.Drawing.Color.White
		self._Final.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._Final.Location = System.Drawing.Point(81, 60)
		self._Final.Name = "Final"
		self._Final.Size = System.Drawing.Size(100, 20)
		self._Final.TabIndex = 1
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(7, 20)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Daytime"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(7, 51)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Evening "
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(7, 82)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Off peak"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(253, 126)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 2
		self._button1.Text = "show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(172, 125)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 3
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(210, 154)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(81, 34)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 2
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(7, 34)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(68, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "minutes"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(512, 201)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._groupBox2)
		self.Name = "MainForm"
		self.Text = "pg272"
		self._groupBox2.ResumeLayout(False)
		self._groupBox4.ResumeLayout(False)
		self._groupBox4.PerformLayout()
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		X = int(self._textBox1.Text) 
		strMessage = 0
		if self._radioButton1.Checked == True:
			strMessage = 0.07
		elif self._radioButton2.Checked == True:
			strMessage = 0.12
		elif self._radioButton3.Checked == True:
			strMessage = 0.05
		self._Final.Text = str(strMessage * X)

	def Button2Click(self, sender, e):
		self._Final.Text = ""
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()