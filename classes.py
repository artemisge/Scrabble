import random
import itertools


class SakClass:
    letters = {
        "Α": [12, 1],
        "Β": [1, 8],
        "Γ": [2, 4],
        "Δ": [2, 4],
        "Ε": [8, 1],
        "Ζ": [1, 10],
        "Η": [7, 1],
        "Θ": [1, 10],
        "Ι": [8, 1],
        "Κ": [4, 2],
        "Λ": [3, 3],
        "Μ": [3, 3],
        "Ν": [6, 1],
        "Ξ": [1, 10],
        "Ο": [9, 1],
        "Π": [4, 2],
        "Ρ": [5, 2],
        "Σ": [7, 1],
        "Τ": [8, 1],
        "Υ": [4, 2],
        "Φ": [1, 8],
        "Χ": [1, 8],
        "Ψ": [1, 10],
        "Ω": [3, 3]
    }

    def __init__(self):
        self.sak = []
        for letter in self.letters:
            n = self.letters[letter][0]
            for i in range(n):
                self.sak.append(letter)
        self.randomize_sak()

    def randomize_sak(self):
        random.shuffle(self.sak)
        pass

    def getletters():
        pass

    def putbackletters():
        pass

    def printsak(self):
        print(self.sak)

    def getwordvalue(self, word):
        value = 0
        for letter in word:
            value += self.letters[letter][1]
        return value


class Player:
    def __init__(self) -> None:
        self.acceptedWords = self.getAcceptedWords()
        pass

    def __repr__(self) -> str:
        pass

    def getAcceptedWords(self):
        # returns dictionary with all accepted words
        words = {}
        file = open('greek7.txt', 'r')
        Lines = file.readlines()
        for line in Lines:
            line2 = line.strip()
            words[line2] = ''
        return words

    def isWordAccepted(self, word):
        return word in self.acceptedWords


class Human(Player):
    def __init__(self) -> None:
        super().__init__()

    def play():
        pass


class Computer(Player):
    def __init__(self) -> None:
        super().__init__()

    def play(self, letters, mode):
        # letters: available letters
        # mode: MIN, MAX, SMART
        words = list(self.getPermutations(letters))
        if (mode == "MIN"):
            for w in words:
                if (super().isWordAccepted(w)):
                    return w
            return # return nothing if no word is found
        if (mode == "MAX"):
            for w in reversed(words):
                if (super().isWordAccepted(w)):
                    return w
            return
        else:
            value = 0
            for w in words:
                if (super().isWordAccepted(w)):
                    newvalue = SakClass.getwordvalue(w)
                    if (value < newvalue):
                        value = newvalue
                        finalword = w
            return finalword

    def getPermutations(letters):
        perms = []
        for i in range(2, 8):
            perms += itertools.permutations(letters, i)
        return perms


class Game:
    def __init__(self):
        self.settings = "ΜΙΝ"
        pass

    def __repr__(self) -> str:
        pass

    def setup(self):
        self.sak = SakClass()
        self.player = Player()
        self.computer = Computer()
        self.moves = 0  # total moves in this game
        self.computerScore = 0
        self.playerScore = 0
        pass

    def run(self):
        while (1 == 1):
            # run game till end condition
            pass

        self.end()

    def end(self):
        # save in json
        pass

    def changeSettings(self):
        userinput = input("""___ΡΥΘΜΙΣΕΙΣ___
Ο υπολογιστής θα παίξει:
1) ΜΙΝ: την πρώτη μικρότερη λέξη που θα βρει
2) ΜΑΧ: την πρώτη μεγαλύτερη λέξη που θα βρει
3) SMART: την λέξη με τους περισσότερους πόντους
Πληκτρολόγησε 1, 2 ή 3
>>> """)
        if (userinput == '1'):
            self.settings = "MIN"
        elif (userinput == '2'):
            self.settings = "MAX"
        elif (userinput == '3'):
            self.settings = "SMART"
        else:
            print("Αυτή η επιλογή δεν υπάρχει. Οι ρυθμίσεις δεν θα αλλάξουν και θα επιστρέψετε στο κυρίως μενού.")
        print(self.settings)

    def menu(self):
        userinput = input("""~~~~ SCRABBLE ~~~~
------------------
1: Σκορ
2: Ρυθμίσεις
3: Παιχνίδι
q: Έξοδος
------------------
>>> """)
        if (userinput == '1'):
            #printScore()
            pass
        elif (userinput == '2'):
            self.changeSettings()
        elif (userinput == '3'):
            #run
            pass
        elif (userinput == 'q'):
            #end()
            pass
        else:
            pass
