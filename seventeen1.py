"""The program should allow a human to play against a computer. 
The human always goes first. If the human enters incorrect 
input (anything other than 1, 2, 3, or a number larger than 
	the number of marbles remaining in the jar), an error 
message should be displayed, and the human is prompted to try again.

The computer player can choose to remove marbles
 according to any strategy of your choosing. Some examples 
 include: (i) always choose the same number as the human player, 
 (ii) choose randomly. Note that it is possible, though not 
 required for this exam, to devise a straightforward strategy
  for the computer such that it will never lose, as long as 
  the human player goes first.

At the end of each turn, the program should print 
out the number of marbles removed in the previous 
turn, and the number of marbles that remain in the
 jar. Once there are no more marbles in the jar,
  the program should declare the winner of the game."""
import random

def marble_game():
	print("\nLet's play the game of Seventeen!")
	marbles_left = 17
	print("Number of marbles left in jar: {} \n".format(marbles_left))
	#continue till no more marbles left in jar
	while marbles_left > 0:
		#get the marbles removed by human
		marbles_left -= human_turn(marbles_left)
		# print number of marbles remaining
		print("Number of marbles left in jar: {}\n".format(marbles_left))
		#check if game is over
		check_jar(marbles_left, "You")
		#get the marbles removed by computer
		marbles_left -= comp_turn(marbles_left)
		# print number of marbles remaining
		print("Number of marbles left in jar: {}\n".format(marbles_left))
		#check if game is over
		check_jar(marbles_left, "Computer")

def check_jar(marbles, player):
	# no more marbles - display winner
	if(marbles == 0):
		print("There are no marbles left. {} wins!".format(player))
		quit()
	else:
		return

def human_turn(marbles):
	try:
	#get input from user
		human_marble = int(input("Your turn: How many marbles will you remove (1-3)? "))
	
	#display error message and prompt again
	except:#exception for non-integer
		print("Sorry, that is not a valid option. Try again!")
		print("Number of marbles left in jar: {}\n".format(marbles))
		return human_turn(marbles)
	else:#error for invalid values - restrict to 1,2,3 or number larger than remaining
		if((human_marble > 3) or (human_marble <= 0) or (human_marble > marbles)):
			print("Sorry, that is not a valid option. Try again!")
			print("Number of marbles left in jar: {}\n".format(marbles))
			return human_turn(marbles)
		else:
			#at end of turn, print number of marbles removed
			print("You removed {} marbles".format(human_marble))
			return human_marble


def comp_turn(marbles):
	print("Computer's turn...")
	#strategy to remove marbles
	#2. choose randomly
	comp_marble = random.randint(1,3)
	#if the random number is more than that left in jar
	if(comp_marble > marbles):
		comp_marble = marbles
	#at end of turn, print number of marbles removed
	print("Computer removed {} marbles.".format(comp_marble))
	return comp_marble


def main():
	marble_game()

if __name__ == '__main__':
	main()