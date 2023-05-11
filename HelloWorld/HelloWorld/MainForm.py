﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Lime
		self._button1.Location = System.Drawing.Point(212, 206)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(216, 123)
		self._button1.TabIndex = 0
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LawnGreen
		self._button2.Location = System.Drawing.Point(434, 206)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(216, 123)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Green
		self._button3.Location = System.Drawing.Point(212, 335)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(438, 103)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit "
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(212, 80)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(438, 123)
		self._label1.TabIndex = 3
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DimGray
		self.ClientSize = System.Drawing.Size(918, 442)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "HelloWorld"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text="Hello, World"

	def Button2Click(self, sender, e):
		self._label1.Text=""

	def Button3Click(self, sender, e):
		Application.Exit()