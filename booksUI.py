#Date: April 12, 2022
#Version: 1.0
#By: Prem Patel
from load_data import book_category_dictionary
from fun import book_add,remove_book,get_books_by_title,get_books_by_rate,get_books_by_author,get_books_by_publisher,get_books_by_category,get_all_categories_for_book_title
from sorting_fun import sort_books_title,sort_books_ascending_rate,sort_books_publisher,sort_books_author 

#User Interface 
def commands():
    """
    Returns the UI interface commands
    
    >>> commands():
    The avaiable commands are:
    1- L)oad data
    2- A)dd book
    3- R)emove book
    4- G)et books
    5- GCT) Get all categories for book title
    6- S)ort books
    7- Q)uit
    
    Returns the load data file of the selected csv file
    
    >>> commands()
    "Please enter the load data file command: "
    google_books_dataset.csv
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page': 288},..}
    
    >> commands()
    "Enter a command: "
    GCT
    Enter Title Name: The Essentials of Finance and Accounting for Nonfinancial Managers
    The book title ' The Essentials of Finance and Accounting for Nonfinancial Managers ' belongs to the following categories:
    Category 1 : Money Management
    Category 2 : Investing
    
    >>> commands()
    "Enter a command: "
    Q
    Quitting
    
    """
    print("\nThe avaiable commands are:\n  1- L)oad data\n  2- A)dd book\n  3- R)emove book\n  4- G)et books")
    print("  5- GCT) Get all categories for book title\n  6- S)ort books\n  7- Q)uit\n")
    
    userinput = None
    valid_filename = False
    while userinput not in ["L", "l"]:
        userinput = input("Please enter the load data file command: ")
        if userinput.upper() == "L":
            while not valid_filename:
                bookinput = input("Enter File name.csv: ")
                if bookinput.split(".")[-1] == "csv":
                    dictionary = book_category_dictionary(bookinput)
                    print("\nHere is the load data file: ")
                    print(dictionary)
                    valid_filename = True
                else:
                    print("\nIncorrect load data file, Please try again\n")
        elif userinput.upper() != "L":
            print("No file loaded")
    
    exit = False
    while not exit:
        userinput = input("\nEnter a command: ").upper()
        if userinput == "A":
            Title = input("\nEnter Title: ")
            Author = input("Enter Author: ")
            Language = input("Enter Language: ")
            Publisher = input("Enter Publisher: ")
            Category = input("Enter Category: ")
            Rate = input("Enter Rating: ")
            Page = input("Enter Page: ")
    
            if '' in [Title, Author, Language, Publisher, Category, Rate, Page]:
                print("")
            else:
                value = (Title,Author,Rate,Publisher,Page,Category,Language)
                books = book_add(book_category_dictionary(bookinput),(value))
    
        elif userinput == "R":
            title1 = input("\nEnter Title: ")
            category1 = input("Enter Category: ")
            if '' in [title1,category1]:
                print("")
            else:
                remove = remove_book(book_category_dictionary(bookinput),title1,category1)
                
        elif userinput.upper() == "G":
            print("\nHow would you like to sort the data?")
            print("\nT)itle   R)ate   A)uthor   P)ublisher   C)ategory\n")
            
            while userinput.upper() not in ["T","R","A","P","C"]:
                userinput = input("Enter a sub-command: ")
                
                if userinput.upper() == "T":
                    title_input = input("Enter Title Name: ")
                    category = book_category_dictionary(bookinput)
                    book_title = get_books_by_title(category, title_input)            
                    
                elif userinput.upper() == "R":
                    rate_input = float(input("Enter Rate: "))
                    category = book_category_dictionary(bookinput)
                    book_rate = get_books_by_rate(category,rate_input)
                    
                elif userinput.upper() == "A":
                    author_input = input("Enter Author Name: ")
                    category = book_category_dictionary(bookinput)
                    book_author = get_books_by_author(category,author_input)
                                     
                elif userinput.upper() == "P":
                    publisher_input = input("Enter Publisher Name: ")
                    category = book_category_dictionary(bookinput)
                    book_publisher = get_books_by_publisher(category,publisher_input)
                
                elif userinput.upper() == "C":
                    category_input = input("Enter Category: ")
                    category = book_category_dictionary(bookinput)
                    book_category = get_books_by_category(category,category_input)
                    
        elif userinput.upper() == "GCT":
            title_name = input("Enter Title Name: ")
            if '' in [title_name]:
                print("")
            else:
                category_title =  get_all_categories_for_book_title(book_category_dictionary(bookinput),title_name)        
             
        elif userinput.upper() == "S":
            print("\nHow would you like to sort the data?")
            print("\nT)itle   R)ate   P)ublisher   A)uthor\n")
            
            while userinput.upper() not in ["T","R","P","A"]:
                userinput = input("Enter a sub-command: ")
                if userinput.upper() == "T":
                    book_title1 = sort_books_title(book_category_dictionary(bookinput))
                    print("\nSorting books by title:")
                    print(book_title1)
                    
                elif userinput.upper() == "R":
                    book_rate1 = sort_books_ascending_rate(book_category_dictionary(bookinput))
                    print("\nSorting books by rate:")
                    print(book_rate1)
                    
                elif userinput.upper() == "P":
                    book_publisher1 = sort_books_publisher(book_category_dictionary(bookinput))
                    print("\nSorting books by publisher:")
                    print(book_publisher1)                
                    
                elif userinput.upper() == "A":
                    book_author1 = sort_books_author(book_category_dictionary(bookinput))
                    print("\nSorting books by author:")
                    print(book_author1)    
    
        elif userinput == "Q":
            exit = True
            print("Quitting")
        else:
            print ("\nIncorrect command, please try again.")

commands()

