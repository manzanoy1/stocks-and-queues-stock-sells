#Yanira Manzano
#3/25/2020

from queue_code import *

#queue Driver

def test_shift():
    colors = Queue()
    colors.shift("Hotdog")
    assert colors.count() == 1
    colors.shift("Banana")
    assert colors.count() == 2

def test_unshift():
    colors = Queue()
    colors.shift("Rose")
    colors.shift("Violet")
    assert colors.unshift() == "Rose"
    assert colors.unshift() == "Violet"
    assert colors.unshift() == None

def test_first():
    colors = Queue()
    colors.shift("Couch")
    assert colors.first() == "Couch"
    colors.shift("Table")
    assert colors.first() == "Table"
    colors.shift("Desk")
    assert colors.first() == "Desk"

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
