
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._Reset = System.Windows.Forms.Button()
		self._Close = System.Windows.Forms.Button()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._checkBox2)
		self._groupBox1.Controls.Add(self._checkBox1)
		self._groupBox1.Location = System.Drawing.Point(38, 22)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(287, 100)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "groupBox1"
		# 
		# groupBox2
		# 
		self._groupBox2.Location = System.Drawing.Point(379, 22)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(200, 100)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "groupBox2"
		# 
		# Reset
		# 
		self._Reset.Location = System.Drawing.Point(38, 146)
		self._Reset.Name = "Reset"
		self._Reset.Size = System.Drawing.Size(75, 23)
		self._Reset.TabIndex = 2
		self._Reset.Text = "Reset"
		self._Reset.UseVisualStyleBackColor = True
		# 
		# Close
		# 
		self._Close.Location = System.Drawing.Point(379, 146)
		self._Close.Name = "Close"
		self._Close.Size = System.Drawing.Size(75, 23)
		self._Close.TabIndex = 3
		self._Close.Text = "button2"
		self._Close.UseVisualStyleBackColor = True
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(7, 20)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(186, 24)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "Confrence: 895$"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(7, 51)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "checkBox2"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(738, 364)
		self.Controls.Add(self._Close)
		self.Controls.Add(self._Reset)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "Form1"
		self.Text = "Form1"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)

