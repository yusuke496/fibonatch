def Fib(n):
	if n ==0:
		return 0
	elif  n==1:
		return 1
	else:
		return Fib(n-1)+Fib(n-2)

for i in range(1,35):
	print(i,Fib(i))
else:
	pass
