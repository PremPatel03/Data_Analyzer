#Date: April 12, 2022
#Version: 1.0
#By: Prem Patel
from load_data import book_category_dictionary

def dictionary_list(dictionary:dict)->list:
    """
    Returns the dictionary as a list where all book data is stored
    """
    book_value = []
    
    for category in dictionary:
        for book in dictionary[category]:
            book["category"] = [category]
            if len(book_value) == 0:
                book_value += [book]
            else:
                flag = False
                for i in range(len(book_value)):
                    if book['title'] == book_value[i]['title']:
                        book_value[i]["category"] += book["category"]
                        flag = True
                if not flag:
                    book_value += [book]
    return book_value  

#=========================Function 1=============================================

def sort_books_title(book_dictionary:dict)-> list:
    """
    Returns a list with the book data stored as a dictionary book where the books are
    sorted alphabetically by title
    
    >>>sort_books_title(mydictionary)
    [{'title': "'Salem's Lot", 'author': 'Stephen King', 'language': 'English', 'rating': 4.4, 'publisher': 'Hachette UK', 'page': 300, 'category': ['Humor']}, 
    {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page': 864, 'category': ['Adventure', 'Adventure', 'Social Science', 'Epic']}, 
    {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones. A Clash of Kings. A Storm of Swords. A Feast for Crows. A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page': 4544, 'category': ['Superheroes', 'Biography', 'Legal', 'Management']},
    {another element}...
    """
    books = dictionary_list(book_dictionary)
    
    
    for final in range(len(books)):
        for i in range(len(books) - 1):
            if books[i]["title"] > books[i+1]["title"]:
                books[i], books[i+1] = books[i+1], books[i]
                
    return books

#=========================Function 2=============================================

def sort_books_ascending_rate(dictionary:dict)->(dict):
    '''
    Retuns the List of book data stored in dictionary in which books are sorted on rating
    
    >>>sort_books_ascending_rate({'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544}]}))
    
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction'], 'pages': 288}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 544}]

    Returns a list where the books from the input dictionary are sorted by rate, in ascending order (least->greatest). If two books have the same rating, they are sorted alphabetically, and if the rating is 'N/A', they are given the first priority in the returned list.
    '''

    rate = dictionary_list(dictionary)
    books = []
    ascending_rate = len(rate)
    for i in range(ascending_rate):
        if rate[i]['rating'] == 'N/A':
            books.append(rate[i])
    for i in range(ascending_rate):
        if rate[i]['rating'] != 'N/A':
            books.append(rate[i])
    for i in range(len(books)):
        for j in range(len(books)-i-1):
            if books[j]['rating'] == books[j+1]['rating']:
                if books[j]['title'] > books[j+1]['title']:
                    books[j], books[j+1] = books[j+1], books[j]
            if books[j]['rating'] != 'N/A' and books[j+1]['rating'] != 'N/A':
                if books[j]['rating'] > books[j+1]['rating']:
                    books[j], books[j+1] = books[j+1], books[j]
                        
    return books          

#=========================Function 3=============================================

def sort_books_publisher(dictionary:dict)-> list:
    """
    This function takes a dictionary and sorts it alphabetically by publisher and returns it as a list.
    
    >>>sort_books_publisher
    {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': 'N/A', 'publisher': 'AMACOM', 'page': 112, 'category': ['Economics']}, 
    {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'language': 'English', 'rating': 4.1, 'publisher': 'DC', 'page': 164, 'category': ['Humor']}, 
    {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'page': 400, 'category': ['Fiction']}, 
    {another element}...
    """
    dict_value = dictionary_list(dictionary)

    for final in range(len(dict_value)):
        for i in range(len(dict_value) - 1):
            if dict_value[i]["publisher"] > dict_value[i+1]["publisher"]:
                dict_value[i], dict_value[i+1] = dict_value[i+1], dict_value[i]
                
    return dict_value

#=========================Function 4=============================================

def sort_books_author(dictionary:dict)->list:
    """
    Creates a list of the dictionary given and make sure there is no duplicates.
    Sort through the novels in alphabetic order for author's name. This is done using bubble sort.
    
    >>> sort_book_author(book_category_dictionary)
    {'author': 'Alex Lake', 'language': 'English', 'pages': '416', 'category': 'Adventure', 'rating': '4.1', 'title': 'After Anna', 'publisher': 'HarperCollins UK'}
    {'author': 'Andrzej Sapkowski', 'language': 'English', 'pages': '400', 'category': 'Adventure', 'rating': '4.8', 'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'publisher': 'Hachette UK'}
    {'author': 'Andrzej Sapkowski', 'language': 'English', 'pages': '96', 'category': 'Adventure', 'rating': '4.8', 'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'publisher': 'Hachette UK'}
    {'author': 'Brandon Sanderson', 'language': 'English', 'pages': '226', 'category': 'Adventure', 'rating': '4.8', 'title': 'Edgedancer: From the Stormlight Archive', 'publisher': 'Tor Books'}
    {'author': 'Brent Weeks', 'language': 'English', 'pages': '688', 'category': 'Adventure', 'rating': '4.7', 'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'publisher': 'Hachette UK'}
    
    """
    
    book_author = dictionary_list(dictionary)
    author = len(book_author)
    
    for i in range(author):
        for j in range(0,author-i-1):
            var = ""
            if book_author[j].get('author') > book_author[j+1].get('author'):
                book_author[j], book_author[j+1] = book_author[j+1], book_author[j]
                    
    return book_author
