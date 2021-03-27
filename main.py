'''
	MainCommand se doc modules truoc roi moi lay cac lenh tu Command
	Kiem tra loi khong du hoac qua nhieu tham so de truyen vao parameter

'''




# Khai bao cac modules
import ExpressionProcess as EP
import CommandProcess as CP
import FunctionProcess as FP
import os
import time
import random



# Khai bao cac doi tuong luu tru du lieu
Modules = []
Constants  = []
Variables = []
Function = []
Label = []
MainCommand = []
Parameters = []
Line = 0

DataTypes = ('variant','byte', 'int', 'float', 'string')

# Khoi tao cac doi tuong
expProcess = EP.ExpProcess()
cmdProcess = CP.CmdProcess()
funcProcess = FP.FuncProcess()


# ------------ CAC HAM XU LI CON ---------------------------------------
def checkVarExisted(varName):
	for i in Variables:
		if i[1] == varName:
			# --- Loi trung ten bien
			return True
	return False		

def getVarValue(varName):
	for i in Variables:
		if i[1] == varName:
			return i[2]

	# --- Loi khong tim thay bien
	return 0

def setVarValue(varName,value):
	for i in Variables:
		if i[1] == varName:
			i[2] = value
	# --- Loi kieu du lieu khong hop le
	#   --> Kiem tra kieu du lieu va check
	# --- Loi khong tim thay bien		

def getVarType(varName):
	for i in Variables:
		if i[1] == varName:
			return i[0]
	# --- Loi khong tim thay bien
	return 'variant'

def checkLabelExisted(lblName):
	for i in Label:
		if i[0] == lblName:
			# --- Loi trung ten label
			return True
	return False	

def getLabelLine(lblName):
	for i in Label:
		if i[0] == lblName:
			return i[1]
	return 0

def checkConstExisted(cName):
	for i in Constants:
		if i[1] == cName:
			# --- Loi trung ten hang
			return True
	return False

def getConstValue(cName):
	for i in Constants:
		if i[1] == cName:
			return i[2]

	# --- Loi khong tim thay hang
	return 0

def getConstType(cName):
	for i in Constants:
		if i[1] == cName:
			return i[0]

	# --- Loi khong tim thay hang
	return 0

def checkFuncExisted(fName):
	for i in Function:
		if i[0] == fName:
			# --- Loi trung ten ham, co the kiem tra doi so de xem co the nap chong hay khong
			return True
	return False

def getFuncLine(fName):
	for i in Function:
		if i[0] == fName:
			return i[1]
	return 0

def checkParamExisted(pName):
	for i in Parameters:
		if i[1] == pName:
			# --- Loi trung ten parameter
			return True
	return False		

def getParamValue(pName):
	for i in Parameters:
		if i[1] == pName:
			return i[2]

	# --- Loi khong tim thay Param
	return 0

def setParamValue(pName,value):
	for i in Parameters:
		if i[1] == pName:
			i[2] = value
	# --- Loi khong tim thay param

def checkModuleExisted(mName):
	for i in Modules:
		if i[1] == mName:
			# --- Loi trung ten modules
			return True
	return False

# ------------ CAC HAM XU LI CHINH -------------------------------------
def ResetAllData():
	global Modules
	global Constants
	global Variables
	global Function
	global Label
	global Parameters
	Modules = []
	Constants  = []
	Variables = []
	Function = []
	Label = []
	Parameters = []

def EProcess(expression):
	exp = expression

	# Xu li hang
	cPoint = exp.find('$')
	while cPoint != -1:
		endPoint = exp.find(' ',cPoint)
		cName = exp[cPoint+1:endPoint]
		exp = exp[0:cPoint] + str(getConstValue(cName)) + exp[endPoint+1:None]
		cPoint = exp.find('$')

	# Xu li bien
	varPoint = exp.find('#')
	while varPoint != -1:
		endPoint = exp.find(' ',varPoint)
		varName = exp[varPoint+1:endPoint]
		exp = exp[0:varPoint] + str(getVarValue(varName)) + exp[endPoint+1:None]
		varPoint = exp.find('#')

	# Xu li params
	pPoint = exp.find('`')
	while pPoint != -1:
		endPoint = exp.find(' ',pPoint)
		pName = exp[pPoint+1:endPoint]
		exp = exp[0:pPoint] + str(getParamValue(pName)) + exp[endPoint+1:None]
		pPoint = exp.find('`')

	# Xu li ham
	exp = funcProcess.ReadFunction(exp)

	# Xu li bieu thuc
	result = expProcess.CalcExp(exp)
	return result


# Ham doc va lay cac command
def GetCommand():
	global Line
	global MainCommand
	cmd = ''
	while True:
		cmd = input('')
		# Kiem tra cac lenh he thong
		if cmd == '--sysRun':
			# Can phai sua lai bang cach cat cac khoang trang
			break
		elif cmd == '--sysEditor':
			os.system('cls')
			for i in range(Line):
				print(MainCommand[i])
		elif cmd == '--sysClear':
			os.system('cls')
		elif cmd == '--sysExit':
			exit(0)
		elif cmd == '--sysNew':
			os.system('cls')
			MainCommand = []
			Line = 0
		elif cmd.find('--sysDelLine ') != -1:
			ln = int(cmd[cmd.find('--sysDelLine ')+13:None])
			print(ln)
			# Xoa dong lenh
			del MainCommand[ln]
			Line = Line - 1
			# In lai toan bo lenh he thong
			os.system('cls')
			for i in range(Line):
				print(MainCommand[i])
		elif cmd.find('--sysInsert ') != -1:
			ln = int(cmd[cmd.find('--sysInsert ')+12:cmd.find(':')])
			cm = cmd[cmd.find(':')+1:None]

			MainCommand.append('')
			n = len(MainCommand)-1
			for i in range(n,ln,-1):
				MainCommand[i] = MainCommand[i-1]
			MainCommand[ln] = cm
			Line = Line + 1

			# In lai toan bo lenh
			os.system('cls')
			for i in range(Line):
				print(MainCommand[i])
		elif cmd.find('--sysMathcal ') != -1:
			# Reset du lieu
			ResetAllData()
			MainCommand = []
			Line = 0
			# Doc file --> dich
			p = cmd.find('--sysMathcal ')+13
			path = cmd[p:None]
			f = open(path, mode = 'r')
			for line in f:
				MainCommand.append(line.strip())
				Line = Line + 1
			f.close()
			break
		else:
			MainCommand.append(cmd)
			Line = Line + 1

def GetCommandFromFile():
	global Line
	global Command
	global MainCommand

	ResetAllData()
	Command = []
	MainCommand = []
	Line = 0

	cmd = ''
	while True:
		cmd = input('')

		if cmd == 'clear':
			os.system('cls')
		elif cmd == 'exit':
			exit(0)
		elif cmd == 'help':
			print('=============================================================')
			print('Tong hop cac lenh Intepreter -- MathCal Programming Language')
			print('')
			print('clear: Xoa man hinh')
			print('exit: Thoat khoi trinh thong dich MathCal')
			print('help: Giup do ve cac lenh')
			print('mathcal <path/file.mc>: Dich file chuong trinh .mc')
			print('_____________________________________________________________')
			print('')
		elif cmd.find('mathcal ') != -1:
			p = cmd.find('mathcal ')+8
			path = cmd[p:None]
			f = open(path, mode = 'r')
			for line in f:
				Command.append(line)
				Line = Line + 1
			f.close()
			break


# Ham doc va lay toan bo command tu cac modules
def GetAllCommand():
	global Line
	global MainCommand
	global Modules
	
	# Lay cac modules ------------------------------------

	ln = 0
	while ln<len(MainCommand):
		n = MainCommand[ln].find('?import_')
		if n != -1:
			# Lay data
			p = MainCommand[ln][n+9:None].strip()
			dt = []
			cmdProcess.GetParams(p,dt)
			# Lay ten modules va path
			mName = dt[0]
			path = dt[1]
			# append modules
			if checkModuleExisted(mName) == False:
				Modules.append(mName)
			# append cac lenh
			m = open(path,mode = 'r')
			for line in m:
				MainCommand.append(line.strip())
				Line = Line + 1
			m.close()
		ln = ln + 1


	# Tra ve Line moi

def PreProcess():
	global Line
	global MainCommand
	global Label
	global Constants
	global Function
	global Parameters

	# Doc cac label va function
	for i in range(Line):
		cmd = MainCommand[i]
		point2 = cmd.find('_')
		point1 = cmd.find(':',0,point2)
		if point1 != -1:
			obj = cmd[0:point1].strip()
			
			if obj.startswith('@'):
				# Neu la function
				func = obj[1:None]
				if checkFuncExisted(func) == False:
					Function.append([func,i])
			else:
				# Neu la label
				lbl = obj
				if checkLabelExisted(lbl) == False:
					Label.append([lbl,i])

# Ham dich chinh
def Intepreter(startLine, endLine):
	global Line
	global MainCommand
	global Parameters

	for l in range(startLine, endLine+1):
		data = []
		cmd = MainCommand[l]
		command = ''
		expProcess.Reset()
		funcProcess.Reset()

		# Doc va lay cac du lieu co so
		point2 = cmd.find('_')
		point1 = cmd.find(':',0,point2)
		if point1 != -1:
			'''lbl = cmd[0:point1]
			if checkLabelExisted(lbl) == False:
				Label.append([lbl,l])'''
			command = cmd[point1+1:None]
		else:
			command = cmd
		point3 = command.find(';')	
		if point3 != -1:
			command = command[0:point3]

		point2 = command.find('_')	
		# Xu li command
		cmdName = command[0:point2]
		cmdParams = command[point2+1:None].strip()

		# Lay du lieu
		cmdProcess.GetParams(cmdParams,data)

		if cmdName == 'var':
			# --- Loi khong doc duoc bien (thieu param ten bien)
			# --- Loi khong tim thay bien
			# --  Loi sai kieu du lieu
			# Kiem tra trung ten bien		
			if checkVarExisted(data[0]) == False:
				Variables.append([data[1],data[0],0])

		elif cmdName == 'mov':
			data[1] = EProcess(data[1])
			setVarValue(data[0],data[1])
		elif cmdName == 'type':
			# Cmd type nay se lay kieu du lieu cua bien va dua ra man hinh
			print('Type of',data[0],'is',getVarType(data[0]))
		elif cmdName == 'stype':
			# Cmd stype nay se lay kieu du lieu cua mot bien va day vao 1 bien khac
			setVarValue(data[0],getVarType(data[1]))
		elif cmdName == 'print':
			data[0] = EProcess(data[0])
			print(data[0])
		elif cmdName == 'end':
			# Cho nay se return ma loi sau khi chay chuong trinh
			# tam thoi return 0 de ket thuc chuong trinh
			return [False,0]
		elif cmdName == 'goto':
			# --- loi khong tim thay label
			line = getLabelLine(data[0])
			return [True,line]
			break
			'''time = line - l
			nextline = True'''
		elif cmdName == 'wait':
			data[0] = float(data[0])
			time.sleep(data[0])
		elif cmdName == 'input':
			ans = input('')
			setVarValue(data[0],ans)
		elif cmdName == 'if':
			data[0] = EProcess(data[0])
			if data[0] == 1:
				# Thuc hien tuong duong lenh goto
				line = getLabelLine(data[1])
				return [True,line]
				break
		elif cmdName == 'for':
			# Lenh lap khong bien
			t = int(data[0])
			ln = getLabelLine(data[1])
			for loop in range(t-1):
				run = Intepreter(l+1,ln)
				while run[0] == True:
					run = Intepreter(run[1],ln)
		elif cmdName == 'foru':
			setVarValue(data[0],data[1])
			ln = getLabelLine(data[4])
			while (int(getVarValue(data[0])) >= int(data[1])) and (int(getVarValue(data[0])) < int(data[2])):
				run = Intepreter(l+1,ln)
				while run[0] == True:
					run = Intepreter(run[1],ln)
				setVarValue(data[0],int(getVarValue(data[0]))+int(data[3]))
				# --- De bi loi kieu du lieu int va float nen sau nay phai sua
				# --- Sua lai tat ca nhung cho ep kieu, thay vao do kiem tra kieu du lieu cua bien
				# --- Neu la kieu du lieu int(hoac number) thi chay, khong thi bao loi
		elif cmdName == 'ford':
			setVarValue(data[0],data[1])
			ln = getLabelLine(data[4])
			while (int(getVarValue(data[0])) <= int(data[1])) and (int(getVarValue(data[0])) > int(data[2])):
				run = Intepreter(l+1,ln)
				while run[0] == True:
					run = Intepreter(run[1],ln)
				setVarValue(data[0],int(getVarValue(data[0]))-int(data[3]))
				# --- De bi loi kieu du lieu int va float nen sau nay phai sua
				# --- Sua lai tat ca nhung cho ep kieu, thay vao do kiem tra kieu du lieu cua bien
				# --- Neu la kieu du lieu int(hoac number) thi chay, khong thi bao loi
		elif cmdName == 'while':
			cond = EProcess(data[0])
			ln = getLabelLine(data[1])
			while cond == 1:
				run = Intepreter(l+1,ln)
				while run[0] == True:
					run = Intepreter(run[1],ln)
				cond = EProcess(data[0])	
		elif cmdName == 'call':
			# data[0] var
			# data[1] func
			# data[2..] params

			# Lay line func
			ln = getFuncLine(data[1])
			# Xu li bieu thuc cho tham so
			for i in range(2,len(data)):
				data[i] = EProcess(data[i])
			# Quet lay param
			i = ln
			p = MainCommand[i].find('?params_')
			while p != -1:
				cmdP = MainCommand[i][p+9:None].strip()
				dt = []
				cmdProcess.GetParams(cmdP,dt)

				if checkParamExisted(dt[0]) == False:
					Parameters.append([dt[1],dt[0],0])
				i = i + 1
				if MainCommand[i].find('return_') != -1:
					break
				else:
					p = MainCommand[i].find('?params_')
			# Truyen tham so
			n = len(data)
			for i in range(2,n):
				# Kiem tra so am
				data[i] = str(data[i])
				if data[i][0] == '-':
					data[i] = '~' + data[i][1:None]
				# Gan gia tri vao params
				Parameters[i-2][2] = data[i]
			# Goi ham	
			run = Intepreter(ln,Line-1)
			while run[0] == True:
				run = Intepreter(run[1],Line-1)

			# Neu gap return va tra ve gia tri run[0] == False
			# Kiem tra so am
			run[1] = str(run[1])
			if run[1][0] == '-':
				run[1] = '~' + run[1][1:None]
			setVarValue(data[0],run[1])

		elif cmdName == 'gosub':
			ln = getLabelLine(data[0])
			run = Intepreter(ln,Line-1)
			while run[0] == True:
				run = Intepreter(run[1],Line-1)
		elif cmdName == 'beep':
			print('\a')
		elif cmdName == 'time':
			os.system(r'echo The current time is %time%')
		elif cmdName == 'date':
			os.system(r'echo The current date is %date%')
		elif cmdName == 'rand':
			print(random.random())
		elif cmdName == 'xrand':
			data[0] = float(data[0])
			data[1] = float(data[1])
			print(random.random() % (data[1] - data[0] + 1) + data[0])
		elif cmdName == 'randint':
			data[0] = int(data[0])
			data[1] = int(data[1])
			print(random.randint(data[0],data[1]))
		elif cmdName == 'sys':
			os.system(data[0])
		elif cmdName == 'color':
			if data[0] == 'blue':
				os.system('color 1')
			elif data[0] == 'green':
				os.system('color 2')
			elif data[0] == 'aqua':
				os.system('color 3')
			elif data[0] == 'red':
				os.system('color 4')
			elif data[0] == 'purple':
				os.system('color 5')
			elif data[0] == 'yellow':
				os.system('color 6')
			elif data[0] == 'white':
				os.system('color 7')
			elif data[0] == 'gray':
				os.system('color 8')
			elif data[0] == 'light blue':
				os.system('color 9')
			elif data[0] == 'light green':
				os.system('color A')
			elif data[0] == 'light aqua':
				os.system('color B')
			elif data[0] == 'light red':
				os.system('color C')
			elif data[0] == 'light purple':
				os.system('color D')
			elif data[0] == 'light yellow':
				os.system('color E')
			elif data[0] == 'bright white':
				os.system('color F')

		elif cmdName == 'rem':		
			mode = data[0]
			comment = data[1]
			if mode.find('s') != -1:
				print(comment)
			if mode.find('w') != -1:
				time.sleep(0.5)
			if mode.find('b') != -1:
				input()
		elif cmdName == 'return':
			data[0] = EProcess(data[0])
			# Reset lai toan bo params
			Parameters = []
			return [False,data[0]]
		elif cmdName == 'const':
			if checkConstExisted(data[0]) == False:
				Constants.append([data[1],data[0],data[2]])

	return [False,0]


# Main function
print('\n\n!!! Welcome to MathCal Intepreter !!!\n(Nhap lenh help de biet chi tiet)\n')
os.system('color B')
while True:
	GetCommand()
	#GetCommandFromFile()
	GetAllCommand()
	PreProcess()
	print('\n==============================\nStarted Intepreter !!!\n')
	run = Intepreter(0,Line-1)
	while run[0] == True:
		run = Intepreter(run[1],Line-1)

	# Khoi tao lai toan bo gia tri
	ResetAllData()
	expProcess.Reset()
	funcProcess.Reset()
	'''print('\n')
	ans = input('>> ')
	if ans == 'exit()':
		break
	else:
		print('')'''
	print('\n!!! Intepretation finished !!!\n_______________________________\n')
os.system('color F')
