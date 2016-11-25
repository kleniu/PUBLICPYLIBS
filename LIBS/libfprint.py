#!/usr/bin/env python
# coding:utf-8
u"""Library contains routines for displaying data."""
import string


def help():
    u"""Help function."""
    print "Library contains routines for displaying data."


def ut(intext, enc="UTF-8"):
    u"""Function converts text to unicode."""
    try:
        ret_val = u"" + intext.decode(enc)
    except UnicodeError:
        # since we are using only unicode or UTF-8 it must be unicode
        ret_val = u"" + intext
    return ret_val


class colors():
    u"""Class used for color definition."""

    NORMAL = '\x1b[0m'
    RED = '\x1b[31m'
    BLUE = '\x1b[34m'
    YELLOW = '\x1b[33m'
    GREEN = '\x1b[32m'


def ct(color, txt2pr, enc="UTF-8"):
    u"""Function returns specified text in color."""
    utext2print = ut(txt2pr, enc)
    ret_val = u""
    if color == "none":
        ret_val = utext2print
    elif color == "red":
        ret_val = (colors.RED + utext2print + colors.NORMAL)
    elif color == "blue":
        ret_val = (colors.BLUE + utext2print + colors.NORMAL)
    elif color == "green":
        ret_val = (colors.GREEN + utext2print + colors.NORMAL)
    elif color == "yellow":
        ret_val = (colors.YELLOW + utext2print + colors.NORMAL)
    return ret_val.encode(enc)


def cprint(color, txt2pr, enc="UTF-8"):
    u"""Function prints specified text in color."""
    print ct(color, txt2pr, enc)


def ctagged(txt2pr, enc="UTF-8"):
    u"""Function returns colored text based on <TAGS>."""
    utext2print = ut(txt2pr, enc)
    TAGLIST = [("RED", colors.RED),
               ("YELLOW", colors.YELLOW),
               ("BLUE", colors.BLUE),
               ("GREEN", colors.GREEN)]
    ret_val = u""
    lines_list = utext2print.splitlines()
    lines_num = len(lines_list)
    for index, line in enumerate(lines_list):
        for TAG in TAGLIST:
            line = string.replace(line, '<'+TAG[0]+'>', TAG[1])
            line = string.replace(line, '</'+TAG[0]+'>', colors.NORMAL)
        ret_val += line
        # print index, lines_num
        if index + 1 < lines_num:
            ret_val += u"\n"
    return ret_val.encode(enc)


def ctaggedprint(txt2pr, enc="UTF-8"):
    u"""Function prints colored text based on <TAGS>."""
    print ctagged(txt2pr, enc)


def _calasize(data):
    u"""Supportive function to calculate array cols and raw size."""
    # calculate number of rows and collumns
    row_nums = len(data)
    col_nums = 0
    for row_index, row in enumerate(data):
        cols = len(row)
        if cols > col_nums:
            col_nums = cols
    #  print "Raws = %d, Cols = %d" % (row_nums, col_nums)
    # now calculate row and callumns sizes
    row_sizes = [0 for x in range(row_nums)]
    col_sizes = [0 for x in range(col_nums)]
    #  print "row_sizes", row_sizes, "col_sizes", col_sizes
    for row_index, row in enumerate(data):
        for col_index, text in enumerate(row):
            #  print "Cell : r=%d,c=%d v=>%s<" % (row_index, col_index, text)
            lines_list = text.splitlines()
            cur_raw_size = len(lines_list)
            cur_col_size = 0
            for line in lines_list:
                if cur_col_size < len(line):
                    cur_col_size = len(line)
            #  print "Size : rs=%d,cs=%d" % (cur_raw_size, cur_col_size)
            # now compare to previousely created array
            if row_sizes[row_index] < cur_raw_size:
                row_sizes[row_index] = cur_raw_size
            if col_sizes[col_index] < cur_col_size:
                col_sizes[col_index] = cur_col_size
    #  print "row_sizes", row_sizes, "col_sizes", col_sizes
    return (row_sizes, col_sizes)


def _make_sep(col_sizes):
    u"""Supportive function for making row separator."""
    line = u"+"
    for col_index, col_size in enumerate(col_sizes):
        line += u"".ljust(col_size, '-')
        line += u"+"
    return line + u"\n"


def carray(data, enc="UTF-8"):
    u"""Function returns formated array ready to print."""
    row_sizes, col_sizes = _calasize(data)
    #  print "row_sizes", row_sizes, "col_sizes", col_sizes
    # now we are ready to format array to be displayed
    ret_val = _make_sep(col_sizes)
    for row_index, row_size in enumerate(row_sizes):
        for cell_line in range(row_size):
            line = u""
            for col_index, col_size in enumerate(col_sizes):
                all_text = data[row_index][col_index]
                text_list = all_text.splitlines()
                try:
                    text = text_list[cell_line]
                except IndexError:
                    text = u""
                #  print "Cell : r=%d,c=%d,l=%d v=>%s<" % (row_index,
                #                                          col_index,
                #                                          cell_line,
                #                                          text)
                if len(text) < col_size:
                    text = text.ljust(col_size)
                line += u"|" + text
            ret_val += (line + u"|" + u"\n")
        ret_val += _make_sep(col_sizes)
    return ret_val.encode(enc)
