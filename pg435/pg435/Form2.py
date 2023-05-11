
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
		
class Form2(Form):
	def __init__(self,mainform):
		self.InitializeComponent()
		self.mainform = mainform
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._txtNumTickets = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._btnCalculate = System.Windows.Forms.Button()
		self._btnClose = System.Windows.Forms.Button()
		self._lblTickets = System.Windows.Forms.Label()
		self._lblTax = System.Windows.Forms.Label()
		self._lblTotal = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._txtNumTickets)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(229, 135)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Tickets"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._lblTotal)
		self._groupBox2.Controls.Add(self._lblTax)
		self._groupBox2.Controls.Add(self._lblTickets)
		self._groupBox2.Controls.Add(self._label4)
		self._groupBox2.Controls.Add(self._label3)
		self._groupBox2.Controls.Add(self._label2)
		self._groupBox2.Location = System.Drawing.Point(247, 12)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(217, 135)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Cash"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(7, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Number of Tickets"
		# 
		# txtNumTickets
		# 
		self._txtNumTickets.Location = System.Drawing.Point(114, 20)
		self._txtNumTickets.Name = "txtNumTickets"
		self._txtNumTickets.Size = System.Drawing.Size(100, 20)
		self._txtNumTickets.TabIndex = 1
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(7, 19)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 0
		self._label2.Text = "Tickets"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(7, 46)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 1
		self._label3.Text = "Tax"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(7, 73)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 2
		self._label4.Text = "Total"
		# 
		# btnCalculate
		# 
		self._btnCalculate.Location = System.Drawing.Point(136, 153)
		self._btnCalculate.Name = "btnCalculate"
		self._btnCalculate.Size = System.Drawing.Size(105, 33)
		self._btnCalculate.TabIndex = 2
		self._btnCalculate.Text = "Calculate"
		self._btnCalculate.UseVisualStyleBackColor = True
		self._btnCalculate.Click += self.BtnCalculateClick
		# 
		# btnClose
		# 
		self._btnClose.Location = System.Drawing.Point(247, 153)
		self._btnClose.Name = "btnClose"
		self._btnClose.Size = System.Drawing.Size(106, 33)
		self._btnClose.TabIndex = 3
		self._btnClose.Text = "Close"
		self._btnClose.UseVisualStyleBackColor = True
		self._btnClose.Click += self.BtnCloseClick
		# 
		# lblTickets
		# 
		self._lblTickets.BackColor = System.Drawing.Color.White
		self._lblTickets.Location = System.Drawing.Point(111, 16)
		self._lblTickets.Name = "lblTickets"
		self._lblTickets.Size = System.Drawing.Size(100, 23)
		self._lblTickets.TabIndex = 4
		# 
		# lblTax
		# 
		self._lblTax.BackColor = System.Drawing.Color.White
		self._lblTax.Location = System.Drawing.Point(111, 43)
		self._lblTax.Name = "lblTax"
		self._lblTax.Size = System.Drawing.Size(100, 23)
		self._lblTax.TabIndex = 4
		# 
		# lblTotal
		# 
		self._lblTotal.BackColor = System.Drawing.Color.White
		self._lblTotal.Location = System.Drawing.Point(111, 69)
		self._lblTotal.Name = "lblTotal"
		self._lblTotal.Size = System.Drawing.Size(100, 23)
		self._lblTotal.TabIndex = 5
		# 
		# Form2
		# 
		self.ClientSize = System.Drawing.Size(471, 397)
		self.Controls.Add(self._btnClose)
		self.Controls.Add(self._btnCalculate)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "Form2"
		self.Text = "Form2"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)
		


	def BtnCalculateClick(self, sender, e):
 		T = float(self._txtNumTickets.Text)
		x = T * 7
		Tax = x * 0.06
		total = x + Tax
		self._lblTickets.Text = str(round(x))
		self._lblTax.Text = str(round(Tax))
		self._lblTotal.Text = str(round(total))
		
		

	def BtnCloseClick(self, sender, e):
		self.Close()
		self.mainform.Show() 
		
	def Form1FormClosing(self, sender, e):
		self.mainform.Show()