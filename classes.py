import random
import itertools
import copy
import json

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

    def getletters(self, n):
        playerletters = []
        for i in range(n):
            playerletters.append(self.sak.pop())
        return playerletters

    def putbackletters(self, letters):
        for l in letters:
            self.sak.append(l)
        self.randomize_sak()

    def getwordvalue(self, word):
        value = 0
        for letter in word:
            value += self.letters[letter][1]
        return value


class Player:
    def __init__(self):
        self.acceptedWords = self.getAcceptedWords()
        self.availableLetters = []

    def __repr__(self):
        return f'Κλάση: {self.__class__}, Διαθέσιμα γράμματα: {self.availableLetters}'

    def getAcceptedWords(self):
        # returns dictionary with all accepted words
        words = set()
        file = open('greek7.txt', 'r')
        Lines = file.readlines()
        for line in Lines:
            line2 = line.strip()
            words.add(line2)
        return words

    def isWordAccepted(self, word):
        tmp = word in self.acceptedWords
        return word in self.acceptedWords


class Human(Player):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'Κλάση: {self.__class__}, Διαθέσιμα γράμματα: {self.availableLetters}'

    def play(self, word):
        word = input("Πληκτρολόγησε την λέξη σου. Αν δεν βρίσκεις μπορείς να πας πάσο πληκτρολογώντας 'p' ή 'q' για να σταματήσεις.\n>>> ")
        while (word != 'p' and word != 'q'):
            if (self.checkWord(word, self.availableLetters)):
                if (self.isWordAccepted(word)):
                    return word
                else:
                    word = input("Η λέξη σου δεν υπάρχει στο λεξικό. Ξαναδοκίμασε ή αν δεν βρίσκεις λέξη μπορείς να πας πάσο πληκτρολογώντας 'p' ή 'q' για να σταματήσεις.\n>>> ")
            else:
                word = input("Η λέξη σου δεν αποτελείται από τα διαθέσιμα γράμματα. Ξαναδοκίμασε ή αν δεν βρίσκεις λέξη μπορείς να πας πάσο πληκτρολογώντας 'p' ή 'q' για να σταματήσεις.\n>>> ")
            
        return word
    
    def checkWord(self, word, letters):
        copyLetters = copy.deepcopy(letters)
        for l in word:
            if (l in copyLetters):
                copyLetters.pop(copyLetters.index(l))
            else:
                return False
        return True    


class Computer(Player):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'Κλάση: {self.__class__}, Διαθέσιμα γράμματα: {self.availableLetters}'

    def play(self, letters, mode):
        # letters: available letters
        # mode: MIN, MAX, SMART
        words = list(self.getPermutations(letters))
        if (mode == "MIN"):
            for w in words:
                strw = self.listToString(w)
                if (self.isWordAccepted(strw)):
                    return strw
            return # return nothing if no word is found
        if (mode == "MAX"):
            for w in reversed(words):
                strw = self.listToString(w)
                if (self.isWordAccepted(strw)):
                    return strw
            return
        else:
            wordlist = []
            for w in words:
                strw = self.listToString(w)
                if (self.isWordAccepted(strw)):
                    wordlist.append(strw)
            return wordlist

    def getPermutations(self, letters):
        perms = []
        for i in range(2, 8):
            perms += itertools.permutations(letters, i)
        return perms

    def listToString(self, s): 
        str = "" 
        return (str.join(s))


class Game:
    def __init__(self):
        self.settings = "MIN"
        pass

    def __repr__(self):
        return f'Κλάση: {self.__class__}, mode: {self.settings}'

    def setup(self):
        self.sak = SakClass()
        self.player = Human()
        self.computer = Computer()
        self.moves = 0  # total moves in this game
        self.computerScore = 0
        self.playerScore = 0
        self.player.availableLetters = self.sak.getletters(7)
        self.computer.availableLetters = self.sak.getletters(7)

    def run(self):
        userinput = self.menu()
        while (userinput != 'q'):
            if (userinput == '1'):
                self.printScore()
                pass
            elif (userinput == '2'):
                self.changeSettings()
            elif (userinput == '3'):
                input("Το παιχνίδι θα ξεκινήσει. Είσαι έτοιμος; (Πάτα ENTER)")
                self.setup()
                print(self.moves)
                condition = self.start()
                if (condition != "quit"):
                    self.announceWinner()
                    self.end()
            else:
                print("Δεν υπάρχει αυτή η επιλογή. Δοκίμασε ξανά.")
            userinput = self.menu()
        
    def start(self):
        # μονός: υπολογιστής
        # ζυγός: παίκτης
        while (len(self.sak.sak) > 0):
            print("_______________________________________")
            if (self.moves % 2 == 0):
                # player
                print("Στο σακουλάκι: {} γράμματα. \nΠαίζεις. Διαθέσιμα Γράμματα:".format(len(self.sak.sak)))

                print(self.getLettersAndValues(self.player.availableLetters))

                word = self.player.play(self.player.availableLetters)

                if (word == "p"):
                    if (len(self.sak.sak) < 7):
                        # δεν υπάρχουν αρκετά γράμματα
                        return
                    print("Πήγες πάσο.")
                    self.sak.putbackletters(self.player.availableLetters)
                    self.player.availableLetters = self.sak.getletters(7)
                elif (word == "q"):
                    areyousure = input("Είσαι σίγουρος ότι θέλεις να σταματήσεις; (Πάτα ENTER για ΝΑΙ ή 'Ο' για ΌΧΙ)\n>>> ")
                    if (areyousure == 'Ο' or areyousure == 'O'):
                        continue
                    return "quit"
                else:
                    value = self.sak.getwordvalue(word)
                    print("Έπαιξες: {} και πήρες {} πόντους.".format(word, value))
                    self.playerScore += value
                    for l in word:
                        self.player.availableLetters.pop(self.player.availableLetters.index(l))
                if (len(self.sak.sak) < len(self.player.availableLetters)):
                    # δεν υπάρχουν αρκετά γράμματα
                    self.moves += 1
                    return
                self.player.availableLetters += self.sak.getletters(7 - len(self.player.availableLetters))
            else:
                # computer
                print("Στο σακουλάκι: {} γράμματα. \nΠαίζει ο υπολογιστής. Διαθέσιμα Γράμματα:".format(len(self.sak.sak)))
                print(self.getLettersAndValues(self.computer.availableLetters))

                word = self.computer.play(self.computer.availableLetters, self.settings)

                if (self.settings == "SMART"):
                    # SMART mode
                    value = 0
                    finalword = "pass"
                    for w in word:
                        newvalue = self.sak.getwordvalue(w)
                        if (value < newvalue):
                            value = newvalue
                            finalword = w
                    word = finalword

                if (word == "pass"):
                    if (len(self.sak.sak) < 7):
                        # δεν υπάρχουν αρκετά γράμματα
                        return
                    print("Ο υπολογιστής πήγε πάσο.")
                    self.sak.putbackletters(self.computer.availableLetters)
                    self.computer.availableLetters = self.sak.getletters(7)
                else:
                    value = self.sak.getwordvalue(word)
                    print("Ο υπολογιστής έπαιξε: {} και πήρε {} πόντους.".format(word, value))
                    self.computerScore += value
                    for l in word:
                        self.computer.availableLetters.pop(self.computer.availableLetters.index(l))
                if (len(self.sak.sak) < len(self.computer.availableLetters)):
                    # δεν υπάρχουν αρκετά γράμματα
                    self.moves += 1
                    return
                self.computer.availableLetters += self.sak.getletters(7 - len(self.computer.availableLetters))
            self.moves += 1
            print("Νέο σκορ: (Εσύ){} - (Υπολογιστής){}".format(self.playerScore, self.computerScore))
            input("ENTER για συνέχεια")

    def announceWinner(self):
        print("Το παιχνίδι τελείωσε με σκορ (Εσύ){}/(Υπολογιστής){}.".format(self.playerScore, self.computerScore))
        if (self.playerScore > self.computerScore):
            print("Νίκησες!")
        elif (self.playerScore < self.computerScore):
            print("Νίκησε ο υπολογιστής.")
        else:
            print("Ισοπαλία!")
        input("Πάτα ENTER για να επιστρέψεις στο μενού.")

    def getLettersAndValues(self, letters):
        str = ''
        for l in letters:
            str += "{}-{}, ".format(l, self.sak.getwordvalue(l))
        return str[:len(str)-2] #remove last ", "

    def end(self):
        # save in json
        with open('score.json') as json_file:
            data = json.load(json_file)
            newentry = '"moves": {}, "player": {}, "computer": {}'.format(self.moves, self.playerScore, self.computerScore)
            newentry = "{" + newentry + "}"
        
        with open('score.json', 'w') as json_file:
            data.append(json.loads(newentry))
            json.dump(data, json_file, ensure_ascii=True, indent=4, sort_keys=True)

    def changeSettings(self):
        userinput = input("""___ΡΥΘΜΙΣΕΙΣ___
Ο υπολογιστής θα παίξει:
1) ΜΙΝ: την πρώτη μικρότερη λέξη που θα βρει
2) ΜΑΧ: την πρώτη μεγαλύτερη λέξη που θα βρει
3) SMART: την λέξη με τους περισσότερους πόντους
Πληκτρολόγησε 1, 2 ή 3 (τρέχον ρύθμιση: {})
>>> """.format(self.settings))
        if (userinput == '1'):
            self.settings = "MIN"
        elif (userinput == '2'):
            self.settings = "MAX"
        elif (userinput == '3'):
            self.settings = "SMART"
        else:
            print("Αυτή η επιλογή δεν υπάρχει. Οι ρυθμίσεις δεν θα αλλάξουν και θα επιστρέψετε στο κυρίως μενού.")
            return
        print("Ο υπολογιστής θα  παίζει πλέον με τον τρόπο: " + self.settings)

    def menu(self):
        return input("""~~~~ SCRABBLE ~~~~
__________________
1: Σκορ
2: Ρυθμίσεις
3: Παιχνίδι
q: Έξοδος
__________________
>>> """)

    def printScore(self):
        with open('score.json') as json_file:
            data = json.load(json_file)
            print('_____ΣΚΟΡ ΑΝΑ ΠΑΙΧΝΙΔΙ_____')
            if (len(data) == 0):
                print("Δεν υπάρχουν διαθέσιμα παιχνίδια.")
            for i in range(len(data)):
                print("{}) εσύ: {}  | υπολογιστής: {}  | συνολικές κινήσεις: {}".format(i+1,  data[i]["player"], data[i]["computer"], data[i]["moves"]))

        input("Πάτα ENTER για να επιστρέψεις στο μενού...")