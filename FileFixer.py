
import os
import string
import turtle 

print 'This is the program for Lab 3'
repeat = 'yes'
while repeat == 'yes':
	Q = int(raw_input("""For which problem from lab  would you like to run script?\n
	1) Renaming files with Python\n 
	2) Counting words in a text document\n
	3) Replacing words in a text document\n
	4) Fun with Turtles (draw a polygon)\n
	5) Challenge Problem - word frequency\n"""))
	#------------This is the code for question 1--------------------
	while Q < 1 or Q > 5:
		Q = raw_input('Please choose between 1 and 5. ')
	
	else:
		#If user chooses question 1
		if Q == 1:
			#get the file path
			path1 = raw_input('Please type the path to the folder with the containing the Problem 1 files, without quotes.\n')
			os.chdir(path1)
			#Iterate through files
			for root, dirs, files in os.walk(path1):
				
			#make lowercase
				for fil in files:
					#make filename lowercase
					fil = fil.lower()
					#Split name and filetype
					filsec = fil.split('.')
					
					#Check if it is a .txt
					if filsec[1] == 'txt':
						
						#Rename file 
						os.rename(path1 + fil, "file_" + fil )
					
					else:
						#Rename file with filetype '.txt'
						os.rename(path1 + fil, "file_" + filsec[0] + '.txt')
			print 'Done processing problem 1...'




		#------------This is the code for question 2--------------------
		#if user chooses question 2
		elif Q == 2:
			path2 = raw_input('Please type the path to the folder containing the GIS_is_the_best.txt file, without quotes.\n')
			os.chdir(path2)
			lab_3_text = open('GIS_is_the_best.txt')
			file_list = lab_3_text.read()

			system_count, science_count, total_words = 0, 0, 0


			for word in file_list.split(' '):
			    
			    if word.lower() == 'systems':
			            system_count = system_count + 1
			    elif word.lower() == 'science':
			            science_count = science_count + 1
			    total_words += 1

			print 'Done processing problem 2...'

			print 'Total word count is: ' + str(total_words)

			print 'Total count of "system" is: ' + str(system_count)

			print 'Total count of "science" is: ' + str(science_count)

			lab_3_text.close()
			
			


		#------------This is the code for question 3--------------------
		#if the user chooses quesion 3
		elif Q == 3:
			path3 = raw_input('Please type the path to the folder containing the GIS_is_the_best.txt file, without quotes.\n')
			os.chdir(path3)
			#open file
			lab_3_text = open('GIS_is_the_best.txt', 'r')
			#open the new file
			newfile = open('Corrected_GIS_is_the_best.txt', 'w+')
			#read file
			origfile = lab_3_text.read()
			#replace science with systems
			interfile = origfile.split(' ')
			for word in interfile:
				i = int(interfile.index(word))
				if word == 'science':
					del interfile[i]
					interfile.insert(i, 'systems')
				elif word == 'Science':
					del interfile[i]
					interfile.insert(i, 'systems')
			joiner = " "
			newfile.write(joiner.join(interfile))
			lab_3_text.close()
			newfile.close()
			print 'Done processing problem 3...'




		#------------This is the code for question 4--------------------
		elif Q == 4:

			#ask how many sides for shape
			sides = int(raw_input('How many sides for this shape? '))
			#ask how long the sides should be
			length = int(raw_input('What length should the sides be? '))
			print 'Turtle Time!'
			#opens screen
			window = turtle.Screen()
			#assigns Charli as a turtle
		 	Charlie = turtle.Turtle()
		 	#calculation for Charlie's turning
		 	degrees = (180 - (180*(sides-2)/sides))
		 	#for loop for drawing circle
		 	for side in range(sides):
				Charlie.forward(length)
				Charlie.left(degrees)
			

		elif Q == 5:
			path5 = raw_input('Please type the path to the folder containing the shunned_house.txt file, without quotes.\n')
			os.chdir(path5)
			#open up the lovecraft file
			origfile = open('shunned_house.txt', 'r')
			#make a list from the words
			bads = [ '.', '\n', ',', '-', "'", ';', '[', ':', '"', ']', '_', '&', '?', '!', '\xc3', '\xa6', '*', '' ]
			interfile = origfile.read().split(' ')
			mast = {}
			for word in interfile:
				low = word.lower()
				i = int(interfile.index(word))
				if word.find('--'):
					spliword = word.split('--')
					del interfile[i]
					c = len(spliword)
					for j in range(c): 
						interfile.insert(i, spliword[c-1])
				for let in word:				
					if let in bads:
						word.replace(let, "")
				if low in mast:
					mast[low] += 1
				else:
					mast[low] = 1

			print 'Done processing problem 5...'
			print 'There are ' + str(len(mast)) + ' unique words in the text'
			print 'The word "uncle" shows up in the text ' + str(mast["uncle"]) + ' times'

			origfile.close()




	#------------This is ending and repeat code--------------------
	#reset
	repeat = raw_input('Would you like to run a script for another question in Lab 3? Answer "yes" or "no". ').lower()
	while repeat != 'yes' and repeat != 'no':
		repeat = raw_input('Please use "yes" or "no" ')

#ending text
print 'I hope you enjoyed using the script'

