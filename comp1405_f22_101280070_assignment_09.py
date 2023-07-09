# Name: Kyle Cathleen Ann San Buenaventura
# CU Student Number: 101280070
# Assignment no. 9: "leetspeak"
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Accuracy Check Recommendation: 
    INPUT: {hello}, thank you so much for teaching me artificial intelligence!! thank you lord!~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import random


def main():  # main function
    print("""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    Assignment no. 09: "1337"
               LEETSPEAK  T |2 A /\/ $ !_ A T 0 |2
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n""")
    english = input(
        "Input a phrase: ")  # user prompt: to input and convert to an acronym then leetspeak
    punct = '''!<>./?@#$%^&*_~`=+()-[]{};:'"\,'''  # defining punctuations
    remove_punct = ""

    for a in english:  # function within main: removes punctuations
        if a not in punct:
            remove_punct += a

    acronym = get_acronym(remove_punct)  # get acronym
    print(acronym)

    replace_up(acronym)  # capitalize: replace_up(message0) function call
    leetspeak = convert(acronym)
    print(leetspeak)  # translate: translate(message1) function call


def get_acronym(string):  # get specific acronyms from the user input: ai, ty, ikr, tyl
    d = {"artificial intelligence": "AI", "thank you": "TY", "i know right": "IKR",
         "thank you lord": "TYL", "machine learning": "ML"}
    for key in d.keys():
        while key in string:
            string = string.replace(key, d[key])
    return string


def replace_up(message0):  # capitalize: function that capitalizes letters using chr() and ord()
    upup = ""
    for j in message0:
        j = ord(j) - 32
        upup += chr(j)
    return upup


# convert: english string to leetspeak (i.e., homoglyphs) without built-in translate() etc...
def convert(message1):
    leetspeak = ""
    homo = {
        "b": ["|3", "|-}", "!3", "\3"],
        "c": ["(", "((", "(_", "[_"],
        "d": ["[}", "[)", "[)", "|)"],
        "e": ["=e", "-3", "eE", "=_'"],
        "f": ["|#", "3|=", "/#", "/=", "/="],
        "g": ["g3", "gee", "@g", "dg3", "C-,"],
        "h": ["|-|", "}{", "/-/", "]-[", "]=[", "\\-\\"],
        "j": [",_|", "_|", "._|", "._]", ",_]", "]"],
        "n": ["/\/", "|\\|", "/\\/", "/V"],
        "o": ["Q", "()", "0", "(*)"],
        "p": ["|;", "|^", "|''", "|D", ],
        "q": ["0,", "(_,)", "Qu", "O,"],
        "s": ["5", "es", "hS", "$", "{s"],
        "u": ["[_]", "(_)", "!_!", "|_|", "Yu"],
        "v": ["\/", "1/", "\//", "\\//"],
        "w": ["\\/\\/", "VV", "\\N", "'//", "\\\\'", "\\^/", "\\X/"],
        "x": [">|<", "}{", "><", "3k$"],
        "z": ["*5", "2c", "z|-|", "2"]}
    for char in message1:
        if char.lower() in homo:
            eng_to_leet = random.choice(homo[char.lower()])
            leetspeak += eng_to_leet
        else:
            leetspeak += char
    return leetspeak


if __name__ == "__main__":
    main()
