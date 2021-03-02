#hangman in oop :(
from os import system, name
from english_words import english_words_lower_set
import random
#import

global word
class gallows():

    def parts(self):
        hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
        return hangmanpics


    def builder():
        pass


class wordpicker():

    def word(self):
        global word
        word = input("your hangsman word plz ?: ")
        return word

    def word2(self):
        global word
        word = random.sample(list(english_words_lower_set),1)
        return word


class gamemain():

    def countererrors(self,errors):
        if errors == 1:
            print(call1.parts()[1])
            print("you got 1 wrong")
        elif errors == 2:
            print(call1.parts()[2])
            print("1 more is 2 wrong")
        elif errors == 3:
            print(call1.parts()[3])
            print("oooh 1 more now is 3 wrong")
        elif errors == 4:
            print(call1.parts()[4])
            print("no no 1 more 4 wrong")
        elif errors == 5:
            print(call1.parts()[5])
            print("now is 5 wrong")
        elif errors == 6:
            print(call1.parts()[6])
            print("ooh no 6 wrong")

    def listtostring(self,s):
        guessword = ''
        return (guessword.join(s))


    def clear(self):
        if name == "nt":
            _ = system("cls")


    def guessing(self,word):

        self.clear()
        print(call1.parts()[0])
        errors = 0
        totalgos = 6
        gos = 0
        listword = []
        for char in word:
            listword.append("_")
        print(self.listtostring(listword))
        while gos < totalgos :
            guess = input("your guess plz: ")
            for index,char in enumerate(word):
                if char != guess:
                    errors += 1
                    self.countererrors(errors)
                    gos += 1
                    print (gos)
                    break

                elif char == guess:
                    listword[index] = guess

            print(self.listtostring(listword))

class starthang():

    def gamepicker():
        test1 = wordpicker()
        run = gamemain()
        print("if you want a 1 player game type 1")
        print("if you want a 2 player game type 2")
        gamepickt = int(input(":"))
        if gamepickt == 1:

            word = test1.word2()
            run.guessing(test1.word2())
        elif gamepickt == 2:

            run.guessing(test1.word())

call1= gallows()
starthang.gamepicker()
