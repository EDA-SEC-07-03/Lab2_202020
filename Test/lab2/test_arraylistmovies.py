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
def lst (file="Data/GoodReads/books-small.csv", sep=";"):
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



def test_no_empty (lst):
    assert slt.isEmpty(lst) == False
    assert slt.size(lst) > 0



def test_addFirst (lst, books):
    assert slt.isEmpty(lst) == False
    assert slt.size(lst) > 0
    slt.addFirst (lst, books[1])
    assert slt.size(lst) == 1
    slt.addFirst (lst, books[2])
    assert slt.size(lst) == 2
    book = slt.firstElement(lst)
    assert book == books[2]




def test_addLast (lst, books):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addLast (lst, books[1])
    assert slt.size(lst) == 1
    slt.addLast (lst, books[2])
    assert slt.size(lst) == 2
    book = slt.firstElement(lst)
    assert book == books[1]
    book = slt.lastElement(lst)
    assert book == books[2]




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