import System.Drawing
import System.Windows.Forms
import Form1
import Form2

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._btnExit = System.Windows.Forms.Button()
		self._btnGeneral = System.Windows.Forms.Button()
		self._btnstudent = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._btnstudent)
		self._groupBox1.Controls.Add(self._btnGeneral)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(59, 13)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(372, 227)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "groupBox1"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(7, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(192, 56)
		self._label1.TabIndex = 0
		self._label1.Text = "Select the sale of tickets sold to the public "
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(7, 108)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(151, 40)
		self._label2.TabIndex = 1
		self._label2.Text = "Select the sale of tickets sold to the Students"
		# 
		# btnExit
		# 
		self._btnExit.Location = System.Drawing.Point(356, 246)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(75, 23)
		self._btnExit.TabIndex = 1
		self._btnExit.Text = "Exit"
		self._btnExit.UseVisualStyleBackColor = True
		self._btnExit.Click += self.BtnExitClick
		# 
		# btnGeneral
		# 
		self._btnGeneral.Location = System.Drawing.Point(206, 20)
		self._btnGeneral.Name = "btnGeneral"
		self._btnGeneral.Size = System.Drawing.Size(75, 39)
		self._btnGeneral.TabIndex = 2
		self._btnGeneral.Text = "General sales"
		self._btnGeneral.UseVisualStyleBackColor = True
		self._btnGeneral.Click += self.BtnGeneralClick
		# 
		# btnstudent
		# 
		self._btnstudent.Location = System.Drawing.Point(206, 108)
		self._btnstudent.Name = "btnstudent"
		self._btnstudent.Size = System.Drawing.Size(75, 40)
		self._btnstudent.TabIndex = 3
		self._btnstudent.Text = "Student Sales"
		self._btnstudent.UseVisualStyleBackColor = True
		self._btnstudent.Click += self.BtnstudentClick
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(628, 378)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "Pg435TicketSalesPython"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def BtnGeneralClick(self, sender, e):
		form1 = Form1.Form1(self)
		form1.Show()
		self.Hide()


	def BtnstudentClick(self, sender, e):
		form2 = Form2.Form2(self)
		form2.Show()
		self.Hide()

	def BtnExitClick(self, sender, e):
		Application.Exit()