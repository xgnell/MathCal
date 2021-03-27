'''
	Author: H.Q.A
	Copyright: H.Q.A
'''

# Bien dich cac ham can ban
import math
import os
import MathFunc as mf
import ExpressionProcess as ep
import OutPut

class FuncProcess():

	def __init__(self):
		#self.__Ex = exp
		self.__modules = ['systemCmd']
		self.__op = OutPut.Output()

	def Reset(self):
		self.__modules = ['systemCmd']

	def __GetName(self,exp,s,e):
		_fName = exp[s+1:e]
		return _fName

	def __SubProcess(self,exp):
		if (exp.startswith("'") == False) and (exp.endswith("'") == False):
			r = ep.ExpProcess()
			rs = r.CalcExp(exp)
			return rs
		return exp[1:len(exp)-1]

	def __GetParams(self,exp,s,e,data):
		# lay param
		more = True
		#kiem tra so luong doi so
		get = exp.find(',',s,e)
		if get == -1: more = False
		# Lay doi so
		if more == False:
			e = exp[s+1:e]
			rs = self.__SubProcess(e)
			data.append(str(rs))
		else:
			sub = exp[s+1:e]
			n = sub.find(',')
			while n != -1:
				rs = self.__SubProcess(sub[0:n])
				data.append(str(rs))
				sub = sub[n+1:len(sub)]
				n = sub.find(',')
			rs = self.__SubProcess(sub)
			data.append(str(rs))	

	def __ToFloat(self,dt,n):
		for i in range(1,n+1):
			dt[i] = float(dt[i])

	# Cac ham xu li functions cua rieng cac thu vien
	def __systemCmdModule(self,data):
		name = data[0]
		result = 0

		# kiem tra ham he thong
		if name == 'print':
			self.__op.out(data[1])
		# Hai ham xu li file chi hoat dong tren Windows, neu muon ham
		# hoat dong o nhung he dieu hanh khac thi phai thay the bang
		# ham cua Python	
		elif name == 'printFile':
			os.system('echo ' + data[2] + ' > ' + data[1])
			self.__op.out(result = '----- Info: Saved data to ' + data[1] + ' -----')
		elif name == 'appendFile':
			os.system('echo ' + data[2] + ' >> ' + data[1])
			self.__op.out(result = '----- Info: Added data to ' + data[1] + ' -----')
		elif name == 'readFile':
			os.system('type ' + data[1])
			self.__op.out(result = '----- Info: Read ' + data[1] + ' -----')
		elif name == 'exec':
			os.system('start ' + data[1])
			self.__op.out(result = '----- Info: Started ' + data[1] + ' -----')
		elif name == 'ls':
			os.system('dir ' + data[1])
			self.__op.out(result = '----- Info: Listed all data in ' + data[1] + ' -----')
		elif name == 'color':
			os.system('color ' + data[1])
			self.__op.out(result = '----- Info: Changed color -----')
		elif name == 'shutdownCom':
			os.system('shutdown -s -f -t ' + data[1])
			self.__op.out(result = '----- Info: Preparing for shutdown -----')
		elif name == 'restartCom':
			os.system('shutdown -r -f -t ' + data[1])
			self.__op.out(result = '----- Info: Preparing for restart -----')
		elif name == 'datenow':
			os.system(r'echo %date%')
		elif name == 'timenow':
			os.system(r'echo %time%')
		elif name == 'clock':
			os.system(r'echo %date% & echo %time%')
		elif name == 'symbols':
			os.system('charmap')
			self.__op.out(result = '----- Info: Specials symbols for insert -----')
		elif name == 'panels':
			os.system('control')
			self.__op.out(result = '----- Info: Opened Control Panels -----')
		elif name == 'paintProg':
			os.system('mspaint')
			self.__op.out(result = '----- Info: Opened MS Paint -----')
		elif name == 'virtualKey':
			os.system('osk')
			self.__op.out(result = '----- Info: Opened virtual Keyboard -----')
		elif name == 'registry':
			os.system('regedit')
		elif name == 'taskmng':
			os.system('taskmgr')
		elif name == 'winver':
			os.system('winver')
			self.__op.out('----- Info: Show windows version -----')
		elif name == 'wordpad':
			os.system('write')
		elif name == 'calcProg':
			os.system('calc')
			self.__op.out('----- Info: Opened windows Calculator -----')
		elif name == 'system':
			os.system(data[1])

		# Cac ham xu li bien
		'''elif name == 'sto':
			self.__var.SetValue(data[1],data[2])
		elif name == 'clearMem':
			self.__var.ClearAll()
		elif name == 'showVar':
			self.__var.ShowValue(data[1])
		elif name == 'showAllVar':
			self.__var.ShowAllValue()
		elif name == 'addVar':
			self.__var.AddValue(data[1],data[2])
		elif name == 'subtVar':
			self.__var.SubtractValue(data[1],data[2])'''

		return result


	def __mathsFuncModule(self,data):
		name = data[0]
		result = 0

		#Kiem tra cac ham cua modules mathFunc
		if name == '_quadratic':
			self.__ToFloat(data,3)
			result = mf.Quadratic(data[1],data[2],data[3])
		elif name == '_qr':
			self.__ToFloat(data,2)
			result = mf.Qr(data[1],data[2])
		elif name == '_gcd':
			self.__ToFloat(data,2)
			result = mf.Gcd(data[1],data[2])
		elif name == '_compact':
			result = mf.Compact(int(data[1]),int(data[2]))

		return result

	def __physicsFuncMudule(self,data):
		pass

	def __chemistryFuncModule(self,data):
		pass

	def __biologyFuncModule(self,data):
		pass


	# Cac ham xu li thu vien chinh

	def __ImportModules(self,name):
		if name == 'mathFunc':
			if self.__modules.count('mathFunc') == 0:
				self.__modules.append('mathFunc')
		elif name == 'physicsFunc':
			if self.__modules.count('physicsFunc') == 0:
				self.__modules.append('physicsFunc')
		elif name == 'chemistryFunc':
			if self.__modules.count('chemistryFunc') == 0:
				self.__modules.append('chemistryFunc')
		elif name == 'biologyFunc':
			if self.__modules.count('biologyFunc') == 0:
				self.__modules.append('biologyFunc')
		elif name == 'systemCmd':
			if self.__modules.count('systemCmd') == 0:
				self.__modules.append('systemCmd')


	def __FuncCalc(self,data):
		name = data[0]
		result = 0

		#Kiem tra cac ham trong cac modules khac
		r = 0
		if self.__modules.count('mathFunc') != 0:
			r = self.__mathsFuncModule(data)
		if self.__modules.count('physicsFunc') != 0:
			r = self.__physicsFuncMudule(data)
		if self.__modules.count('chemistryFunc') != 0:
			r = self.__chemistryFuncModule(data)
		if self.__modules.count('biologyFunc') != 0:
			r = self.__biologyFuncModule(data)
		if self.__modules.count('systemCmd') != 0:
			r = self.__systemCmdModule(data)
		#gan lai gia tri tra ve
		result = r

		#Kiem tra lenh add modules
		if name == 'import':
			self.__ImportModules(data[1])
		elif name == 'unimport':
			self.__modules.remove(data[1])
		# kiem tra ham toan hoc can ban (moi ngon ngu lap trinh deu co)
		if name == 'const':
			if data[1] == 'pi':
				result = 3.141592654
			elif data[1] == 'e':
				result = 2.718281828
			elif data[1] == 'gold_ratio':
				result = 1.6180339887
			else:
				result = None
		elif name == 'sqrt':
			self.__ToFloat(data,1)
			result = math.sqrt(data[1])
		elif name == 'nthrt':
			self.__ToFloat(data,2)
			result = data[2]**(data[1]**-1)
		elif name == 'pow':
			self.__ToFloat(data,2)
			result = math.pow(data[1],data[2])
		elif name == 'abs':
			self.__ToFloat(data,1)
			result = math.fabs(data[1])
		elif name == 'fac':
			self.__ToFloat(data,1)
			result = math.factorial(data[1])
		elif name == 'pytago':
			self.__ToFloat(data,2)
			result = math.hypot(data[1],data[2])
		elif name == 'degrees':
			self.__ToFloat(data,1)
			result = math.degrees(data[1])
		elif name == 'radians':
			self.__ToFloat(data,1)
			result = math.radians(data[1])
		elif name == 'sin':
			self.__ToFloat(data,1)
			result = math.sin(data[1])
		elif name == 'cos':
			self.__ToFloat(data,1)
			result = math.cos(data[1])
		elif name == 'tan':
			self.__ToFloat(data,1)
			result = math.tan(data[1])
		elif name == 'cot':
			self.__ToFloat(data,1)
			result = (math.cos(data[1]))/(math.sin(data[1]))
		elif name == 'asin':
			self.__ToFloat(data,1)
			result = math.asin(data[1])
		elif name == 'acos':
			self.__ToFloat(data,1)
			result = math.acos(data[1])
		elif name == 'atan':
			self.__ToFloat(data,1)
			result = math.atan(data[1])
		elif name == 'compare':
			data[1] = float(data[1])
			data[3] = float(data[3])
			if data[2] == '==':
				if data[1] == data[3]:
					self.__op.out('True')
				else:
					self.__op.out('False')
			elif data[2] == '<':
				 if data[1] < data[3]:
				 	self.__op.out('True')
				 else:
				 	self.__op.out('False')
			elif data[2] == '>':
				if data[1] > data[3]:
					self.__op.out('True')
				else:
					self.__op.out('False')
			elif data[2] == '<=':
				if data[1] <= data[3]:
					self.__op.out('True')
				else:
					self.__op.out('False')
			elif data[2] == '>=':
				if data[1] >= data[3]:
					self.__op.out('True')
				else:
					self.__op.out('False')
		
		return result


	def ReadFunction(self,exp = None):
		end = exp.find(']')
		while end != -1:
			start = exp.rfind('[',0,end)
			fname = exp.rfind('@',0,start)
			_name = self.__GetName(exp,fname,start)
			dt = []
			dt.append(_name)
			self.__GetParams(exp,start,end,dt)
			r = self.__FuncCalc(dt)
			exp = exp[0:fname] + str(r) + exp[end+1:None]

			end = exp.find(']')
		return exp


#main
'''exp = input('>> ')
obj = FuncProcess(exp)
print(obj.ReadFunction())'''
