#!/usr/bin/env python
# coding:utf-8
u"""The Utility for testing library libkeywords.py.

DO NOT forget to export PYTHONPATH with directory
containing libkeywords.py before you run this script
"""
import libkeywords


def testme():
    u"""Just for tests."""
    print "### This is a test of " + __file__
    testtxt = u""".NET
    Java node.js C# django
    spring AngularJS
    """
    print "### Keywords search test"
    keywords = libkeywords.load_keywords_def('./DATA/keywords.json')
    result = libkeywords.detect_keywords(testtxt, keywords)
    print "### raw output: ", result

    print "### CSV formated output"
    print "# BEGIN #"
    print libkeywords.print_keywords_csv(result, '|')
    print "#  END  #"

    print "### JSON formated prettified output"
    print "# BEGIN #"
    print libkeywords.print_keywords_json(result, prettify=True)
    print "#  END  #"

    print "### JSON formated output"
    print "# BEGIN #"
    print libkeywords.print_keywords_json(result)
    print "#  END  #"

if __name__ == "__main__":
    testme()
