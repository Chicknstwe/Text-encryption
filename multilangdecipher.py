import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file ' + file_name + '.txt...')
    # inFile: file
    in_file = open(file_name + '.txt', 'r')
    word_list = []
    # line: string
    for line in in_file:
        word_list.append(in_file.readline()[:-2])
    # word_list: list of strings
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text, lang):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(lang)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        output = {}
        x = 0
        while x < 26:
            dictShift = x + shift
            if dictShift >= 26:
                dictShift -= 26
            lowerKey = string.ascii_lowercase[x]
            upperKey = string.ascii_uppercase[x]
            lowerShift = string.ascii_lowercase[dictShift]
            upperShift = string.ascii_uppercase[dictShift]
            output[lowerKey] = lowerShift
            output[upperKey] = upperShift
            x += 1
        return output
                
            


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shiftedMsg = ''
        shiftDict = self.build_shift_dict(shift)
        
        for char in self.message_text:
            if char in string.ascii_letters:
                shiftedMsg += shiftDict[char]
            else:
                shiftedMsg += char
            
        return shiftedMsg

class PlaintextMessage(Message):
    def __init__(self, text, shift, lang):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        self.text = text
        self.shift = shift
        self.msg = Message(self.text, lang)
        self.valid_words = self.msg.valid_words
        self.encrypting_dict = self.msg.build_shift_dict(self.shift)
        self.message_text_encrypted = self.msg.apply_shift(self.shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        copyDict = {}
        for key in self.encrypting_dict.keys():
            copyDict[key] = self.encrypting_dict[key]
        return copyDict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.msg.build_shift_dict(self.shift)
        self.message_text_encrypted = self.msg.apply_shift(self.shift)
        
class CiphertextMessage(Message):
    def __init__(self, text, lang):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.text = text
        self.msg = Message(self.text, lang)
        self.valid_words = self.msg.valid_words

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        prevKey = 1
        prevCount = 0
        for key in range(1, 27):
            raw_decrypt_msg = self.msg.apply_shift(26 - key).split(' ')
            decrypt_msg = [item.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"") for item in raw_decrypt_msg]
            count = 0
            for word in decrypt_msg:
                if word in self.valid_words:
                    count += 1
            if count > prevCount:
                prevCount = count
                prevKey = key
        return (26 - prevKey, self.msg.apply_shift(26 - prevKey), prevCount)

def multiLangDecrypt(text):
    
    languages = ['spanish', 'english', 'italian', 'french', 'german']
    best = ['', 0, '', 0] # [language, matches, decrypted text, key]
    may_be = []
    for lang in languages:
        obj = CiphertextMessage(text, lang)
        decryption = obj.decrypt_message()
        if decryption[2] > best[1]:
            best[0] = lang
            best[1] = decryption[2]
            best[2] = decryption[1]
            best[3] = decryption[0]
        elif decryption[2] == best[1]:
            may_be.append(lang)
    
    print("Input: " + text + "\nOutput: " + best[2] + "\nLanguage: " + best[0] + "\nFound: " + str(best[1]) + " matches\nKey: " + str(26 - best[3]))
    
    

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello, this is my story', 2, 'english')
print('Expected Output: jgnnq, vjku ku oa uvqta')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq, vjku ku oa uvqta', 'english')
print('Expected Output:', (24, 'hello, this is my story', 3))
print('Actual Output:', ciphertext.decrypt_message())

#Example text case (multiLangDecrypt)
multiText = 'jgnnq, vjku ku oa uvqta'
print('Expected Output:', ('Input: jgnnq, vjku ku oa uvqta', 'Output: hello, this is my story', 'Language: english', 'Found: 3 matches', 'Key: 2'))
multiLangDecrypt(multiText)

