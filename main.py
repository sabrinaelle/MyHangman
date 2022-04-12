
from operator import le
import random
import pickle
from webbrowser import Galeon


class Game:

    def __init__(self, player, word):
    
        self.player = player
        self.word = word
        self.alp = "abcdefghijklmnopqrstuv"
    
    def player_name_input(self):
        pass
    

    def guesses(self, letter):
        self.alp = self.alp.replace(letter, "")
        return self.alp
        

class Word:
    
    def __init__(self, file):
        self.file = file
        self.guesses = 6
        self.updated_word = ""

    def random_word_generator(self):
        num = random.randint(0,854)
        f = open(self.file)
        words = f.readlines()
        game_word = words[num-1]
        f.close()
        return game_word
    
    # def pos_letters(self, word):
    #     length = len(game1.alp)
    #     #self.guesses = length-1
    #     return length
    
    def print_lines(self, word):
        leng = len(word)
        for i in range(leng-1):
            print("_ ", end="")
    
    def check(self,letter):
        if letter in gameword:
            length = len(game1.guesses(letter))
            print("Yes correct! Your guess will be removed from the options. You have " + str(length) + " options left. They are:")
            for let in game1.alp:
                print(let + " ", end="")
                #print(" ")
            print("\n")
            game1.guesses(letter)
            word1.word_update(letter)
        else:
            print("Uh oh! " + letter + "is not in the word!")
            print("Guesses Remaining: " + str(self.guesses-1))
    
    def word_update(self, letter):
        for i in range(len(gameword)-1):
            self.updated_word +="_ "
        for let in gameword:
            if let == letter:
                for i in self.updated_word:
                    pos = self.updated_word.index(i)
                    print(pos)

        
        

class Score:

    def __init__(self, player):
        self.player = player
    
    def player_score(self):
        player_file = "{0}file.pk{1}".format(self.player," ")
        outwrite = open(player_file, 'wb')
        #tempscore
        score = 2
        pickle.dump(score, outwrite)
        outwrite.close()
        outread = open(player_file, 'rb')
        player_score = pickle.load(outread)
        return player_score  
        


if __name__ == "__main__":
    word1 = Word("words.txt")
    game1 = Game("Sabrina",word1)
    score1 = Score(game1.player)
    gameword = word1.random_word_generator()
    print("welcome! " + game1.player)
    print(gameword)
    word1.print_lines(gameword)
    score1.player_score()
    print("You have " + str(word1.guesses) + " guesses")
    for i in range(len(gameword)):
        guess = input("What letter would you like to guess?")
        word1.check(guess)

    

    


