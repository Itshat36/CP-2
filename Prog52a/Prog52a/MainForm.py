import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label6 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(161, 44)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 36)
		self._label1.TabIndex = 0
		self._label1.Text = "Length"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(314, 44)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 2
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Red
		self._button1.Location = System.Drawing.Point(161, 141)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(252, 55)
		self._button1.TabIndex = 4
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Snow
		self._label3.Location = System.Drawing.Point(161, 203)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Area"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Snow
		self._label4.Location = System.Drawing.Point(161, 244)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 6
		self._label4.Text = "Perimiter"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(268, 203)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 7
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Red
		self._button2.Location = System.Drawing.Point(134, 290)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(190, 79)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(330, 290)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(188, 79)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(268, 244)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 11
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(314, 94)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 3
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(161, 94)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 34)
		self._label2.TabIndex = 1
		self._label2.Text = "Width"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(224, 224, 224)
		self.ClientSize = System.Drawing.Size(946, 453)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang52a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()
	

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""

	def Button1Click(self, sender, e):
		length = int(self._textBox1.Text)
		width = int(self._textBox2.Text)
		area = length * width
		perim = 2 * length + 2 * width
		self._label5.Text = str(area)
		self._label6.Text = str(perim)