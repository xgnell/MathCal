import math
import OutPut as output

op = output.Output()

def Quadratic(a,b,c):
	global op
	D = b*b-4*a*c
	if D<0:
		op.out('=> Phuong trinh vo nghiem')
	elif D == 0:
		op.out('=> Phuong trinh co nghiem kep x1 = x2 = ' + str(-b/(2*a)))
	elif D>0:
		x1 = (-b-math.sqrt(D))/(2*a)
		x2 = (-b+math.sqrt(D))/(2*a)
		op.out('=> Phuong trinh co 2 nghiem phan biet\n    => x1 = ' + str(x1) + '\n    => x2 = ' + str(x2))
	return 0

def Gcd(a,b):
	global op
	while not a == b:
		if a>=b:
			a = a-b
		else:
			b = b-a
	op.out('=> Uoc chung lon nhat: ' + str(a))
	return a

def Qr(a,b):
	global op
	a = int(a)
	b = int(b)
	t = a // b
	d = a % b
	op.out('=> Thuong: ' + str(t) + '\n   Du: ' + str(d))
	return 0

def Compact(a,b):
	global op
	x = Gcd(a,b)
	op.out('Phan so toi gian: ' + str(a/x) + '/' + str(b/x))
	return 0
