class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0


    def display(self):
        self.count = 0
        for i, c in enumerate(self.secretWord):
            if c in self.guessedChars:
                self.count += 1
        if self.count == len(self.secretWord):
            return True
        else:
            return False

        self.blanks= ['_']*len(self.secretWord)
        for i, c in enumerate(self.secretWord):
            if self.c in self.guessedChars:
                self.count += 1
                self.blanks.insert(self.count - 1, c)
                self.blanks.pop(self.count)
                if self.count == len(self.secretWord):
                    return ''.join(str(e) for e in self.blanks)
            else:
                self.count += 1
                self.blanks.insert(self.count - 1, '_')
                self.blanks.pop(self.count)
                if self.count == len(self.secretWord):
                    return ''.join(str(e) for e in blanks)


    def guess(self, character):
        if character in self.secretWord:
            if character in self.guessedChars:
                print(self.display(self))
            else:
                self.guessedChars.append(character)
                print("Tries:", self.numTries)
                print(self.guessedChars)
        else:
            if character in self.guessedChars:
                print(self.display(self))
            else:
                self.guessedChars.append(character)
                self.numTries += 1
                print("Tries:", self.numTries)
                print(self.guessedChars)

