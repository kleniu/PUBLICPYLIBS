#!/usr/bin/env python
# coding:utf-8
u"""The first lib."""
import json
import codecs


def load_keywords(file_name):
    u"""Funkcja orczytuje JSON z definicją keywordów."""
    with codecs.open(file_name, 'r', encoding='UTF-8') as my_file:
        return json.load(my_file)


def detect_keywords(mytext, keywords):
    u"""Funkcja sprawdza czy występują zdefiniowane w 2 argumencie keywordy."""
    ret_val = {}
    for type_name in keywords:
        type_def = keywords[type_name]
        ret_val[type_name] = []
        for keyword_name in type_def:
            keyword_def = type_def[keyword_name]
            for keyword_alias in keyword_def:
                # to jest właściwe sprawdzenie czy keyword występuje
                # print "keyword_alias", keyword_alias
                if keyword_alias in mytext:
                    # print "%s|%s" % (type_name, keyword_name)
                    ret_val[type_name].append(keyword_name)
                    break
    return ret_val

if __name__ == "__main__":
    def testme():
        u"""Just for tests."""
        print "### This is a test of " + __file__
        testtxt = u"""
		Java node.js C# django
        """
        print "### Keywords search test"
        file_keywords = load_keywords('../../MYCORPUS/keywords.json')
        print detect_keywords(testtxt, file_keywords)
    testme()
