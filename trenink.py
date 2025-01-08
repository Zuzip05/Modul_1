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

#user inpu
username=input("username: ")
password=input("password: ")

#maximum number of characters for dash length
dash_lenght=len("Enter a number btw. 1 and 3 to select: x")

#enabling access for registered users and user welcome
if username in users and users[username] == password:
    print("-" * dash_lenght)
    print("Welcome to the app, ",username,)
    print("We have 3 texts to be analyzed.")
    print("-" * dash_lenght)
   
#text selection 1-3
    text_nr=input("Enter a number btw. 1 and 3 to select:")
    if text_nr.isdigit():
        if 1 <= int(text_nr) <= 3:

# Remove unwanted characters and split the text
            words=(TEXTS[int(text_nr)-1].split())
            clean_words=[item.replace(",", "").replace(".","").replace("/n","").replace(" ","") for item in words]
                       
#number of words in the selected text
            words_count = len(clean_words)
            
#number of words with title case            
            titlecase_count = sum(1 for word in clean_words if word[0].isupper()) 

 #number of words with upper case           
            uppercase_count= sum(1 for word in clean_words if word.isupper() 
                                and not any(char.isdigit() for char in word))

#number of words with lower case            
            lowercase_count= sum(1 for word in clean_words if word.islower()) 

#number of digits
            digit_count= sum(1 for word in clean_words if word.isdigit()) 
            
#sum of all numbers            
            sum_numbers=sum([int(word) for word in clean_words if word.isdigit()]) 
            
#print results 
            print("-" * dash_lenght)
            print("There are ",words_count, " words in the selected text.")
            print("There are ",titlecase_count, " titlecase words.")
            print("There are ",uppercase_count, " uppercase words.")
            print("There are ",lowercase_count, " lowercase words.")
            print("There are ",digit_count, " numeric strings.")
            print ("The sum of all the numbers ",sum_numbers)
            print("-" * dash_lenght)
            
#count the length of words and the number of words of a given length            
            dict_word_len = {}
            for word in clean_words:
                word_length = len(word)
                if word_length in dict_word_len:
                    dict_word_len[word_length] += 1
                else:
                    dict_word_len[word_length] = 1
                continue
#sorted dictionairy
            sorted_dict = {key:dict_word_len[key] for key in sorted(dict_word_len)}

#print bar chart header
            print("{:>3}|".format("LEN"),"{:^12}".format("OCCURENCES"),"|NR")
            print("-" * dash_lenght)

# Print the rows of the table - number of words with define lenght
            for key, value in sorted_dict.items():
                print("{:>3}|".format(f"{key}"),"{:<12}".format("*"*int(f"{value}")),"|",f"{value}")
    
#input selected text is not between 1-3, terminating the program        
        else:
            print("your input is not btw. 1 and 3, terminating the program")

#input selected text is not a number, terminating the program   
    else:
        print("your input is not a number, terminating the program")

#user is not registered, terminating the program
else:
    print("unregistered user, terminating the program.")