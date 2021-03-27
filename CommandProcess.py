
class CmdProcess():
	
	def __init__(self):
		pass

	def GetParams(self,exp,data):
		token = exp.find(',')
		if token == -1:
			data.append(exp)
		else:
			sub = exp
			while token != -1:
				data.append(sub[0:token])
				sub = sub[token+1:None]

				token = sub.find(',')
			data.append(sub)