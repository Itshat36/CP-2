
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
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._lblTickets = System.Windows.Forms.Label()
		self._lblTax = System.Windows.Forms.Label()
		self._lblTotal = System.Windows.Forms.Label()
		self._RadSec1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._btnCalculate = System.Windows.Forms.Button()
		self._btnClose = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._txtNumTickets = System.Windows.Forms.TextBox()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._txtNumTickets)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Location = System.Drawing.Point(71, 26)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(432, 100)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Tickets"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._radioButton3)
		self._groupBox2.Controls.Add(self._radioButton2)
		self._groupBox2.Controls.Add(self._RadSec1)
		self._groupBox2.Location = System.Drawing.Point(71, 132)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(214, 93)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Section"
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._lblTotal)
		self._groupBox3.Controls.Add(self._lblTax)
		self._groupBox3.Controls.Add(self._lblTickets)
		self._groupBox3.Controls.Add(self._label3)
		self._groupBox3.Controls.Add(self._label2)
		self._groupBox3.Controls.Add(self._label1)
		self._groupBox3.Location = System.Drawing.Point(291, 132)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(212, 93)
		self._groupBox3.TabIndex = 2
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Total"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(7, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Tickets"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(7, 42)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Tax"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(7, 65)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Total"
		# 
		# lblTickets
		# 
		self._lblTickets.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._lblTickets.Location = System.Drawing.Point(106, 20)
		self._lblTickets.Name = "lblTickets"
		self._lblTickets.Size = System.Drawing.Size(100, 23)
		self._lblTickets.TabIndex = 3
		# 
		# lblTax
		# 
		self._lblTax.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._lblTax.Location = System.Drawing.Point(106, 42)
		self._lblTax.Name = "lblTax"
		self._lblTax.Size = System.Drawing.Size(100, 23)
		self._lblTax.TabIndex = 4
		# 
		# lblTotal
		# 
		self._lblTotal.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._lblTotal.Location = System.Drawing.Point(106, 65)
		self._lblTotal.Name = "lblTotal"
		self._lblTotal.Size = System.Drawing.Size(100, 23)
		self._lblTotal.TabIndex = 5
		# 
		# RadSec1
		# 
		self._RadSec1.Location = System.Drawing.Point(7, 20)
		self._RadSec1.Name = "RadSec1"
		self._RadSec1.Size = System.Drawing.Size(104, 24)
		self._RadSec1.TabIndex = 0
		self._RadSec1.TabStop = True
		self._RadSec1.Text = "section 1"
		self._RadSec1.UseVisualStyleBackColor = True
		self._RadSec1.CheckedChanged += self.RadSec1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(7, 42)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "section 2"
		self._radioButton2.UseVisualStyleBackColor = True
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(7, 65)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "section 3"
		self._radioButton3.UseVisualStyleBackColor = True
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# btnCalculate
		# 
		self._btnCalculate.Location = System.Drawing.Point(71, 232)
		self._btnCalculate.Name = "btnCalculate"
		self._btnCalculate.Size = System.Drawing.Size(75, 23)
		self._btnCalculate.TabIndex = 3
		self._btnCalculate.Text = "Calculate"
		self._btnCalculate.UseVisualStyleBackColor = True
		self._btnCalculate.Click += self.BtnCalculateClick
		# 
		# btnClose
		# 
		self._btnClose.Location = System.Drawing.Point(291, 232)
		self._btnClose.Name = "btnClose"
		self._btnClose.Size = System.Drawing.Size(75, 23)
		self._btnClose.TabIndex = 4
		self._btnClose.Text = "Close"
		self._btnClose.UseVisualStyleBackColor = True
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(11, 20)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 0
		self._label4.Text = "Number of tickets"
		# 
		# txtNumTickets
		# 
		self._txtNumTickets.Location = System.Drawing.Point(237, 23)
		self._txtNumTickets.Name = "txtNumTickets"
		self._txtNumTickets.Size = System.Drawing.Size(100, 20)
		self._txtNumTickets.TabIndex = 1
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(685, 424)
		self.Controls.Add(self._btnClose)
		self.Controls.Add(self._btnCalculate)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox1)
		self.Name = "Form1"
		self.Text = "Form1"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self.ResumeLayout(False)


	def BtnCalculateClick(self, sender, e):
		Tickets = 0.0
		ticketsCost = 0.0
		Tax = 0.06
		
		if self._RadSec1.Checked == True:
			x = self._txtNumTickets.Text * 20
			self._lblTickets.Text = x 
			
		if self._radioButton2.Checked == True:
			x * 15
		
		if self._radioButton3.Checked == True:
			x * 10
		
		#self._lblTickets.Text = x 
		#self._lblTax.Text = Tax
		#self._lblTotal.Text = x + Tax
		
		
		
	def RadSec1CheckedChanged(self, sender, e):
		pass

	def RadioButton2CheckedChanged(self, sender, e):
		pass

	def RadioButton3CheckedChanged(self, sender, e):
		pass

