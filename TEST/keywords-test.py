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
as spring and AngularJS. File created by lazy developer."""

    print "\n### TEST 1 Keywords search test"
    keywords_json = libkeywords.load_keywords_json('../PRIVATE/keywords.json')
    result_json = libkeywords.detect_keywords(testtxt, keywords_json)
    keywords_yaml = libkeywords.load_keywords_yaml('../PRIVATE/keywords.yaml')
    result_yaml = libkeywords.detect_keywords(testtxt, keywords_yaml)
    print "### test text:"
    print "#-BEGIN-#"
    print testtxt
    print "#-=END=-#"
    print "### raw output of detected keywords in json:"
    print "#-BEGIN-#"
    print result_json
    print "#-=END=-#"
    print "### raw output of detected keywords in yaml:"
    print "#-BEGIN-#"
    print result_yaml
    print "#-=END=-#"

    # print "\n### TEST 1.1 print keywords loaded from json file"
    # print "#-BEGIN-#"
    # libkeywords.print_keywords_def(keywords_json)
    # print "#-=END=-#"

    # print "\n### TEST 1.2 print keywords loaded from yaml file"
    # print "#-BEGIN-#"
    # libkeywords.print_keywords_def(keywords_yaml)
    # print "#-=END=-#"

    print "\n### TEST 2 CSV formated output"
    print "#-BEGIN-#"
    print libkeywords.dump_keywords_csv(result_json, '|')
    print libkeywords.dump_keywords_csv(result_yaml, '|')
    print "#-=END=-#"

    print "\n### TEST 3 JSON formated prettified output"
    print "#-BEGIN json-#"
    print libkeywords.dump_keywords_json(result_json)
    print "#-=END json=-#"
    print "#-BEGIN yaml-#"
    print libkeywords.dump_keywords_json(result_yaml), "#####"
    print "#-=END= yaml-#"

    print "\n### TEST 4 YAML formated output"
    print "#-BEGIN json-#"
    print libkeywords.dump_keywords_yaml(result_json)
    print "#-=END json=-#"
    print "#-BEGIN yaml-#"
    print libkeywords.dump_keywords_yaml(result_yaml)
    print "#-=END yaml=-#"

    print "\n### TEST 5 tagging test"
    print "#-BEGIN-#"
    print libkeywords.tag_keywords(u".Net python this is text with java C#",
                                   keywords_json, "[", "]")
    print libkeywords.tag_keywords(u".Net python this is text with java C#",
                                   keywords_yaml, "[", "]")
    print "#-=END=-#"

    print "\n### TEST 6 Taging text"
    print "#-BEGIN-#"
    tagged_text_json = libkeywords.tag_keywords(testtxt, keywords_json,
                                           "<GREEN>", "</GREEN>")
    tagged_text_yaml = libkeywords.tag_keywords(testtxt, keywords_yaml,
                                           "<GREEN>", "</GREEN>")
    # print tagged_text.encode('utf-8')
    libfprint.ctaggedprint(tagged_text_json)
    libfprint.ctaggedprint(tagged_text_yaml)
    print "#-=END=-#"

if __name__ == "__main__":
    testme()
