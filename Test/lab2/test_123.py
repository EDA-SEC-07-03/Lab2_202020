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
def lst(file="Data/GoodReads/books-small.csv", sep=";"):
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
    "book_id","goodreads_book_id","best_book_id","work_id","books_count","isbn","isbn13","authors","original_publication_year","original_title","title","language_code","average_rating","ratings_count","work_ratings_count","work_text_reviews_count","ratings_1","ratings_2","ratings_3","ratings_4","ratings_5","image_url","small_image_url"
    books.append({"book_id":1,"goodreads_book_id":2767052,"best_book_id":2767052,"work_id":2792775,"books_count":272,"isbn":439023483,"isbn13":9.78043902348e+12,"authors":"Suzanne Collins","original_publication_year":2008.0,"original_title":"The Hunger Games","title":"The Hunger Games (The Hunger Games, #1)","language_code":"eng","average_rating":4.34,"ratings_count":4780653,"work_ratings_count":4942365,"work_text_reviews_count":155254,"ratings_1":66715,"ratings_2":127936,"ratings_3":560092,"ratings_4":1481305,"ratings_5":2706317,"image_url":"https://images.gr-assets.com/books/1447303603m/2767052.jpg","small_image_url":"https://images.gr-assets.com/books/1447303603s/2767052.jpg"})
    books.append({"book_id":2,"goodreads_book_id":3,"best_book_id":3,"work_id":4640799,"books_count":491,"isbn":439554934,"isbn13":9.78043955493e+12,"authors":"J.K. Rowling, Mary GrandPré","original_publication_year":1997.0,"original_title":"Harry Potter and the Philosopher's Stone","title":"Harry Potter and the Sorcerer's Stone (Harry Potter, #1)","language_code":"eng","average_rating":4.44,"ratings_count":4602479,"work_ratings_count":4800065,"work_text_reviews_count":75867,"ratings_1":75504,"ratings_2":101676,"ratings_3":455024,"ratings_4":1156318,"ratings_5":3011543,"image_url":"https://images.gr-assets.com/books/1474154022m/3.jpg","small_image_url":"https://images.gr-assets.com/books/1474154022s/3.jpg"})
    books.append({"book_id":3,"goodreads_book_id":41865,"best_book_id":41865,"work_id":3212258,"books_count":226,"isbn":316015849,"isbn13":9.78031601584e+12,"authors":"Stephenie Meyer","original_publication_year":2005.0,"original_title":"Twilight","title":"Twilight (Twilight, #1)","language_code":"en-US","average_rating":3.57,"ratings_count":3866839,"work_ratings_count":3916824,"work_text_reviews_count":95009,"ratings_1":456191,"ratings_2":436802,"ratings_3":793319,"ratings_4":875073,"ratings_5":1355439,"image_url":"https://images.gr-assets.com/books/1361039443m/41865.jpg","small_image_url":"https://images.gr-assets.com/books/1361039443s/41865.jpg"})
    books.append({"book_id":46,"goodreads_book_id":2657,"best_book_id":2657,"work_id":3275794,"books_count":487,"isbn":61120081,"isbn13":9.78006112008e+12,"authors":"Harper Lee","original_publication_year":1960.0,"original_title":"To Kill a Mockingbird","title":"To Kill a Mockingbird","language_code":"eng","average_rating":4.25,"ratings_count":3198671,"work_ratings_count":3340896,"work_text_reviews_count":72586,"ratings_1":60427,"ratings_2":117415,"ratings_3":446835,"ratings_4":1001952,"ratings_5":1714267,"image_url":"https://images.gr-assets.com/books/1361975680m/2657.jpg","small_image_url":"https://images.gr-assets.com/books/1361975680s/2657.jpg"})
    books.append({"book_id":150,"goodreads_book_id":4671,"best_book_id":4671,"work_id":245494,"books_count":1356,"isbn":743273567,"isbn13":9.78074327356e+12,"authors":"F. Scott Fitzgerald","original_publication_year":1925.0,"original_title":"The Great Gatsby","title":"The Great Gatsby","language_code":"eng","average_rating":3.89,"ratings_count":2683664,"work_ratings_count":2773745,"work_text_reviews_count":51992,"ratings_1":86236,"ratings_2":197621,"ratings_3":606158,"ratings_4":936012,"ratings_5":947718,"image_url":"https://images.gr-assets.com/books/1490528560m/4671.jpg","small_image_url":"https://images.gr-assets.com/books/1490528560s/4671.jpg"})
    return books


@pytest.fixture
def lstbooks(books):
    lst = slt.newList(cmpfunction)
    for i in range(0,5):    
        slt.addLast(lst,books[i])    
    return lst



def test_No_empty (lst):
    assert slt.isEmpty(lst) == False
    assert slt.size(lst) > 0



def test_addFirst (lst, books):
    assert slt.isEmpty(lst) ==False 
    assert slt.size(lst) > 0
    slt.addFirst (lst, books[3])
    assert slt.size(lst) == 150
    slt.addFirst (lst, books[4])
    assert slt.size(lst) == 151
    book = slt.firstElement(lst)
    assert book == books[4]




def test_addLast (lst, books):
    assert slt.isEmpty(lst) == False
    assert slt.size(lst) == 149
    slt.addLast (lst, books[1])
    assert slt.size(lst) == 150
    




def test_getElement(lstbooks, books):
    book = slt.getElement(lstbooks, 1)
    assert book == books[0]
    book = slt.getElement(lstbooks, 5)
    assert book == books[4]



def test_removeFirst (lstbooks, books):
    assert slt.size(lstbooks) == 5
    slt.removeFirst(lstbooks)
    assert slt.size(lstbooks) == 4
    book = slt.getElement(lstbooks, 1)
    assert book  == books[1]



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
