from database import *

class Books(dB):
    def __init__(self):
        books = {}
        books['book_id'] = dB.book_id+1
        dB.book_id+=1
        books['book_title'] = 'Book 1'
        books['author_name'] = 'Andrew Thomas'
        books['total_page'] = 120
        books['available_copy'] = 40
        books['ISBN'] = 1234567654343
        books['published_year'] = 2001
        dB.book_collection.append(books) 

        books = {}
        books['book_id'] = dB.book_id+1
        dB.book_id+=1
        books['book_title'] = 'Book 2'
        books['author_name'] = 'Helen Thomas'
        books['total_page'] = 125
        books['available_copy'] = 10
        books['ISBN'] = 8787674565354
        books['published_year'] = 2002
        dB.book_collection.append(books) 

        books = {}
        books['book_id'] = dB.book_id+1
        dB.book_id+=1
        books['book_title'] = 'Book 3'
        books['author_name'] = 'Jacob Thomas'
        books['total_page'] = 139
        books['available_copy'] = 20
        books['ISBN'] = 1234987654343
        books['published_year'] = 2003
        dB.book_collection.append(books) 

        books = {}
        books['book_id'] = dB.book_id+1
        dB.book_id+=1
        books['book_title'] = 'Book 4'
        books['author_name'] = 'Kalam James'
        books['total_page'] = 150
        books['available_copy'] = 5
        books['ISBN'] = 1234567623343
        books['published_year'] = 2004
        dB.book_collection.append(books) 

        books = {}
        books['book_id'] = dB.book_id+1
        dB.book_id+=1
        books['book_title'] = 'Book 5'
        books['author_name'] = 'James Thomas'
        books['total_page'] = 110
        books['available_copy'] = 0
        books['ISBN'] = 1234567654346
        books['published_year'] = 2005
        dB.book_collection.append(books) 

        books = {}
        books['book_id'] = dB.book_id+1
        dB.book_id+=1
        books['book_title'] = 'Book 6'
        books['author_name'] = 'Pascal Thomas'
        books['total_page'] = 190
        books['available_copy'] = 10
        books['ISBN'] = 1234567654843
        books['published_year'] = 2006
        dB.book_collection.append(books) 

        books = {}
        books['book_id'] = dB.book_id+1
        dB.book_id+=1
        books['book_title'] = 'Book 7'
        books['author_name'] = 'Richie Thomas'
        books['total_page'] = 120
        books['available_copy'] = 4
        books['ISBN'] = 1234567954343
        books['published_year'] = 2007
        dB.book_collection.append(books) 

        books = {}
        books['book_id'] = dB.book_id+1
        dB.book_id+=1
        books['book_title'] = 'Book 8'
        books['author_name'] = 'Andrew Dennis'
        books['total_page'] = 200
        books['available_copy'] = 30
        books['ISBN'] = 1234567654943
        books['published_year'] = 2008
        dB.book_collection.append(books) 

        books = {}
        books['book_id'] = dB.book_id+1
        dB.book_id+=1
        books['book_title'] = 'Book 9'
        books['author_name'] = 'Thomas Thomas'
        books['total_page'] = 120
        books['available_copy'] = 40
        books['ISBN'] = 1234567004343
        books['published_year'] = 2009
        dB.book_collection.append(books) 

        books = {}
        books['book_id'] = dB.book_id+1
        dB.book_id+=1
        books['book_title'] = 'Book 10'
        books['author_name'] = 'Andrew Kosling'
        books['total_page'] = 120
        books['available_copy'] = 40
        books['ISBN'] = 1234986654343
        books['published_year'] = 2010
        dB.book_collection.append(books) 