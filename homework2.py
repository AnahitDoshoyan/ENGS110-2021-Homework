def fibonacciSum (N):
	f1 = 0
	f2 = 1
	sum = 0
	while (f2 < N):
		sum = sum + f2
		fn = f1 + f2
		f1 = f2
		f2 = fn
	print (sum)

def prime (N):
	if N > 1:
		for i in range(2,N):  
			if (N % i) == 0:
				print(N,"is not a prime number")  
				print(i,"times",N//i,"is",N)  
				break
		else:
			print(N,"is a prime number")  
	else:
		print(N,"is not a prime number")

def ToBinary (N):
	if N >= 1:
		ToBinary (N // 2)
		print(N % 2, end='')

def main():
	n = int(input("Please insert your age"))
	fibonacciSum (n)
	prime (n)
	ToBinary (n)
	print('\n')
	print("Have a nice day")

main()
