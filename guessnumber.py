import random

savedNumber = random.randint(1, 100)

numberOfSteps = 0

while (True):
	userGuess = input("Please guess a number in range from 1 to 100")
	if(savedNumber == int(userGuess)):
		print(f"You are the winner! after {numberOfSteps} steps ")
		break
	elif(savedNumber >int(userGuess)):
		print("The number is too small")
		numberOfSteps = numberOfSteps + 1
	else:
		print("The number is too high")
		numberOfSteps = numberOfSteps + 1
print("Goodbye")
