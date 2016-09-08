from sys import exit


def right_hallway():
	print "There are 10 rooms."
	print "Half the rooms are filled with hungry lions." 
	print "The other half is filled with a millon dollars."
	print "Which room do you choose?" 
	 
	choice = raw_input("> ")
	
	if "1" in choice or "3" in choice or "5" in choice or "7" in choice or "9" in choice:
		print "You get a million dollars!"
		print "Do you want to play again?"
		
		decision = raw_input("> ")
		
		if "yes" in decision:
			start()
		elif "no" in decision:
			dead("Thanks for playing!")
		else:
			dead("I guess you don't want to play.")
	
	elif "2" in choice or "4" in choice or "6" in choice or "8" in choice or "10" in choice:
		print "You get torn apart by the lions!"
		print "Do you want to try again?"
		
		decision = raw_input("> ")
		
		if "yes" in decision:
			start()
		elif "no" in decision:
			dead("Thanks for playing!")
		else:
			dead("I guess you don't want to play.")
		
	else: 
		dead("You fall into limbo for not choosing a door.")
		
		
def left_hallway():
	print "There are 10 rooms."
	print "One room is the gate to heaven."
	print "The other nine rooms are gates to hell."
	print "Which room do you choose?"
	
	choice = raw_input("> ")
	
	if "1" in choice or "2" in choice or "3" in choice or "4" in choice or "5" in choice or "6" in choice or "8" in choice or "9" in choice or "10" in choice:
		print "You open the door and enter through the gates of hell."
		print "Do you want to play again?"
			
		decision = raw_input("> ")
		
		if "yes" in decision:
			start()
		elif "no" in decision:
			dead("Thanks for playing!")
		else:
			dead("I guess you don't want to play.")

	elif "7" in choice:
		print "You open the door and walk through the pearly gates of heaven."
		print "Do you want to play again?"	
		
		decision = raw_input("> ")
		
		if "yes" in decision:
			start()
		elif "no" in decision:
			dead("Thanks for playing!")
		else:
			dead("I guess you don't want to play.")
	else:
		dead("You can't decide, so you got trapped in purgatory.")
		
		
def dead(why):
	print why, "Good job!"
	exit(0)
		
def start():
	print "There are two hallways."
	print "A left hallway and a right hallway."
	print "Which hallway do you choose?"
	
	choice = raw_input("> ")
	
	if choice == "left":
		left_hallway()
	elif choice == "right":
		right_hallway()
	else:
		start()
		
		
start()
		

