import os # To use the type command and easily display a text file's contents

def menu_display():	
	print ("Please enter the number corresponding to the menu option you want to choose:")
	print ("\t1) Instructions")
	print ("\t2) Blah")
	print ("\t3) Blah")
	print ("\t4) Blah")
	print ("\t5) Blah")
	print ("\t6) Quit")

print ("BULK EMAILING PROGRAM\n---------------")

# Take an integer as a menu choice
while True:
	menu_display()
	menu_choice = int(input())

	if menu_choice == 1:
		os.system("type instructions.txt")

	elif menu_choice == 2:
		pass

	elif menu_choice == 3:
		pass

	elif menu_choice == 4:
		pass

	elif menu_choice == 5:
		pass

	elif menu_choice == 6:
		exit()

	else:
		print("Invalid choice.")

