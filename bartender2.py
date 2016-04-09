#this program asks for a person's drink preferences, stores them in a new dictionary
#and then creates a drink based on the person's answers by selecting ingredients
#at random that identify with the choices the person has made.

questions = {
    "strong": "Do ye like yer drinks strong? ",
    "salty": "Do ye like it with a salty tang? ",
    "bitter": "Are ye a lubber who likes it bitter? ",
    "sweet": "Would ye like a bit of sweetness with yer poison? ",
    "fruity": "Are ye one for a fruity finish? ",}

import random

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],}

responses = {}

def taste_questions():
    print("Please answer each question with 'yes or no'.")

    for taste, question in questions.items():
        
        response = raw_input(question)
        
        if response == "yes":
            responses[taste] = True
        
        else:
            responses[taste] = False
            
    return responses

def bartender(responses, ingredients):
    print("I made you a drink, here are the ingredients:")
    
    for key, value in responses.items():
    
        if value is True:
            
            print("A {0}".format(ingredients[key][random.randint(0,2)]))

    return

if __name__ == '__main__':
    taste_questions()
    bartender(responses, ingredients)