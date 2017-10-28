"""
MIT License

Copyright (c) 2017 Demetrio Carmona Derqui

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from random import randint

class Encryption(object):
    def __init__(self, words='&', key='&'):
        '''
        Initialize a new en/decryption.
        
        words: string. Empty string by default. Words to encrypt/decrypt.
        key: string. Empty string by default.
        char_dic and val_dic: dictionaries used in en/decryption.
        '''
        self.words = str(words).lower()
        self.key = str(key)
        
        self.char_dic = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
            'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 
            'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 
            'w': 22, 'x': 23, 'y': 24, 'z': 25, 'ñ': 26, 'ç': 27, ' ': 28, 
            '0': 29, '1': 30, '2': 31, '3': 32, '4': 33, '5': 34, '6': 35, 
            '7': 36, '8': 37, '9': 38, '!': 39, '¡': 40, '¿': 41, '?': 42, 
            'º':43, 'ª': 44, '%': 45, '@': 46, '€': 47, '$': 48, '(': 49, ')': 50}
        
        self.val_dic = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', 
            '6': 'g', '7': 'h', '8': 'i', '9': 'j', '10': 'k', '11': 'l', 
            '12': 'm', '13': 'n', '14': 'o', '15': 'p', '16': 'q', '17': 'r', 
            '18': 's', '19': 't', '20': 'u', '21': 'v', '22': 'w', '23': 'x', 
            '24': 'y', '25': 'z', '26': 'ñ', '27': 'ç', '28': ' ', '29': '0',
            '30': '1', '31': '2', '32': '3', '33': '4', '34': '5', '35': '6',
            '36': '7', '37': '8', '38': '9', '39': '!', '40': '¡', '41': '¿', 
            '42': '?', '43': 'º', '44': 'ª', '45': '%', '46': '@', '47': '€', 
            '48': '$', '49': '(', '50': ')'}
        
        self.enc_msg = ''
        self.dec_msg = ''
        self.method = 'none'
        
    def __str__(self):
        return 'Input Words: ' + str(self.words) + '\nInput key: ' + str(self.key)
      
    def getKey(self):
        return self.key
    
    def getWords(self):
        return self.words
    
    def getEncMesg(self):
        return self.enc_msg
        
    def getDecMsg(self):
        return self.dec_msg
    
    def getMethod(self):
        return self.method
    
    def swap(self):
        if self.dec_msg != '':
            self.words = str(self.dec_msg)
            return True
        else:
            print('You must decrypt a message before using swap().')
        
    def setKey(self, newKey):
        '''
        Setter for self.key.
        
        newKey: string.
        '''
        allowed = True
        for char in newKey:
            if char not in self.char_dic.keys():
                allowed = False
                print('Error: the string contains one or more unallowed characters.')
                break
        if allowed:    
            self.key = str(newKey)
            print('Key has been changed.')
    
    def length(self):
        print('Words length: ' + str(len(str(self.words))) + '\nKey length: ' + str(len(str(self.key))) + '\nDics length: ' + str(len(self.char_dic)) + ' | ' +  str(len(self.val_dic)))
        
    def setWords(self, newWords):
        '''
        Setter for self.words.
        
        newWords: string.
        '''
        allowed = True
        for char in newWords:
            if char not in self.char_dic.keys():
                allowed = False
                print('Error: the string contains one or more unallowed characters.')
                break
        if allowed:    
            self.words = str(newWords)
            print('Words have been changed.')
        
    def charsAllowed(self):
        '''
        Return a string with all characters allowed to be en/decrypted.
        '''
        output = ''
        for i in self.char_dic.keys():
            output = output + str(i)
        print('Allowed characters: ' + output)
        
    def caesar_enc(self):
        '''
        Caesar encryption adds the 'index' of each input's character in the 
        dictionary (char_dic) to the 'index' of the key (that must be a string 
        with length 1) to get each encrypted character.
        
        Returns a string with encrypted characters or error if key's length is 
        different than 1.
        '''
        if self.key not in self.char_dic.keys():
            # The program can generate a random key if user doesn't provide it
            # or it is not valid.
            self.key = self.val_dic[str(randint(0, 50))]
            print('Random key generated: ' + self.key)
        if len(self.key) == 1:
            output = ''
            for char in self.words.lower():
                newKey = self.char_dic[char] + self.char_dic[self.key]
                if newKey >= len(self.val_dic):
                    newKey = newKey - len(self.val_dic)
                output = output + self.val_dic[str(newKey)]
            self.enc_msg = output
            print('Encrypted output:' + output)
            self.method = 'Caesar'
        else:
            print('Error: wrong key length.\nInfo: Cesar encryption\'s key must be a single character.')
            
    def caesar_dec(self):
        '''
        Caesar decryption substracts the 'index' of the key to each input's 
        character to get each decrypted character.
        
        Returns a string with decrypted characters or error if key's length is 
        different than 1 or key isn't in the dictionary.
        '''
        if self.method != 'Caesar' and self.method != 'none':
            print('Error: the words must be encrypted with Caesar method before.')
        else:
            if len(self.enc_msg) > 0:
                rec = input('There\'s an encrypted message stored in this object. Do you want to use it to decryption? y/n')
                if rec == 'y':
                    msg_input = self.enc_msg
                else:
                    msg_input = self.words
            if len(self.key) == 1 and self.key in self.char_dic.keys():
                
                output = ''
                for char in msg_input.lower():
                    newKey = self.char_dic[char] - self.char_dic[self.key]
                    if newKey < 0:
                        newKey = len(self.char_dic) + newKey
                    output = output + self.val_dic[str(newKey)]
                self.msg_dec = output
                print('Encrypted output:' + output)
            else:
                print('Error: wrong key.\nInfo: Cesar decryption\'s key must be a single character.\nUse charsAllowed method to get all allowed characters.')
    
    def oneTimePad_enc(self):
        '''
        One-Note Pad encryption adds the 'index' of each input's character in the 
        dictionary (char_dic) to the 'index' of the key (that must be a string 
        with length 1) to get each encrypted character.
        
        Returns a string with encrypted characters or error if key's length is 
        different than 1.
        '''
        if len(self.key) != len(self.words):
            # The program can generate a random key if user doesn't provide it
            # or it is not valid.
            cont = False
            while not cont:
                genKey = input('Key and input words lengths are different.\nDo you want to generate a random key? (y/n)')
                if genKey == 'y':
                    self.key = ''
                    cont = True
                    while len(self.key) < len(self.words):
                        self.key = self.key + self.val_dic[str(randint(0, len(self.val_dic) - 1))]
                    print('Random key generated: ' + self.key)
                elif genKey == 'n':
                    cont = True
                    print('Encryption was cancelled.')
        if len(self.key) == len(self.words):
            output = ''
            i = 0
            while i < len(self.words):
                newKey = self.char_dic[self.words[i]] + self.char_dic[self.key[i]]
                if newKey >= len(self.val_dic):
                    newKey = newKey - len(self.val_dic)
                output = output + self.val_dic[str(newKey)]
                i += 1
            self.enc_msg = output
            print('Encrypted output: ' + output)
            self.method = 'One Time Pad'
            
    def oneTimePad_dec(self):
        '''
        One-Note Pad encryption adds the 'index' of each input's character in the 
        dictionary (char_dic) to the 'index' of each key's character (that must
        be a string with same length as the input words) to get each encrypted 
        character.
        
        Returns a string with encrypted characters or error if key's length is 
        different than 1.
        '''
        if self.method != 'One Time Pad' and self.method != 'none':
            print('Error: the words must be encrypted with One Time Pad method before.')
        else:
            if len(self.enc_msg) > 0:
                rec = input('There\'s an encrypted message stored in this object. Do you want to use it to decryption? y/n')
                if rec == 'y':
                    msg_input = self.enc_msg
                else:
                    msg_input = self.words
            if len(self.key) == len(msg_input):
                output = ''
                i = 0
                while i < len(msg_input):
                    newKey = self.char_dic[msg_input[i]] - self.char_dic[self.key[i]]
                    if newKey < 0:
                        newKey = len(self.val_dic) + newKey
                    output = output + self.val_dic[str(newKey)]
                    i += 1
                self.msg_dec = output
                print('Decrypted output: ' + output)
            else:
                print('Error: words and key must have the same length.')
            
