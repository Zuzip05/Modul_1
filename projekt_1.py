"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Zuzana Pechova
email: pechovazuzana@seznam.cz
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#registered users
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username=input("username: ") #input user
password=input("password: ") #input password

dash_lenght=len("Enter a number btw. 1 and 3 to select: x") #dash lenght

if username in users and users[username] == password: #enabling access
    print("-" * dash_lenght) #dash
    print("Welcome to the app, ",username,) #welcome user
    print("We have 3 texts to be analyzed.") #welcome user
    print("-" * dash_lenght) #dash
    text_nr=input("Enter a number btw. 1 and 3 to select:") #text selection
    if text_nr.isdigit(): #calculation
        if 1 <= int(text_nr) <= 3:
            print("-" * dash_lenght) #dash
            words=(TEXTS[int(text_nr)-1].split()) #words split
            words_count = len(words) #number of words in the selected text
            print("There are ",words_count, " words in the selected text.") #print
            titlecase_count = sum(1 for word in words if word[0].isupper()) #number of words with title case
            print("There are ",titlecase_count, " titlecase words.") #print
            uppercase_count= sum(1 for word in words if word.isupper() #number of words with upper case
                                and not any(char.isdigit() for char in word))
            print("There are ",uppercase_count, " uppercase words.") #print
            lowercase_count= sum(1 for word in words if word.islower()) #number of words with lower case
            print("There are ",lowercase_count, " lowercase words.") #print
            digit_count= sum(1 for word in words if word.isdigit()) #number of digits
            print("There are ",digit_count, " numeric strings.") #print
            sum_numbers=sum([int(word) for word in words if word.isdigit()]) #sum of all numbers
            print ("The sum of all the numbers ",sum_numbers) #print
            print("-" * dash_lenght) #dash
            print("{:>3}|".format("LEN"),"{:^12}".format("OCCURENCES"),"|NR") #print chart title
            print("-" * dash_lenght) #dash
            words_lenght = {slovo: len(slovo) for slovo in words} #délka slov
            len1=sum(1 for word, lenght in words_lenght.items() if len(word)==1) #number of words with lenght 1
            print("{:>3}|".format("1"),"{:<12}".format("*"*len1),"|",len1) #print
            len2=sum(1 for word, lenght in words_lenght.items() if len(word)==2) #number of words with lenght 2
            print("{:>3}|".format("2"),"{:<12}".format("*"*len2),"|",len2) #print
            len3=sum(1 for word, lenght in words_lenght.items() if len(word)==3) #number of words with lenght 3
            print("{:>3}|".format("3"),"{:<12}".format("*"*len3),"|",len3) #print
            len4=sum(1 for word, lenght in words_lenght.items() if len(word)==4) #number of words with lenght 4
            print("{:>3}|".format("4"),"{:<12}".format("*"*len4),"|",len4) #print
            len5=sum(1 for word, lenght in words_lenght.items() if len(word)==5) #number of words with lenght 5
            print("{:>3}|".format("5"),"{:<12}".format("*"*len5),"|",len5) #print
            len6=sum(1 for word, lenght in words_lenght.items() if len(word)==6) #number of words with lenght 6
            print("{:>3}|".format("6"),"{:<12}".format("*"*len6),"|",len6) #print
            len7=sum(1 for word, lenght in words_lenght.items() if len(word)==7) #number of words with lenght 7
            print("{:>3}|".format("7"),"{:<12}".format("*"*len7),"|",len7) #print
            len8=sum(1 for word, lenght in words_lenght.items() if len(word)==8) #number of words with lenght 8
            print("{:>3}|".format("8"),"{:<12}".format("*"*len8),"|",len8) #print
            len9=sum(1 for word, lenght in words_lenght.items() if len(word)==9) #number of words with lenght 9
            print("{:>3}|".format("9"),"{:<12}".format("*"*len9),"|",len9) #print
            len10=sum(1 for word, lenght in words_lenght.items() if len(word)==10) #number of words with lenght 10
            print("{:>3}|".format("10"),"{:<12}".format("*"*len10),"|",len10) #print
            len11=sum(1 for word, lenght in words_lenght.items() if len(word)==11) #number of words with lenght 11
            print("{:>3}|".format("11"),"{:<12}".format("*"*len11),"|",len11) #print
        else:
            print("your input is not btw. 1 and 3, terminating the program") #terminating the program
    else:
        print("your input is not a number, terminating the program") #terminating the program
else:
    print("unregistered user, terminating the program.") #terminating the program