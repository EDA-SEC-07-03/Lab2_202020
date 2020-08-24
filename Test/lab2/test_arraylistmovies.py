import pytest 
import config 
import csv
from DataStructures import arraylist as slt



def cmpfunction (element1, element2):
    if element1["book_id"] == element2["book_id"]:
        return 0
    elif element1["book_id"] < element2["book_id"]:
        return -1
    else:
        return 1

@pytest.fixture
def listax (file="Data/GoodReads/books-small.csv", sep=";"):
    lst = slt.newList(cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                slt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


@pytest.fixture
def books ():
    books = []
    books.append({"book_id":2,"goodreads_book_id":3,"best_book_id":3,"work_id":4640799,"books_count":491,"isbn":2439554934,"isbn13":29.78043955493e+12,"authors":"J.K. Rowling, Mary GrandPré","original_publication_year":1997.0,"original_title":"Harry Potter and the Philosopher's Stone","title":"Harry Potter and the Sorcerer's Stone (Harry Potter), #1)","language_code":"eng","average_rating":4.44,"ratings_count":4602479,"work_ratings_count":4800065,"work_text_reviews_count":75867,"ratings_1":75504,"ratings_2":101676,"ratings_3":455024,"ratings_4":1156318,"ratings_5":3011543,"image_url":"https://images.gr-assets.com/books/1474154022m/3.jpg","small_image_url":"https://images.gr-assets.com/books/1474154022s/3.jpg"})
    books.append({"book_id":1,"goodreads_book_id":3836,"best_book_id":14243723,"work_id":9,"books_count":2,"isbn":2,"isbn13":2,"authors":"Miguel de Cervantes Saavedra, Roberto González Echevarría, John Rutherford","original_publication_year":1,"original_title":1,"title":1,"language_code":1,"average_rating":1,"ratings_count":1,"work_ratings_count":1,"work_text_reviews_count":1,"ratings_1":1,"ratings_2":1,"ratings_3":1,"ratings_4":1,"ratings_5":1,"image_url":1,"small_image_url":1})
    books.append({"book_id":2,"goodreads_book_id":45107,"best_book_id":6480098,"work_id":9,"books_count":3,"isbn":3,"isbn13":3,"authors":"Robin Hobb","original_publication_year":2,"original_title":2,"title":2,"language_code":2,"average_rating":2,"ratings_count":2,"work_ratings_count":2,"work_text_reviews_count":2,"ratings_1":2,"ratings_2":2,"ratings_3":2,"ratings_4":2,"ratings_5":2,"image_url":2,"small_image_url":2})
    books.append({"book_id":3,"goodreads_book_id":8695,"best_book_id":345418921,"work_id":9,"books_count":4,"isbn":4,"isbn13":4,"authors":"Douglas Adams","original_publication_year":3,"original_title":3,"title":3,"language_code":3,"average_rating":3,"ratings_count":3,"work_ratings_count":3,"work_text_reviews_count":3,"ratings_1":3,"ratings_2":3,"ratings_3":3,"ratings_4":3,"ratings_5":3,"image_url":3,"small_image_url":3})
    books.append({"book_id":14,"goodreads_book_id":7613,"best_book_id":7613,"work_id":2207778,"books_count":896,"isbn":452284244,"isbn13":9.78045228424e+12,"authors":"George Orwell","original_publication_year":1945.0,"original_title":"Animal Farm: A Fairy Story","title":"Animal Farm","language_code":"eng","average_rating":3.87,"ratings_count":1881700,"work_ratings_count":1982987,"work_text_reviews_count":35472,"ratings_1":366854,"ratings_2":3135147,"ratings_3":3433432,"ratings_4":3698642,"ratings_5":3648912,"image_url":"https://images.gr-assets.com/books/1424037542m/7613.jpg","small_image_url":"https://images.gr-assets.com/books/1424037542s/7613.jpg"})
    print (books[0])
    return books

@pytest.fixture
def lstbooks(books):
    lst = slt.newList(cmpfunction)
    for i in range(0,len(books)):    
        slt.addLast(lst,books[i])    
    return lst


def test_No_empty (listax):
    assert slt.isEmpty(listax) == False
    assert slt.size(listax) > 0



def test_addFirst (listax, books):
    assert slt.isEmpty(listax) == False
    assert slt.size(listax) > 0
    ant=slt.size(listax)
    slt.addFirst (listax, books[1])
    assert slt.size(listax) == ant+1
    ant+=1
    slt.addFirst (listax, books[2])
    assert slt.size(listax) == ant+1
    book = slt.firstElement(listax)
    assert book == books[2]




def test_addLast (listax, books):
    assert slt.isEmpty(listax) == False
    assert slt.size(listax) > 0
    added=slt.size(listax)
    slt.addLast (listax, books[1])
    assert slt.size(listax) > added
    added+=1
    slt.addLast (listax, books[2])
    assert slt.size(listax) > added
    book = slt.lastElement(listax)
    assert book == books[2]




def test_getElement(lstbooks,books):
    book = slt.getElement(lstbooks, 14)
    assert book == books[4]


def test_removeFirst (lstbooks, books):
    assert slt.size(lstbooks) == 149
    slt.removeFirst(lstbooks)
    assert slt.size(lstbooks) == 148
    book = slt.getElement(lstbooks, 1)
    assert book  == books[3]



def test_removeLast (lstbooks, books):
    assert slt.size(lstbooks) == 5
    slt.removeLast(lstbooks)
    assert slt.size(lstbooks) == 4
    book = slt.getElement(lstbooks, 4)
    assert book  == books[3]



def test_insertElement (lst, books):
    assert slt.isEmpty(lst) is True
    assert slt.size(lst) == 0
    slt.insertElement (lst, books[0], 1)
    assert slt.size(lst) == 1
    slt.insertElement (lst, books[1], 2)
    assert slt.size(lst) == 2
    slt.insertElement (lst, books[2], 1)
    assert slt.size(lst) == 3
    book = slt.getElement(lst, 1)
    assert book == books[2]
    book = slt.getElement(lst, 2)
    assert book == books[0]



def test_isPresent (lstbooks, books):
    book = {'book_id':'10', 'book_title':'Title 10', 'author':'author 10'}
    print(slt.isPresent (lstbooks, books[2]))
    assert slt.isPresent (lstbooks, books[2]) > 0
    assert slt.isPresent (lstbooks, book) == 0
    


def test_deleteElement (lstbooks, books):
    pos = slt.isPresent (lstbooks, books[2])
    assert pos > 0
    book = slt.getElement(lstbooks, pos)
    assert book == books[2]
    slt.deleteElement (lstbooks, pos)
    assert slt.size(lstbooks) == 4
    book = slt.getElement(lstbooks, pos)
    assert book == books[3]


def test_changeInfo (lstbooks):
    book10 = {'book_id':'10', 'book_title':'Title 10', 'author':'author 10'}
    slt.changeInfo (lstbooks, 1, book10)
    book = slt.getElement(lstbooks, 1)
    assert book10 == book


def test_exchange (lstbooks, books):
    book1 = slt.getElement(lstbooks, 1)
    book5 = slt.getElement(lstbooks, 5)
    slt.exchange (lstbooks, 1, 5)
    assert slt.getElement(lstbooks, 1) == book5
    assert slt.getElement(lstbooks, 5) == book1