import random
import csv
'''

This tests the airplane seat model

1. First person sits in the wrong seat. Person sits in their seat if it's available. Sits in a random seat. 
2. Less people than plane


Future tests
1. When passengers are less than seats
2. Add in likely hood for passengers to show update
3. Passenger Preferential seats if their is taken 

'''


def run_simulation():
	iterations = 1
	#lets run an iteration 10,000 times.
	while iterations <= 100000:
		print("Iterations: "+str(iterations))
		number_of_seats = 10
		while number_of_seats <= 1000:
			#this is just declaring a variable
			got_seat = False
			#an array of the seats taken
			seat_taken = []
			#the number of passengers
			passengers = range(1,number_of_seats+1)
			#need a list of seats equal to the number of passengers
			seats = range(1,number_of_seats+1)
			#randomize the seats
			random.shuffle(seats)
			#zip into dictionary
			flight = zip(passengers,seats)
			#our dictionary of passengers and their seats
			seat_dictionary = dict(flight)
			#first passenger selects a seat at random.
			k = 0
			#delcaring a k for only the first passenger. He's a jerk and sits in a random seat
			#lets run this for all passengers
			for passenger in passengers:
				if k == 0:
					#A random seat
					seat_sat = random.choice(seats)
					#add it to the seat_taken array
					seat_taken.append(seat_sat)
					#remove it from the seats array
					seats.remove(seat_sat)
					#don't want to do this for any other passenger
					k = k + 1
				else:
					#hi, passenger what's your assigned seat
					assigned_seat =  seat_dictionary[passenger]
					#if their seat is taken, take someone else's seat
					if assigned_seat in seat_taken:
						seat_sat = random.choice(seats)
						#add it to seat taken
						seat_taken.append(seat_sat)
						#remove it from available seat
						seats.remove(seat_sat)
						#got_seat is false
						got_seat = False
					else:
						#Horray, no one took your seat
						seat_taken.append(assigned_seat)
						#remove it from available seats
						seats.remove(assigned_seat)
						#set got_seat true
						got_seat = True
			#write results
			#note if the last passenger has their seat it's true, if they don't have their seat it's false
			result = [iterations,number_of_seats,got_seat,seats,seat_taken,seat_dictionary]
			write_results(result)
			#increase the number of seats and the number and passengers by one
			number_of_seats = number_of_seats + 1
		#iterate again
		iterations = iterations + 1
	
def write_results(result):
	with open("path/to/file", "a") as csvfile:
		scribe = csv.writer(csvfile, delimiter = ',',quotechar = '"',lineterminator = '\n')
		scribe.writerow(result)
		
run_simulation()
