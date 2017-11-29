class Guess:
    def __init__(self, word):
        self.guessedChars = []
        self.numTries = 0
        self.secretWord = word
        self.currentStatus = '_' * (len(self.secretWord))

    def display(self):
        print("Current : ", self.currentStatus)
        print("Tries : ", self.numTries)

    def guess(self, character):
        if character in self.guessedChars:
            pass

        else:
            self.guessedChars += character

        if character not in self.secretWord:
            self.numTries += 1

        for i in range(len(self.secretWord)):
            if self.secretWord[i] == character:
                self.currentStatus = self.currentStatus[0: i] + character + self.currentStatus[i + 1:]

        if self.currentStatus == self.secretWord:
            return True

        else:
            return False