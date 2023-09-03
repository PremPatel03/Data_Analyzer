#Date: April 12, 2022
#Version: 1.0
#By:: Prem Patel 101224274
#=================================Function #1===================================
def book_add(book_dict:dict,books:tuple)->list:
    """
    Returns the newly added book in the dictionary depending on its category. 
    A message is printed as confirmation
    
    >>> book_add(T090_P1_load_data.book_category_dictionary("google_books_dataset.csv"),("Harry Potter and the Sorcerer's Stone","J.K Rowling", "4.5", "Bloomsbury Publishing" , "223 ", "Fiction", "English"))
    Fiction: "Harry Potter and the Sorcerer's Stone","J.K Rowling", "English", "4.5", "Bloomsbury Publishing" , "223 "
    "Book has been added correctly!"
    >>>book_add(T090_P1_load_data.book_category_dictionary("google_books_dataset.csv"),("The Eye of the World","Robert Jordan", "4.2", "Tor Books" , "782 ", "Fantasy", "English"))
    Fantasy: "The Eye of the World","Robert Jordan", "English", "4.2", "Tor Books" , "782 "
    "Book has been added correctly!"
    >>>book_add(T090_P1_load_data.book_category_dictionary("google_books_dataset.csv"),("The Hobbit","J.R.R.Tolkien", "4.2", "Harper Collins." , "310 ", "Adventure", "English"))
    "The Hobbit","J.R.R.Tolkien", "English", "4.2", "Harper Collins." , "310 ", "Adventure"
    "Book has been added correctly!"
    """
    book = {}       
    rating = books[2]
    if rating != "N/A" and rating != "rating": 
        book.update({                 
            "title" : books[0],   
            "author" : books[1],
            "language" : books[6],
            "rating" : rating,
            "publisher" : books[3],
            "page" : int(books[4])  
        })    
    
    statement = {}
    category = books[5]
    if books[5] not in book_dict:        
        book_dict[category] = []
    book_dict[category].append(book)    
    
    if statement == book:
        print("There was an error adding the book")
    else:
        print("Book has been added correctly!")
        
    return book_dict

#=================================Function #2===================================
def remove_book(book_dict:dict, book_title:str, book_category:str)->list:
    """
    Returns the removed book removed book dictionary depending on its category.
    A message is printed as confirmation.
    
    >>> remove_book(book_dict,"Antiques Roadkill: A Trash 'n' Treasures Mystery","Fiction")
    The book has been removed correctly
    >>> remove_book(book_dict,"Deadpool Kills the Marvel Universe","Comic")
    The book has been removed correctly
    >>> remove_book(book_dict,"And Then There Were None","Detective")
    The book has been removed correctly
    """
    check_values = 0
    if book_category in book_dict:
        for book in book_dict[book_category]:
            if book_title == book['title']:
                book_dict[book_category].remove(book)
                check_values = 1

    if check_values == 1:
        print("The book has been removed correctly")
    else:
        print("There was an error removing the book. Book not found")
    
    return book_dict
#=================================Function #3===================================
def get_books_by_category(doc:str,cat:str) -> list[str]:
    """ This function displays the books of a user inputted category.
    >>> 
    The category Economics has 22 books. This is the list of books:
    Book 1: How To Win Friends and Influence People by Dale Carnegie
    Book 2: Marketing (The Brian Tracy Success Library) by Brian Tracy
    Book 3: Goals!: How to Get Everything You Want -- Faster Than You Ever Thought Possible. Edition 2 by Brian Tracy
    Book 4: The Power of Habit: Why We Do What We Do in Life and Business by Charles Duhigg
    Book 5: Management (The Brian Tracy Success Library) by Brian Tracy
    Book 6: Getting Things Done: The Art of Stress-Free Productivity by David Allen
    Book 7: How to Understand Business Finance: Edition 2 by Bob Cinnamon
    Book 8: Rework by Jason Fried
    Book 9: The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    Book 10: Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth by T. Harv Eker
    Book 11: Business Strategy (The Brian Tracy Success Library) by Brian Tracy
    Book 12: Principles: Life and Work by Ray Dalio
    Book 13: The Magic of Thinking Big by David J. Schwartz
    Book 14: Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything by Steven D. Levitt
    Book 15: Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk by Michael Sincere
    Book 16: Predictably Irrational: The Hidden Forces that Shape Our Decisions by Dan Ariely
    Book 17: Eat That Frog!: 21 Great Ways to Stop Procrastinating and Get More Done in Less Time. Edition 3 by Brian Tracy
    Book 18: Summary: Think and Grow Rich by Nine99 Innovation Lab
    Book 19: Personal Success (The Brian Tracy Success Library) by Brian Tracy
    Book 20: The Essentials of Finance and Accounting for Nonfinancial Managers by Edward Fields
    Book 21: Financial Statements. Revised and Expanded Edition: A Step-by-Step Guide to Understanding and Creating Financial Reports by Thomas Ittelson
    Book 22: Platform: Get Noticed in a Noisy World by Michael Hyatt
    """
    doc = open("google_books_dataset.csv", "r")
    x=1
    for line in doc:
        line = line.split(",")
        category = line[5]
        if category==cat: 
            x+=1
    print("The category", cat, "has", x-1, "books. This is the list of books:")
    x=1    
    
    doc.close()
    doc = open("google_books_dataset.csv", "r")
    for line in doc:

        line = line.split(",")
        title = line[0]
        author = line[1]
        category = line[5]
        if category==cat: 
            print("Book", str(x) + ":" , title, "by", author)
            x+=1
            
    doc.close()
#=================================Function #4===================================
def get_books_by_rate(library:str, rate:float) -> list[str]:
    """ This function displays the books of an inputted rate.
    >>> 
    There are 19 books whose rate is between 3.0 and 4.0 This is the list of books:
    Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    Book 2: Bring Me Back by B A Paris
    Book 3: How to Understand Business Finance: Edition 2 by Bob Cinnamon
    Book 4: Bring Me Back by B A Paris
    Book 5: The Infinite Game by Simon Sinek
    Book 6: Mrs. Pollifax Unveiled by Dorothy Gilman
    Book 7: Bring Me Back by B A Paris
    Book 8: How to Understand Business Finance: Edition 2 by Bob Cinnamon
    Book 9: The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    Book 10: Selling 101: What Every Successful Sales Professional Needs to Know by Zig Ziglar
    Book 11: The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    Book 12: Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything by Steven D. Levitt
    Book 13: The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    Book 14: Mrs. Pollifax Unveiled by Dorothy Gilman
    Book 15: Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything by Steven D. Levitt
    Book 16: The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    Book 17: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    Book 18: The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    Book 19: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    
    """
    result_dict = {}
    for category in library:
        book_list = library.get(category)
        for book in book_list:
            if book["rating"] != "N/A":
                rating = int(book["rating"])
                if rating == rate:
                    if category not in result_dict:
                        result_dict[category] = []
                    result_dict[category].append(book)
                    
    x = 0
    i = 1
    for book_list in result_dict:
        x += len(result_dict[book_list])
    print("There are",x,"books whose rate is between",rate,"and",rate+1,"these are the list of books:")
    for category in result_dict:
        book_list = result_dict.get(category)
        for book in book_list:
            print("Book", i, " :", book['title'], "by", book['author'])
            i += 1
            
    return x    
        
        
#=================================Function #5===================================
def get_books_by_title(library: dict, book_title: str)->bool:
    """
    Returns a bool that shows whether the title is in the dictionary or not.
    >>>get_books_by_title('google_books_dataset.csv',"Antiques Roadkill: A Trash 'n' Treasures Mystery")
    "The book has been found"
    True
    >>>get_books_by_title('google_books_dataset.csv',"Linear Algebra and its applications")
    "The book has NOT been found"
    False
    """
    for category in library.keys():
            books = library.get(category)
            for book in books:
                book_name = book['title']
                if book_name == book_title:
                    print ("The book has been found")
                    return True
    
    print ("The book has NOT been found")
    return False    
#=================================Function #6===================================
def get_books_by_author(dictionary:dict, author:str)->int:
    """
    Returns the number of books published by the author and prints out the respective title and rating.
    >>>get_books_by_author('google_books_dataset.csv',"Barbara Allan")
    The author "Barbara Allan" has published the following books:
    Book 1: Antiques Roadkill: A Trash 'n' Treasures Mystery , rate: 3.3
    Book 2: Antiques Chop, rate: 4.5
    """   
    counter = 0
    title_name = []
    other_counter = 0
    value = True
    print("The author",author,"has published the following book(s):")
    for item in dictionary:
        categories = dictionary[item]
        for dictionaries in categories:
            doub_check = 0
            author_name = dictionaries.get('author')
            topic = dictionaries.get('title')
            if other_counter > 0:
                while doub_check < len(title_name):
                    if topic == title_name[doub_check]:
                        value = False
                    doub_check+=1
                              
            if author_name==author and value == True:
                counter = counter + 1
                rating=dictionaries.get('rating')
                print("Book", counter, ":", topic, ", rating:",rating)
                title_name.append(topic)
        other_counter += 1
                  
    return counter
#=================================Function #7===================================
def get_books_by_publisher(dictionary:dict, publisher_name:str)->str:
    '''
    Returns a list of of the books (with their corresponding author) of all the books in the given dictionary published
    by the input publisher name.
    
    Precondition: the first input parameter of this function is the dictionary, and the second input parameter of this 
    function is a string

    >>>get_books_by_publisher(book_category_dictionary('google_books_dataset.csv') , 'Kensington Publishing Corp.')
    The Publisher Kensington Publishing Corp. has published the following books:
    Book 1: Antiques Knock-Off by Barbara Allan
    Book 2: Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan

    >>>get_books_by_publisher(book_category_dictionary('google_books_dataset.csv') , 'Crown Business')
    The Publisher Crown Business has published the following books:
    Book 1: Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader by Brent Schlender

    >>>get_books_by_publisher(book_category_dictionary('google_books_dataset.csv') , 'Hachette UK')
    The Publisher Hachette UK has published the following books:
    Book 1: Sword of Destiny: Witcher 2: Tales of the Witcher by Andrzej Sapkowski
    Book 2: The Way Of Shadows: Book 1 of the Night Angel by Brent Weeks
    Book 3: The Malady and Other Stories: An Andrzej Sapkowski Sampler by Andrzej Sapkowski
    Book 4: Tall Tales and Wee Stories: The Best of Billy Connolly by Billy Connolly
    Book 5: The Guardians: The explosive new thriller from international bestseller John Grisham by John Grisham
    Book 6: The Malady and Other Stories: An Andrzej Sapkowski Sampler by Andrzej Sapkowski
    Book 7: The Name of the Wind: The Kingkiller Chronicle:Book 1 by Patrick Rothfuss
    Book 8: The Tower of the Swallow: Witcher 6 by Andrzej Sapkowski
    Book 9: The Way Of Shadows: Book 1 of the Night Angel by Brent Weeks
    Book 10: The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    Book 11: Sword of Destiny: Witcher 2: Tales of the Witcher by Andrzej Sapkowski
    Book 12: Sword of Destiny: Witcher 2: Tales of the Witcher by Andrzej Sapkowski
    '''    
    counter = 0
    publisher = []
    publisher_set = set()
    for sub_category in dictionary.keys(): 
        for publish in range(len(dictionary[sub_category])):
            if (dictionary[sub_category][publish]["publisher"]) == publisher_name:
                publisher.append(dictionary[sub_category][publish])
       
    for sub_category1 in publisher: 
        publisher_set.add(sub_category1["title"])
        counter = len(publisher_set)
    print("\nThe Publisher", publisher_name, "has published the following books:")
    
    for sub_cat in range(len(publisher_set)):
        publisher1 = sub_cat + 1
        print("Book "+str(publisher1)+": "+str(publisher[sub_cat]["title"])+" by "+str(publisher[sub_cat]["author"]))
                 
    return str(counter)

#=================================Function #8===================================
def get_all_categories_for_book_title(dictionary: dict, all_books_name: str)->int: 
    """
    The function returns the number of categories associated with the given title. 
    
>>> get_all_categories_for_book_title(book_category_dictionary('google_books_dataset.csv'), "We")
    
The book title ' We ' belongs to the following categories:
Category 1 : Fiction
Category 2 : Fantasy
2

>>> get_all_categories_for_book_title(book_category_dictionary('google_books_dataset.csv'), "No")
The book title ' No ' belongs to the following categories:
0
    
>>> get_all_categories_for_book_title(book_category_dictionary('google_books_dataset.csv'), "Tall Tales and Wee Stories: The Best of Billy Connolly")
Category 1 : Biography
Category 2 : Humor
2
        
        """    
    list_categories = []
    counter = 0
    for category in dictionary.keys():
        books = dictionary.get(category)
        for library in books:
            book_title = library['title']
            if book_title == all_books_name:
                if not category in list_categories: 
                    list_categories.append(category)
                    counter +=1
                    
    print( "The book title '", all_books_name, "' belongs to the following categories:")
    for i in range(0,len(list_categories)):
        print("Category", i+1,":" ,list_categories[i]) 
    
    return counter


