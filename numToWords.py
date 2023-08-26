from enum import Enum


class numToWords():

    WORDS = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', \
            11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen', \
            10:'Ten', 20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety'}

    MILESTONES = {1:['One',0], 10:['Ten',1], 100:['Hundred',2], 1000:['Thousand',3], 1000000:['Millions',6], 1000000000:['Billion',9], 1000000000000:['Trillion', 12]}

    MAX_VALUE = 10000000000000       #start at one trillion

    def __init__(self, val):
        self.value = val
        self.sum = 0
        self.start = numToWords.MAX_VALUE
        self.words = ''
        self.index = 0
        self.cents = 0

    def numToWords(self):

        self._get_cents()
        self._find_init_idx()
        self._stream_value()

        self.words = self.words + ' ' + str(self.cents) + '/100'

        # print(f'NumToWords: {self.words}')

        return self.words

    def _get_cents(self):
        whole = int(self.value) 
        diff = round(self.value - whole,2)
        self.cents = int(diff * 100)
        self.value = whole


    def _find_init_idx(self):
        for idx, x in enumerate(numToWords.MILESTONES):
            if self.value / x > 1:
                self.index = x
                self.data = numToWords.MILESTONES[x][0]
            else:    
                break
        
        if self.data == 'Ten':
            if self.value in numToWords.WORDS:
                self.words = self.words + ' ' + numToWords.WORDS[self.value]
                self.value = self.value-self.value
            else:
                whole = self.value // self.index
                self.data = numToWords.WORDS[whole*self.index]
                self.value = self.value - (whole*self.index)
                self.index = 1
        elif self.data == 'One':
            self.data = ''
        
        # print(f'value: {self.value} \ data: {self.data} \ index: {self.index}')


    def _greater_than_twenty(self, value):
        val = value
        word = ''

        while val > 0:
            if val > 100:
                whole = val // 100
                word = numToWords.WORDS[whole] + ' Hundred'
                val = val - (whole * 100)
            elif val > 20:
                whole = val // 10
                word = word + ' ' + numToWords.WORDS[whole * 10]
                val = val - (whole * 10)
            else:
                word = word + ' ' + numToWords.WORDS[val]
                val = val - val
            
            # print(f'value: {value} / val: {val} / whole: {whole} / word: {word}')
        
        return word

    def _stream_value(self):
        while self.value > 0:
            whole = self.value // self.index

            if whole > 20:
                self.words = self.words + ' ' + self._greater_than_twenty(whole) + ' ' + self.data
            elif self.index == 1:
                self.words = self.words + ' ' + self.data + ' ' + numToWords.WORDS[whole]
            else:
                self.words = self.words + ' ' + numToWords.WORDS[whole] + ' ' + self.data
            # print(f'1. whole: {whole} \ words: {self.words} \ value: {self.value} \ index: {self.index}')
            self.value = self.value - (whole*self.index)
            # print(f'2. whole: {whole} \ words: {self.words} \ value: {self.value} \ index: {self.index}')
            self._find_init_idx()

if __name__ == '__main__':
    app = numToWords(213410006311002.21)
    app.numToWords()