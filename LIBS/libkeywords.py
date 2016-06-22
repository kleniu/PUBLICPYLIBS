#!/usr/bin/env python
# coding:utf-8
u"""The first lib."""
import json
import codecs
import re


def load_keywords_def(file_name):
    u"""Function reads the JSON file with the definition of keywords."""
    u"""The format of the keywords JSON file:
        {
            "keyword_group_name1": {
                "keyword1": [ "reg_exp1_g1k1"
                              "reg_exp2_g1k1",
                              ...
                          ]
                ...
            }
            ...
        }
    """
    with codecs.open(file_name, 'r', encoding='UTF-8') as my_file:
        keywords = json.load(my_file)
    # compile all regexps
    for group_name in keywords:
        group_def = keywords[group_name]
        for keyword_name in group_def:
            reg_exp_def_list = group_def[keyword_name]
            reg_exp_obj_list = []
            for reg_exp_def in reg_exp_def_list:
                # print group_name, keyword_name, reg_exp_def
                reg_exp_obj = re.compile('.*' + reg_exp_def + '.*',
                                         re.DOTALL)
                reg_exp_obj_list.append(reg_exp_obj)
            group_def[keyword_name] = reg_exp_obj_list
            # print group_def[keyword_name]
    return keywords


def print_keywords_def(keywords):
    u"""Function prints compiled reg_exps definitions."""
    for group_name in keywords:
        group_def = keywords[group_name]
        for keyword_name in group_def:
            reg_exp_obj_list = group_def[keyword_name]
            for reg_exp_obj in reg_exp_obj_list:
                print group_name, keyword_name, reg_exp_obj.pattern


def detect_keywords(mytext, keywords):
    u"""Function checks if keywords has been found in the text."""
    ret_val = {}
    for group_name in keywords:
        group_def = keywords[group_name]
        ret_val[group_name] = []
        for keyword_name in group_def:
            reg_exp_obj_list = group_def[keyword_name]
            for reg_exp_obj in reg_exp_obj_list:
                # print "pattern: ", reg_exp_obj.pattern
                m = reg_exp_obj.match(mytext)
                if m:
                    # print "%s|%s" % (group_name, keyword_name)
                    ret_val[group_name].append(keyword_name)
                    break
    return ret_val


def testme():
    u"""Just for tests."""
    print "### This is a test of " + __file__
    testtxt = u"""
    Java node.js C# django
    """
    print "### Keywords search test"
    keywords = load_keywords_def('./TEST/keywords.json')
    # print_keywords_def(keywords)
    print detect_keywords(testtxt, keywords)

if __name__ == "__main__":
    testme()
