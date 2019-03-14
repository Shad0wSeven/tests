#!/usr/bin/env python 3

'''      __
         __]
 \\  // [__
  \\//
  //\\
 //  \\  DEVELOPMENT TEAM
 '''


# import statements
import time
import sys
import random



#Function Defenitions


def signin():
	'''
	A program made to simulate signing in

	'''
	#start of signin()
	print('Hello')
	time.sleep(0.5)
	print('Welcome to the System') #welcome message
	time.sleep(0.5)
	print('Please Enter Your Username')
	user = input('Username: ')
	time.sleep(0.3)
	reg = {} # initialize users/passwords dictionary
	# user initinilization in form red['username'] = 'password'
	reg['ayush'] = 'asdf'
	reg['god'] = 'asdfasdf'
	reg['asdf'] = 'asdfasdfasdf'
	if user in reg:
		print(user + ' Welcome to the System!')
	else:
		sys.exit('Sorry Your Username is not Registered With this System!')
	# Now for the passcode
	time.sleep(0.3)
	print(user + ' Please Enter Your Passcode')
	passcode = input('Passcode: ')
	if reg[user] == passcode:
		print('Welcome to the system ' + user + '!')
		time.sleep(2)
		print('Loading')
		y = 0
		while y < 10:
			time.sleep(0.2)
			print('.')
			y += 1
		print('All content successfully Loaded!')
		# Now here input the code that will add multiuser suppourt, although it will be copy pasted :(

	else:
		sys.exit("Sorry Your Credentials don't match")


def printitem(items):
	for item in items:
		print(item)


def main():
	signin()


def calculator1():
	'''
	Kind of a bulky calculator, but its fun, and thats what matters!

	'''
	print('Welcome to the calculator')
	print('Please input your first number')
	firstnum = int(input('First Number Here: '))
	print('Nice now print an Operator!')
	op = input('Operator (/ * - +): ')
	if op == '/' or '*' or '-' or '+':
		print('Great now print your second number!')
		secondnum = int(input('Second Number: '))
		if op == '/':
			ans =  firstnum /secondnum
		elif op == '*':
			ans = firstnum * secondnum
		elif op == '+':
			ans = firstnum + secondnum
		elif op == '-':
			ans = firstnum - secondnum
		else:
			sys.exit('Please enter an Operator such as: /, *, -, +! Remember not to use spaces')

	answer = str(ans)
	print('The answer is: ' + answer)


def calculator2(ins):
	''' This Code does not really work right now, all lines are erronous'''
	inp = str(ins)
	pars = inp.split(' ')
	#parone  = int(pars[0])
	print(pars)
	'''	partwo = int(pars[2])
	operone = par[1]
	if operone == '/':
		ans = parone / partwo
	elif operone == '*':
		ans = parone * partwo
	elif operone == '+':
		ans = parone + partwo
	elif operone == '-':
		ans = Sparone - partwo
	else: print('Please format as x * y for example with spaces between numberes!')
	print(ans)

	'''


def dice():
	'''this is a project that just outputs a random integer :)'''
	print('Rolling a dice . . . ')
	time.sleep(0.2)
	diceint = random.randint(1,6)
	print('Your dice roll solution is:', diceint)


def guess():
	'''
	Creates a program to guess a number based on different bounds, and a system of variables to help have rudimentary fun.
	'''
	int1 = int(input('Input your lower bound: ')) #initialize first bound
	if type(int1) != int: #to catch errors NOTES: DOES NOT CURRENTLY WORK!!!!
		print('Please enter a number!!!!!!!')
		guess()
	int2 = int(input('Great! Now input your upper bound: ')) #initialize second bound
	if type(int2) != int: #to catch errors NOTES: DOES NOT CURRENTLY WORK!!!!
		print('Please enter a number!!!!!!!')
		guess()
	print('Generating a random number . . . ')
	time.sleep(0.3)
	thenum = random.randint(int1, int2) #generate variable that stores already defined variables
	print('Okay, this is optinol. If you want to set a number of guesses,\n type "yes", (the default is 5 guesses before the answer is revealed)')#if you want a different guess limit
	yesno = input(':') #check if user wants
	if yesno == 'yes':
		print('Okay, you can now print your maximum number of guesses\n (the larger the range, the higher the guesses should be)')
		guesslimit = int(input(':')) #execute if user wants
	else:
		guesslimit = 5
	correct = 0
	attempts = 0
	while correct == 0:
		myinput = int(input('Guess a number:'))
		if type(myinput) != int: #to catch errors in input NOTES: DOES NOT CURRENTLY WORK!!!!
			print('Please enter a number!!!!!!!')
			guess()
		if myinput == thenum: #for correct guesses
			print('Great! You guessed the number:', thenum, 'correctly in', attempts, 'attempts!' )
			correct = 1
			break
		elif myinput != thenum and attempts < 5: #incorrect guesses
			print('Sorry! Incorrect!') #warmercolder
			warmcoldraw = thenum - myinput
			warmcold = abs(warmcoldraw)
			if warmcold > 0 and warmcold < 5:
				warmcoldout = 'Scalding!'
			elif warmcold > 5 and warmcold < 10:
				warmcoldout = 'Hot!'
			elif warmcold > 10 and warmcold < 15:
				warmcoldout = 'Warm!'
			elif warmcold > 15 and warmcold < 20:
				warmcoldout = 'Cold!'
			elif warmcold > 25 and warmcold < 40:
				warmcoldout = 'Freezing!'
			elif warmcold > 40 and warmcold < 70:
				warmcoldout = 'Below Freezing!'
			elif warmcold > 70:
				warmcoldout = 'Absolute Zero!'
			else:
				print('Unknown Error, exiting!')
				break
			print('You are:', warmcoldout)
			attempts += 1
		elif myinput != thenum and attempts == guesslimit:
			print('Sorry, You have guessed wrong 5 times, the answer was:', thenum)


def madlibs():
	'''Creates a story!'''
	#Here is the story it will create!!!
	'''
	Jimmy decided to go down to the store. He really needed some new pencils. All his older ones had broken. He thought, how can I
	'''

def hangman():
    '''fun hangman game!
    '''
    print('Generating Word . . . ')
    wordbank = [ 'Hello', 'America', 'Finally', 'Someone', 'Somebody', 'Therefore', 'Terminal', 'Activity', 'Exuberant', 'Execute', 'Enlighten', 'Entertaining', 'Settings', 'Messages','Reminding', 'Epic', 'Night', 'Fortnight', 'Seven',
    'Fifteen', 'Ending', 'Application', 'Musically', 'Centegrade', 'Centimeter', 'Meter', 'Launchpad', 'Rocket', 'Car','Lamborghini', 'Notes', 'Notebook', 'Addition', 'Multiplication', 'Photography',
    'Science', 'Astronomy', 'Asteroid', 'Universe', 'Ending'] #Currently 40 long, so 39 for the random function

    lengthwordbank = len(wordbank)
    answerword = wordbank[random.randint(0, lengthwordbank)] #generates word
    charactercount = list(answerword) #splits words into characters

    time.sleep(0.5)
    print('Word Generated!')
    correct = 0

    while correct == 0:
        print('Directions: guess a Letter, or word. After 6 Incorrect Guesses, the word will be revealed!')
        rawguess0 = input('Your Guess: ')
        rawguess1 = strip.rawguess0
        rawguesslen = len(rawguess1)
        #Validility Checker
        if rawguess len == 1:
            guess = rawguess1.lower()
        elif rawguess len < 1:
            print('Please Enter one character, like "A"')
        else:
            print('Unknown Error, Restarting')
        #Answerchecker
        if guess in charactercount:
            #Correct
            '''
            What Needs to be Done:
            Add placment such as __a__a print , also check if the entire word is complete, remove from charactercount or add message that it has already been inputted
            add to a list of letters tried, (Right and wrong)
            '''
        elif guess not in charactercount:
            #Incorrect
            '''
            What Needs to be Done:
            Add error message, add such as 'Head, Right Arm', for the hangman thing, also make sure to add to a list, so one can know what they have already entered,
            make sure to count errors,
            if errors at 6, then reveal answer
            '''
        else:
            print('Weird Error')


if __name__ == '__main__':
	main()


print('Successfully imported!') # import sucessful
print('Test Enviroment Toolkit v0.1.0')   # name
print('By X-Squared Studios')   # credits
print('         __')
print('         __]')
print(' \\\\  // [__')
print('  \\\\//')
print('  //\\\\')
print(' //  \\\\')
