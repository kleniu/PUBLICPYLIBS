#!/usr/bin/env python
# coding:utf-8
u"""The Utility for testing library libfprint.py.

DO NOT forget to export PYTHONPATH with directory
containing libkeywords.py before you run this script
"""
import libfprint as t


def testme():
    u"""Test function."""
    t.help()
    print "\n#### TEST 1"
    print "This is " + t.ct("none", u"normal") + " text"
    print "This is " + t.ct("red", u"red") + " text"
    print "This is " + t.ct("blue", "blue") + " text"
    print "This is " + t.ct("yellow", "yellow") + " text"
    print "This is " + t.ct("green", "green") + " text"

    print "\n#### TEST 2"
    t.cprint("none", u"This text is normal (śćół).")
    t.cprint("red", u"This text is red (śćół).")
    t.cprint("blue", "This text is blue (śćół).")
    t.cprint("yellow", "This text is yellow (śćół).")
    t.cprint("green", "This text is green (śćół).")
    print ""

    print "\n#### TEST 3"
    print repr(t.ct("red", u"red"))
    print repr(t.ct("blue", u"blue"))
    print repr(t.ct("yellow", u"yellow"))
    print repr(t.ct("green", u"green"))

    print "\n#### TEST 4"
    test_txt = u"""This is test string
used to check if <RED>red</RED> will
be red. (śćó) and <YELLOW>yellow
</YELLOW>will be yellow. And <BLUE>blue (óśćłę)</BLUE> will be
blue. <GREEN>This sentance is green</GREEN>.
"""
    print "BEGIN\n" + t.ctagged(test_txt) + "\nEND"

    print "\n#### TEST 5"
    t.ctaggedprint(test_txt)

    print "\n#### TEST 6"
    my_array = [["", "\nColumn 1", "Multi\nColumn 2", "Column 3"],
                ["Raw 1", "1", "2", "3"],
                ["Raw 2\n(multi)", "A1\nA2\nA3", "B", "C"],
                ["Raw 3", "I", "II", "III"]]
    print t.carray(my_array)

if __name__ == "__main__":
    testme()
