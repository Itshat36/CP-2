
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form2(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 126)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(215, 114)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(215, 114)
		self._label1.TabIndex = 1
		self._label1.Text = "label1"
		# 
		# Form2
		# 
		self.ClientSize = System.Drawing.Size(231, 246)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "Form2"
		self.Text = "Form2"
		self.Load += self.Form2Load
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.Close()
		self.parent.Show()

	def Form2Load(self, sender, e):
		self._label1.Text = self.msg