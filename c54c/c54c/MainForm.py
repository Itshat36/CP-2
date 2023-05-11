import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label6 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(300, 229)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 20
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(362, 275)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(188, 79)
		self._button3.TabIndex = 19
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Red
		self._button2.Location = System.Drawing.Point(166, 275)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(190, 79)
		self._button2.TabIndex = 18
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(300, 188)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 17
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Snow
		self._label4.Location = System.Drawing.Point(193, 229)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 16
		self._label4.Text = " Circumference"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Snow
		self._label3.Location = System.Drawing.Point(193, 188)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 15
		self._label3.Text = "Area"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Red
		self._button1.Location = System.Drawing.Point(193, 126)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(252, 55)
		self._button1.TabIndex = 14
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(345, 87)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 13
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(193, 87)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 36)
		self._label1.TabIndex = 12
		self._label1.Text = "Radius"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(716, 440)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "c54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		length = float(self._textBox1.Text)
		one = length * 2 
		Area = one * 3.14159
		Radius = length / 3.14159 * 2
		self._label5.Text = str(round(Area))
		self._label6.Text = str(round(Radius))