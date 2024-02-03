import random
import csv
'''

'''


def run_simulation():
	result = []
	iterations = 1
	#lets run an iteration 10,000 times.
	options = [1,2,3,4,5,6]
	total_rolls = 0
	while iterations <= 100000:
		print("Iterations: "+str(iterations))
		rolls = 1
		roll = random.choice(options)
		while roll != 6:
			roll = random.choice(options)
			rolls = rolls + 1
		total_rolls = total_rolls + rolls
		result.append([iterations,rolls])
		iterations = iterations + 1
	print(total_rolls/(iterations*1.0))
	
def write_results(result):
	with open("C://Users/Owner/Desktops/dice_rolls.csv", "a") as csvfile:
		scribe = csv.writer(csvfile, delimiter = ',',quotechar = '"',lineterminator = '\n')
		scribe.writerow(result)
		
run_simulation()
