"""
After you have Version 1 working, you can proceed to implement
 Version 2, which plays the Seventeen Game in batch mode.
The program reads from an input file (named 'i206_placein_input.txt')
 a sequence of comma delimited numbers representing the sequence of 
 moves made by Player 1. Each line of the input file represents a
  different game. For example, the sample input file contains data
   for ten games. In the first game, Player 1 removes 3 marbles 
   during its first turn, 1 marble during its second turn, 
   three marbles during its third turn, and so on.

If the number of marbles left in the jar is fewer than the
 next number in the play sequence, then Player 1 should remove
  all the remaining marbles. For example, if there are two marbles
   left in the jar, and the next number in the sequence is 3, then
    Player 1 should remove two marbles, not three.
Player 2 will play the same marble-removal strategy as in Version 1.

Note that not all numbers in each line may be used, depending 
on the progress of the game (which in turn depends on the strategy 
used by Player 2). Conversely, the play sequences are generated 
such that there will always be enough numbers for each game.

The program will play the game as many times as there are
 lines in the input file, printing the sequence of moves 
 and the game winner into an output text file
  (named i206_placein_output2_<ischool_userid>.txt'),
   one line per game. At the end of all the games, 
   the program will print the number of games won by each player.
    See below for what an output file for ten games might look like.
"""
import random
import sys

def file_input():
	#read the file and return each list
	with open(sys.argv[1],"r") as human_play:
		human_num = []
		for lines in human_play:
			human_num += lines.split()
	return human_num

def play_game():
	game_counter = 0#counter to count number of games
	win_ct_p1 = 0#counter for player 1 winning
	win_ct_p2 = 0#counter for player 2 winning
	human_num = file_input() # read the file
	with open("i206_placein_output2_niavivek.txt","w") as write_file:
		for values in human_num: # iterate the list
			game_counter += 1
			play_1 = values.split(",") # split the numbers
			marbles_left = 17
			idx = 0 #index for each number in list
			while marbles_left > 0: # iterate the numbers in the list till no more marbles left
				#display when starting the game for each list
				if idx == 0:
					write_file.write("Game #{}. Play sequence: ".format(game_counter))
				#get number removed by player 1
				marb_play1_rem = play1_turn(marbles_left,play_1[idx])
				marbles_left -= marb_play1_rem
				#display the number removed
				if idx == 0:
					write_file.write(str(marb_play1_rem))
				else:
					write_file.write("-"+str(marb_play1_rem))
			
				idx += 1
				#check if game is over
				if(check_jar(marbles_left)):
					write_file.write(". Winner: P1" +"\n")
					win_ct_p1 += 1
					break
				#player 2 turn- get marbles removed
				marb_play2_rem = play2_turn(marbles_left)
				marbles_left -= marb_play2_rem
				write_file.write("-"+str(marb_play2_rem))
				#check if game is over
				if(check_jar(marbles_left)):
					write_file.write(". Winner: P2"+"\n")
					win_ct_p2 += 1
					break
		#print stats
		write_file.write("Player 1 won {} times; Player 2 won {} times.".format(win_ct_p1,win_ct_p2))

def check_jar(marbles):
	# no more marbles - display winner
	if(marbles == 0):
		return True
	else:
		return False

def play1_turn(marbles,num):
	# get marble removed from value in file

	play1_marble = int(num)
	#if value is more than that in jar, change the value to the number left in jar
	if(play1_marble > marbles):
		play1_marble = marbles
	return play1_marble


def play2_turn(marbles):
	#strategy to remove marbles
	#2. choose randomly
	play2_marble = random.randint(1,3)
	#if the random number is more than that left in jar
	if(play2_marble > marbles):
		play2_marble = marbles
	return play2_marble


def main():
	play_game()

if __name__ == '__main__':
	main()