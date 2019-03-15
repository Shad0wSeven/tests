#!/usr/bin/env python 3
'''      __
         __]
 \\  // [__
  \\//
  //\\
 //  \\
 '''
#information for DEVS

#Conventions whithin this particular program!!! AKA Commented Tags
'''
COMMENTED TAGS (use ctrl + f to find)

    #CHANGE
        ^^^ this means that change this command while updating, use this command to mark commands
        that may need their contents updated to make sense with further updates
        remove tag, ONLY if revisions will not be needed in the forseeable future


    #PLACEHOLDER
        ^^^ this means that this is purely a placeholder for the future, safely change the name
        then safely remove

    #ERR: [Reason]
        ^^^ this means that this block of code is causing an error
        when flagged, focus on clearing errors

    #INCREMENTAL
        ^^^ error blocking code, this means that do not change this code, because otherwise errors will be caused
        can be used to
    #NULL
        ^^^ used for code that is not run NOT NULLS!!!!
    #REVIEW
        ^^^ used for code that is flagged for review
    #AUTORUN
        ^^^ code that is automatically run, use #AUTORUN[END] to specify end of Autorun
    #SP
        ^^^ means that you dont know how to spel stuf, if  ur revweing than mke shure tu fics speling erors thancs! :)
    #$
        ^^^ means that for especiallly long codeblocks, this is how many lines the code spans (ALWAYS subject to change)
'''
'''
CODE CONVENTIONS

    ¯\_(ツ)_/¯ For errors
    ( ͡° ͜ʖ ͡°) For sneaky statements or eastereggs
    ಠ_ಠ for security execptions
    (╯°□°）╯︵ ┻━┻ when something goes wrong
    o_O hmmm thinking

'''

#   START
#   OF
#   THE
#   CODE
#   !!!!!!!!!!!!!!!





#AUTORUN
# $47
# Welcome statement
print('Welcome to the DOS')
print('Loading . . .')

''' INITIAlIZATION'''
# import statements
import random
import time
import sys

'''
||||||||     |||||||    |||||||     \\  //
||      ||  ||     ||  ||            \\//
||      ||  ||     ||   ||||||       //\\
||      ||  ||     ||        ||     //  \\
||||||||     |||||||   |||||||

By X^2
v1.0
'''
#additinol initialiazation
'''The version name must be changed with different version distros'''
version = '0.1.0' #REVIEW :this code should work as an int value, but string is required due to x.x.x format

'''END OF INITIAlIZATION'''
    #AUTORUN [END]

#startupanimation

ifs = 0

def startup():
    if ifs == 0: #ERR: [This is triggering an error in Terminal, supposedly naming it as a local variable, if global is inputted, a syntax error is outputted]
        print('Successfully imported!') # import sucessful

        #Startup animation
        print('||||||||     |||||||    |||||||')
        time.sleep(0.1)
        print('||      ||  ||     ||  ||')
        time.sleep(0.1)
        print('||      ||  ||     ||   |||||| ')
        time.sleep(0.1)
        print('||      ||  ||     ||        ||')
        time.sleep(0.1)
        print('||||||||     |||||||   |||||||       X')
        time.sleep(0.3)

        print('XDOS v', version, 'Alpha')      # name
        print('By X-Squared Studios')   # credits
        ifs = 1
    elif ifs != 0:
        print('System already started up!!!!!')
        print('Try dosx ( ͡° ͜ʖ ͡°)')
    else:
        print('something went wrong ¯\_(ツ)_/¯')

startup()
print('Remember this is Python, so use Function Name() instead of just Function name to run commands\n')
#start of command defenition





#eastereggs
def dosx():
        '''Prints the DOS Logo as well as version :)'''
        print('||||||||     |||||||    |||||||')
        time.sleep(0.1)
        print('||      ||  ||     ||  ||')
        time.sleep(0.1)
        print('||      ||  ||     ||   |||||| ')
        time.sleep(0.1)
        print('||      ||  ||     ||        ||')
        time.sleep(0.1)
        print('||||||||     |||||||   |||||||')
        time.sleep(0.3)
        print('version', version)


def ayush():
        '''the real credits'''
        print('realcredits') #this is pretty cool
        print('Ayush Nayak in 2019')
        print('Not designed by apple in california')
        print('and not hermes in paris either')
        print('but by somebodys fingers in a room with a desk and keyboard and mouse :)')

#commands start yay

#control commands
def shutdown():
    sys.exit('User Exited')


def help():
    print('Use directory() to see list of functions,\n for more advanced help, look up DOSX or play with the code.')


def directory():  #$ ~70 Lines
    '''prints all commands excepts the eastereggs :)'''
    #organized the same way as the codebody
    print('Select one of the function directories: \n',
    '[1] Control Commands\n',
    '[2] Storage Commands\n',
    '[3] Help Commands\n',
    '[4] Cool Commands\n', #PLACEHOLDER
    '[5] Even Cooler Commands\n',#PLACEHOLDER
    '[6] Developer Commands\n',
    '[7] Very Very Cool Commands\n') #PLACEHOLDER


    selection = input('Select the Function Directoty: ')
    if selection == '1':
        print('List of Control Commands\n',
        'shutdown(): Exits the code\n',
        'directory(): Displays the Directory, although if you are here already, you should know that :)\n',
        'viewfiles(): Displays all of the available files on this system \n',
        )
    selection = input('Select the Function Directoty: ')
    if selection == '2':
        print('List of Control Commands\n', #PLACEHOLDER
        'shutdown(): Exits the code\n', #PLACEHOLDER
        'directory(): Displays the Directory, although if you are here already, you should know that :)\n',#PLACEHOLDER
        'viewfiles(): Displays all of the available files on this system \n',#PLACEHOLDER
        )
    selection = input('Select the Function Directoty: ')
    if selection == '3':
        print('List of Control Commands\n',#PLACEHOLDER
        'shutdown(): Exits the code\n',#PLACEHOLDER
        'directory(): Displays the Directory, although if you are here already, you should know that :)\n',#PLACEHOLDER
        'viewfiles(): Displays all of the available files on this system \n',#PLACEHOLDER
        )
    selection = input('Select the Function Directoty: ')
    if selection == '4':
        print('List of Control Commands\n',#PLACEHOLDER
        'shutdown(): Exits the code\n',#PLACEHOLDER
        'directory(): Displays the Directory, although if you are here already, you should know that :)\n',#PLACEHOLDER
        'viewfiles(): Displays all of the available files on this system \n',#PLACEHOLDER
        )
    selection = input('Select the Function Directoty: ')
    if selection == '5':
        print('List of Control Commands\n',#PLACEHOLDER
        'shutdown(): Exits the code\n',#PLACEHOLDER
        'directory(): Displays the Directory, although if you are here already, you should know that :)\n',#PLACEHOLDER
        'viewfiles(): Displays all of the available files on this system \n',#PLACEHOLDER
        )
    selection = input('Select the Function Directoty: ')
    if selection == '6':
        print('List of Control Commands\n',#PLACEHOLDER
        'shutdown(): Exits the code\n',#PLACEHOLDER
        'directory(): Displays the Directory, although if you are here already, you should know that :)\n',#PLACEHOLDER
        'viewfiles(): Displays all of the available files on this system \n',#PLACEHOLDER
        )
    selection = input('Select the Function Directoty: ')
    if selection == '7':
        print('List of Control Commands\n',#PLACEHOLDER
        'shutdown(): Exits the code\n',#PLACEHOLDER
        'directory(): Displays the Directory, although if you are here already, you should know that :)\n',#PLACEHOLDER
        'viewfiles(): Displays all of the available files on this system \n',#PLACEHOLDER
        )

    else: print('Please enter a number from 1 -> 7')#CHANGE
