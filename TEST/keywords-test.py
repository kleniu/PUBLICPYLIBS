#!/usr/bin/env python
# coding:utf-8
u"""The Utility for testing library libkeywords.py.

DO NOT forget to export PYTHONPATH with directory
containing libkeywords.py before you run this script
"""
import libkeywords
import libfprint


def testme():
    u"""Just for tests."""
    print "### This is a test of " + __file__
    testtxt = u"""This is a file with .NET framework (a.k.a DOTNET
) Java and node.js interpreters, plus C# language. Django is the framework
as spring and AngularJS."""

    print "\n### TEST 1 Keywords search test"
    keywords = libkeywords.load_keywords_def('./PRIVATE/keywords.json')
    result = libkeywords.detect_keywords(testtxt, keywords)
    print "### raw output: ", result

    print "\n### TEST 2 CSV formated output"
    print "#-BEGIN-#"
    print libkeywords.print_keywords_csv(result, '|')
    print "#-=END=-#"

    print "\n### TEST 3 JSON formated prettified output"
    print "#-BEGIN-#"
    print libkeywords.print_keywords_json(result, prettify=True)
    print "#-=END=-#"

    print "\n### TEST 4 JSON formated output"
    print "#-BEGIN-#"
    print libkeywords.print_keywords_json(result)
    print "#-=END=-#"

    print "\n### TEST 5 Taging text"
    print "#-BEGIN-#"
    tagged_text = libkeywords.tag_keywords(testtxt, keywords, "GREEN")
    print tagged_text.encode('utf-8')
    libfprint.ctaggedprint(tagged_text)
    print "#-=END=-#"

if __name__ == "__main__":
    testme()
