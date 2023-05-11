import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(94, 223)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(129, 91)
		self._button1.TabIndex = 0
		self._button1.Text = "show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(229, 223)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(129, 91)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(156, 30)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(57, 20)
		self._label1.TabIndex = 2
		self._label1.Text = "Enter Text"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(156, 111)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(57, 41)
		self._label2.TabIndex = 3
		self._label2.Text = "soulution:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightCoral
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(219, 111)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(129, 41)
		self._label3.TabIndex = 5
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(364, 223)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(129, 91)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(219, 30)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(129, 20)
		self._textBox1.TabIndex = 7
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(556, 360)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "StrInt4"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._textBox1.Text = ""

	def Button1Click(self, sender, e):
		self._label3.Text = ""
		text = self._textBox1.Text
		self._label3.Text = reversedstring=''.join(reversed(text))