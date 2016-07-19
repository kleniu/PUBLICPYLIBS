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
                # reg_exp_obj = re.compile('.*' + reg_exp_def + '.*',
                reg_exp_obj = re.compile(reg_exp_def,
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
    u"""Function checks if keyword has been found in the text."""
    ret_val = {}
    for group_name in keywords:
        group_def = keywords[group_name]
        ret_val[group_name] = []
        for keyword_name in group_def:
            reg_exp_obj_list = group_def[keyword_name]
            for reg_exp_obj in reg_exp_obj_list:
                # print "pattern: ", reg_exp_obj.pattern
                # m = reg_exp_obj.match(mytext)
                m = reg_exp_obj.search(mytext)
                if m:
                    # print "%s|%s" % (group_name, keyword_name)
                    ret_val[group_name].append(keyword_name)
                    break
    return ret_val


def _tag_on_marker(mytext, marker, stag, etag):
    u"""Function tags text based on marker."""
    ret_val = u""
    if len(marker) > 0:
        # check the first char
        if marker[0] == '|':
            ret_val = stag
        ret_val += mytext[0]
        # now check rest of the marker string
        prev_marker_char = marker[0]
        for index in range(1, len(marker)):
            if marker[index] == "|" and prev_marker_char == ".":
                ret_val += stag
            if marker[index] == "." and prev_marker_char == "|":
                ret_val += etag
            ret_val += mytext[index]
            prev_marker_char = marker[index]
        # check the last charakter
        if marker[-1] == '|':
            ret_val += etag

    return ret_val


def _create_marker(mytext, keywords):
    u"""Function detects imput text."""
    ret_val = u"".ljust(len(mytext), '.')
    # print ret_val
    for group_name in keywords:
        group_def = keywords[group_name]
        for keyword_name in group_def:
            reg_exp_obj_list = group_def[keyword_name]
            for reg_exp_obj in reg_exp_obj_list:
                # print "pattern: ", reg_exp_obj.pattern
                # m = reg_exp_obj.match(mytext)
                m = reg_exp_obj.search(mytext)
                if m:
                    # print "\n%s|%s" % (group_name, keyword_name)
                    matched_text = mytext[m.start(): m.end()]
                    # print "Matched text: %s \ns=%d e=%d" % (matched_text,
                    #                                         m.start(),
                    #                                         m.end())
                    marker = u"".ljust(len(matched_text), '|')
                    ret_val = ret_val[:m.start()] + \
                        marker + \
                        ret_val[m.end():]
                    # break
    return ret_val


def tag_keywords(mytext, keywords, stag, etag):
    u"""Function tags input text."""
    ret_val = u""
    marker = _create_marker(mytext, keywords)
    # print mytext
    # print marker
    ret_val = _tag_on_marker(mytext, marker, stag, etag)
    # print ret_val
    return ret_val


def print_keywords_csv(detected_keywords, delimiter=',', outen='utf-8'):
    u"""Function formats detected keywords in CSV."""
    first_line = True
    ret_val = u""
    for group_name in detected_keywords:
        tags_list = detected_keywords[group_name]
        for tag_name in tags_list:
            if first_line:
                first_line = False
            else:
                ret_val += u"\n"
            ret_val += group_name + delimiter + tag_name
    return ret_val.encode(outen)


def print_keywords_json(detected_keywords, prettify=False, outen='utf-8'):
    u"""Function forrmats detected keywords in JSON."""
    if prettify:
        return json.dumps(detected_keywords,
                          indent=4,
                          ensure_ascii=False).encode(outen)
    else:
        return json.dumps(detected_keywords, ensure_ascii=False).encode(outen)
