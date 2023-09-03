#Date: April 12, 2022
#Version: 1.0
#Written by: Prem Patel


import string
from typing import List

def book_category_dictionary(file_name:str)->list:
    """
    Preconditions : File must be in .csv or .txt and contain information 
    in the similar layout as the example file
    
    Returns all the different types of books depending on the selected category
    
    >>> "Fiction"
    >>> [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 
    'language': 'English', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'page': '288'}
    >>> "Comic"
    >>> [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 
    'language': 'English', 'rating': '4.2', 'publisher': 'Marvel Entertainment', 'page': '96'}
    >>> "Fantasy"
    >>> [{'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 
    'language': 'English', 'rating': '4.8', 'publisher': 'Hachette UK', 'page': '96'}]
    
    """
    file = open(file_name,"r") #Opens the file and reads through it
    book_dict = {}             #The dictionary is listed
    categories = set()
    
    file.readline()[1:] #Skips the first line
    for books in file:
        book_info = books.strip("\n").split(",") #Remove \n and splits every comma
        categories.add(book_info[5])
        book = {}       
        rating = book_info[2]
        if rating != "N/A" and rating != "rating": #If statement to make "rating"
            rating = float(rating)                 # a float number
        book.update({                 #Keys and their corresponding values
            "title" : book_info[0],   
            "author" : book_info[1],
            "language" : book_info[6],
            "rating" : rating,
            "publisher" : book_info[3],
            "page" : int(book_info[4])  #Page is defined as an integer
            })
        
        if book_info[5] not in book_dict: 
            category = book_info[5]
            book_dict[book_info[5]] = [] 
        
        if book not in book_dict[category]: 
            book_dict[category].append(book) #Append the book only if it is not already included in dictionary       
            
    file.close() #Close file when done
    
    return book_dict #Returns the dictionary    
