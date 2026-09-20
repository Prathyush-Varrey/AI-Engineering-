'''
Functions : is a block of code that performes a specific task

functions helps in organizing code, reusing code and improving readability.

syntax :
def function_name(parameters):
    "DocString (helps others to know why this function is created)"
    #function body
    return expression 

'''

def translator(english_text):
    """This function is going to be used for converting the english to hindi  """
    if english_text == "Hello" or english_text == 'hello':
        print(f"The translation for {english_text} is Namaste")
    elif english_text == "Help"  or english_text == 'help':
        print(f'The translation for {english_text} is Madad')

translator('Help')

def translator2(english_txt):
    if english_txt == "Hello" or english_txt == 'hello':
        hindi_wrd = "Namaste"
    elif english_txt == "Help" or english_txt == 'help':
        hindi_wrd = "Madad"
    return f"The translation for {english_txt} in Hindi is {hindi_wrd}"

print(translator2('hello'))