"""
	Author: H.Q.A
	Copyright: H.Q.A
"""
class ExpProcess():
	"""Class Xu li bieu thuc so hoc"""
	__opelist = ('+','-','*','/','%','^','~','^^','<','>','=','(',')','<=','>=','//')

	def __init__(self,oList = __opelist):
		self.list = oList
		self.__num = []
		self.__ope = []

	def Reset(self):
		self.__num = []
		self.__ope = []

	def __FormatExp(self,exp):
		# kiem tra truong hop ket thuc la dau )
		if exp.endswith(')'):
			exp = exp + '+0'
		# Bo het khoang trang o dau va cuoi bieu thuc
		exp.strip()
		return exp

	def __GetPriority(self,op):
		if op == '~':
			return 5
		elif (op == '^') or (op == '^^'):
			return 4
		elif (op == '*') or (op == '/') or (op == '%') or (op == '//'):
			return 3
		elif (op == '+') or (op == '-'):
			return 2
		elif (op == '>') or (op == '<') or (op == '=') or (op == '<=') or (op == '>='):
			return 1
		return 0
	
	def ConvertToStack(self,exp):
		s,e = 0,0
		stack = []
		n = len(exp)
		while e<n:
			if exp[e] in self.list:
				if exp[s:e] != '':
					stack.append(exp[s:e])
				stack.append(exp[e])
				#dat lai
				s = e + 1

			e = e + 1
		# lay phan tu cuoi
		stack.append(exp[s:e])

		# Quet stack de gop cac toan tu nhieu ki tu
		i = 1
		n = len(stack)
		while i<n:
			if (stack[i] in self.list) and (stack[i-1] in self.list):
				if (stack[i-1] == '(') or (stack[i-1] == ')') or (stack[i] == '(') or (stack[i] == ')') or (stack[i] == '~'):
					# Dieu kien ben tren phai gan ca nhung toan tu 1 ngoi
					i = i + 1
				else:
					stack[i-1] = str(stack[i-1]) + str(stack[i])
					del stack[i]
					n = len(stack)
			else:
				i = i + 1
		return stack

	def GetPostfix(self,exp):
		exp = self.ConvertToStack(exp)

		for i in exp:
			if i == '(':
				self.__ope.append('(')
			elif i == ')':
				n = len(self.__ope)-1
				while self.__ope[n] != '(':
					self.__num.append(self.__ope[n])
					del self.__ope[n]
					n = n - 1
				del self.__ope[n]

			elif i in self.list:
				while (len(self.__ope)>0) and (self.__GetPriority(i) <= self.__GetPriority(self.__ope[len(self.__ope)-1])):
					self.__num.append(self.__ope[len(self.__ope)-1])
					del self.__ope[len(self.__ope)-1]
				self.__ope.append(i)	
			else:
				self.__num.append(i)

		# dua not self.__ope -> self.__num
		n = len(self.__ope)-1
		while n >= 0:
			self.__num.append(self.__ope[n])
			del self.__ope[n]
			n = n - 1

	def __StackMove(self,stack,s,st):
		e = len(stack)-st
		for i in range(s,e):
			stack[s] = stack[s+st]
		return stack


	def CalcExp(self,exp):
		exp = self.__FormatExp(exp)
		self.GetPostfix(exp)
		self.__num.reverse()
		# thuc hien tinh toan

		sub = 0.0
		i = len(self.__num)-1
		while (i>-1):
			if self.__num[i] in self.list:
				if self.__num[i] == '+':
					sub = float(self.__num[i+2])+float(self.__num[i+1])
					del self.__num[i+2]
					del self.__num[i+1]
					self.__num[i] = sub
				elif self.__num[i] == '-':
					sub = float(self.__num[i+2])-float(self.__num[i+1])
					del self.__num[i+2]
					del self.__num[i+1]
					self.__num[i] = sub
				elif self.__num[i] == '*':
					sub = float(self.__num[i+2])*float(self.__num[i+1])
					del self.__num[i+2]
					del self.__num[i+1]
					self.__num[i] = sub
				elif self.__num[i] == '/':
					sub = float(self.__num[i+2])/float(self.__num[i+1])
					del self.__num[i+2]
					del self.__num[i+1]
					self.__num[i] = sub
				elif self.__num[i] == '%':
					sub = float(self.__num[i+2])%float(self.__num[i+1])
					del self.__num[i+2]
					del self.__num[i+1]
					self.__num[i] = sub
				elif self.__num[i] == '^':
					sub = float(self.__num[i+2])**float(self.__num[i+1])
					del self.__num[i+2]
					del self.__num[i+1]
					self.__num[i] = sub
				elif self.__num[i] == '^^':
					sub = float(self.__num[i+1])**(1/float(self.__num[i+2]))
					del self.__num[i+2]
					del self.__num[i+1]
					self.__num[i] = sub
				elif self.__num[i] == '//':
					sub = float(self.__num[i+2])//float(self.__num[i+1])
					del self.__num[i+2]
					del self.__num[i+1]
					self.__num[i] = sub
				elif self.__num[i] == '<':
					if float(self.__num[i+2]) < float(self.__num[i+1]):
						self.__num[i] = 1
					else:
						self.__num[i] = 0
					del self.__num[i+2]
					del self.__num[i+1]
				elif self.__num[i] == '>':
					if float(self.__num[i+2]) > float(self.__num[i+1]):
						self.__num[i] = 1
					else:
						self.__num[i] = 0
					del self.__num[i+2]
					del self.__num[i+1]
				elif self.__num[i] == '=':
					if float(self.__num[i+2]) == float(self.__num[i+1]):
						self.__num[i] = 1
					else:
						self.__num[i] = 0
					del self.__num[i+2]
					del self.__num[i+1]
				elif self.__num[i] == '>=':
					if float(self.__num[i+2]) >= float(self.__num[i+1]):
						self.__num[i] = 1
					else:
						self.__num[i] = 0
					del self.__num[i+2]
					del self.__num[i+1]
				elif self.__num[i] == '<=':
					if float(self.__num[i+2]) <= float(self.__num[i+1]):
						self.__num[i] = 1
					else:
						self.__num[i] = 0
					del self.__num[i+2]
					del self.__num[i+1]
				# toan tu 1 ngoi	
				elif self.__num[i] == '~':
					sub = 0-float(self.__num[i+1])
					del self.__num[i+1]
					self.__num[i] = sub

			else:
				i = i - 1

		return self.__num[0]	


#Main
'''e = '56*(8.5-5*12)+3'
p = ExpProcess()
print(p.CalcExp(e))'''