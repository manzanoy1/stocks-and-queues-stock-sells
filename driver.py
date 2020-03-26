#Yanira Manzano
#3/25/2020

from queue_code import *

#queue Driver

def test_shift():
    colors = Queue()
    colors.shift("Apple")
    assert colors.count() == 1
    colors.shift("Banana")
    assert colors.count() == 2

def test_unshift():
    colors = Queue()
    colors.shift("Blue")
    colors.shift("Black")
    assert colors.unshift() == "Blue"
    assert colors.unshift() == "Black"
    assert colors.unshift() == None

def test_first():
    colors = Queue()
    colors.shift("Couch")
    assert colors.first() == "Couch"
    colors.shift("Table")
    assert colors.first() == "Table"
    colors.shift("Chair")
    assert colors.first() == "Chair"

def test_drop():
    colors = Queue()
    colors.shift("Couch")
    colors.shift("Table")
    assert colors.count() == 2
    colors.drop()
    assert colors.count() == 1
    assert colors.first() == "Couch"
    colors.drop()
    assert colors.first() == None
