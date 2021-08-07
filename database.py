#Database for books, borower lists, users, histry
class dB:
    #For all books in the library
    book_collection = []
    #Book Id's starting from 1000
    book_id = 1000
    #For storing all users
    users_dB = []
    #To temporarily store requested books till admin approves
    requested_books = []
    #To store history for admin
    borrower_list = []
    #To store history for users
    users_borrowing_history = []
    #Teporary book  list
    return_book = []
