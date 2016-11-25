#!/usr/bin/env python
# coding:utf-8
u"""The Utility used for detecting keywords in text.

DO NOT forget to export PYTHONPATH with directory
containing libkeywords.py before you run this script
"""
import libkeywords
import sys
import getopt


def print_usage():
    u"""Function prints usage including options and arguments."""
    print "Srtipt %s" % __file__
    print "Required options:"
    print "-t text_to_be_examined"
    print "-d json_keyword_deffinition_file"
    print "-f [json|csv]"


def do_it(txt, def_json, fmt):
    u"""Function generates required output."""
    keywords = libkeywords.load_keywords_def(def_json)
    result = libkeywords.detect_keywords(txt, keywords)
    if fmt == u"csv":
        print libkeywords.print_keywords_csv(result, '|')
    elif fmt == u"json":
        print libkeywords.print_keywords_json(result, prettify=True)


def main():
    u"""Main function."""
    try:
        script_opts, script_args = getopt.getopt(sys.argv[1:], "t:d:f:")
    except getopt.GetoptError as e:
        print(str(e))
        print_usage()
        sys.exit(1)

    txt = u""
    def_json = u""
    fmt = u""

    for o, a in script_opts:
        if o == '-t':
            txt = a
        elif o == '-d':
            def_json = a
        elif o == '-f':
            fmt = a
    if def_json == u"":
        print_usage()
        print "EMPTY keywords definition file name! Check -d option."
        sys.exit(1)
    elif fmt != u"json" or fmt != u"csv":
        print_usage()
        print "BAD format! Check -f option."
        sys.exit(1)

    # print "text: >%s<; def_file: >%s<; format: >%s<" % (txt, def_json, fmt)
    do_it(txt, def_json, fmt)

if __name__ == "__main__":
    main()
