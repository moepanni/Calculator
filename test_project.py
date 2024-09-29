from tkinter import Tk, Entry
from project import backspace, clear, calc_expression


def test_calc_expression():
    assert calc_expression('1+1') == '2'
    assert calc_expression('2*3') == '6'
    assert calc_expression('4/2') == '2.0'
    assert calc_expression('2**3') == '8'
    assert calc_expression('1/0') == 'Error: Divide by 0'
    assert calc_expression('abc') == 'Error'


def test_backspace():
    root = Tk()
    entry = Entry(root)
    entry.insert(0, '12345')
    backspace(entry)
    assert entry.get() == '1234'
    root.destroy()


def test_clear():
    root = Tk()
    entry = Entry(root)
    entry.insert(0, '12345')
    clear(entry)
    assert entry.get() == ''
    root.destroy()
