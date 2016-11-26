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
    print "   It can be any test."
    print "-d keyword_deffinition_file"
    print "   It can be any file in json or yaml format."
    print "-of [json|csv|yaml]"
    print "   The format of the output data."


def do_it(txt, def_file, fmt, def_file_format):
    u"""Function generates required output."""
    if def_file_format == u"json":
        keywords = libkeywords.load_keywords_json(def_file)
    elif def_file_format == u"yaml":
        keywords = libkeywords.load_keywords_yaml(def_file)
    else:
        print "Unknown format name : " + def_file_format
        return
    result = libkeywords.detect_keywords(txt, keywords)
    if fmt == u"csv":
        print libkeywords.dump_keywords_csv(result, '|')
    elif fmt == u"json":
        print libkeywords.dump_keywords_json(result)
    elif fmt == u"yaml":
        print libkeywords.dump_keywords_yaml(result)


def main():
    u"""Main function."""
    try:
        script_opts, script_args = getopt.getopt(sys.argv[1:], "t:d:of:")
    except getopt.GetoptError as e:
        print(str(e))
        print_usage()
        sys.exit(1)

    txt = u""
    def_json = u""
    outfmt = u""

    for o, a in script_opts:
        if o == '-t':
            txt = a
        elif o == '-d':
            def_file = a
        elif o == '-f':
            outfmt = a
            # print outfmt
    if def_file == u"":
        print_usage()
        print "EMPTY keywords definition file name! Check -d option."
        sys.exit(1)
    elif outfmt != u"json" and outfmt != u"csv" and outfmt != u"yaml":
        print_usage()
        print "BAD format! Check -f option."
        sys.exit(1)
    else:
        def_file_format = libkeywords.detect_keywords_filedef_format(def_file)
        if len(def_file_format) == 0:
            print_usage()
            print "BAD keyword definition file format. Check file : " + def_file
            sys.exit(2)

    # print "text: >%s<; def_file: >%s<; format: >%s<" % (txt, def_json, fmt)
    do_it(txt, def_file, outfmt, def_file_format)

if __name__ == "__main__":
    main()
