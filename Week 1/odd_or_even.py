isRunning = True

while isRunning:
	userInput = input('Sonni kiriting: ')

	if userInput == "exit":
		print('Dastur yopildi xayr!')
		isRunning = False
	else: 
		def fun(n):
			if n % 2 > 0:
				print('But toq son')
			else:
				print('Bu juft son')
		fun(int(userInput))