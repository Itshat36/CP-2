﻿import System.Drawing
import System.Windows.Forms
import math

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(356, 317)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(264, 78)
		self._button1.TabIndex = 0
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(275, 143)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 173)
		self._button2.TabIndex = 1
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(626, 143)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 173)
		self._button3.TabIndex = 2
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.ImeMode = System.Windows.Forms.ImeMode.On
		self._listBox1.Location = System.Drawing.Point(356, 143)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(264, 173)
		self._listBox1.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(931, 444)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "lang122a"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for num in range(1, 50 + 1):
			numSqd = num**2
			numSqrt = round(math.sqrt(num), 4)
			self._listBox1.Items.Add(str(num) + "\t" + str(numSqd) + "\t" + str(numSqrt))

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()

