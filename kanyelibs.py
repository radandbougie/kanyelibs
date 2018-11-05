
import time
import string
import sys
import random

'''
Prompts the user for inputs
Example:Noun,Verb,Adjective
Then once the information has been inputted,
output a premade story
Psudeocode:
char1 gives some input, store that in a variable
char2 gives some input, store that in a variable
the user is prompted for a setting, we store that
the user is prompted for a verb, we store that
After this we output the story with the user's input
'''
colors = {
    "startGreen": '\x1b[6;30;42m',
    "endGreen": '\x1b[0m',
    "startBlue": '\033[34m',
    "endBlue": '\033[0m',
}


def print_start(number=0):
    print("Kanyelibs story #{} started\n".format(
        number) + colors["startGreen"] + "=" * 20 + colors["endGreen"])


def print_end():
    """Prints when Kanyelibs end"""
    print(colors["startBlue"] +
          "MADLIBS HAS ENDED!  " + colors["endBlue"])
    run_it = input('DO YOU WANT TO PLAY AGAIN? +  (Y or N): '.lower())
    if run_it == 'y':
        time.sleep(1)
        main()
    else:
        print('K!!! Bye!')


def mad_lib_game1():
    print('{} is dead. {} is dead. Walt Disney is {}. Name somebody {}. My greatest {} is that Ill never be able to see myself perform {} live.'.format(
        input('Enter a name: '), input(
            'Enter another name: '), input('Enter a verb(past tense): '), input('Enter a verb (past tense): '), input('Enter a noun: '), input('Enter a Kanye Song name: ')))


def mad_lib_game2():
    pronoun = input('Enter a pronoun: ')
    noun = input('Enter another noun: ')
    pronoun = input("Enter a pronoun(place): ")
    noun = int(input("Enter a noun(food): "))
    time.sleep(1)
    print("I am a {}, Hurry up with my damn {}, in a {} restaurant, hurry up with my damn {}".format(
        name, noun, pronoun, noun, noun))



def askUser():

    answer = int(input(
        'Which Kanyelib game would you like to play? Choose from story: [1] [2]: '))
    return answer


def main():
    answer = askUser()
    print_start(answer)
    if answer == 1:
        mad_lib_game1()
    elif answer == 2:
        mad_lib_game2()
    else:
        print('Error')
    print_end()


def test():
    mad_lib_game1()
    mad_lib_game2()



test()


if __name__ == '__main__':
    main()
