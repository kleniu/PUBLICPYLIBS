#!/usr/bin/env python
# coding:utf-8
u"""The utility to detect language in text provided in stdin

DO NOT forget to export PYTHONPATH with directory
containing libkeywords.py before you run this script
"""
import sys
import os
from langdetect import detect


def detect_language_long(message):
    u"""Function detects language and returns long language name"""
    ln = detect(message)
    if ln == "af":
        ln_long = "afrikaans"
    elif ln == "ar":
        ln_long = "arabic"
    elif ln == "bg":
        ln_long = "bulgarian"
    elif ln == "bn":
        ln_long = "bengali"
    elif ln == "ca":
        ln_long = "catalan"
    elif ln == "cs":
        ln_long = "czech"
    elif ln == "cy":
        ln_long = "welsh"
    elif ln == "da":
        ln_long = "danish"
    elif ln == "de":
        ln_long = "german"
    elif ln == "el":
        ln_long = "greek"
    elif ln == "en":
        ln_long = "english"
    elif ln == "es":
        ln_long = "spanish"
    elif ln == "et":
        ln_long = "estonian"
    elif ln == "fa":
        ln_long = "persian"
    elif ln == "fi":
        ln_long = "finnish"
    elif ln == "fr":
        ln_long = "french"
    elif ln == "gu":
        ln_long = "gujarati"
    elif ln == "he":
        ln_long = "hebrew"
    elif ln == "hi":
        ln_long = "hindi"
    elif ln == "hr":
        ln_long = "croatian"
    elif ln == "hu":
        ln_long = "hungarian"
    elif ln == "id":
        ln_long = "indonesian"
    elif ln == "it":
        ln_long = "italian"
    elif ln == "ja":
        ln_long = "japan"
    elif ln == "kn":
        ln_long = "kannada"
    elif ln == "ko":
        ln_long = "korean"
    elif ln == "lt":
        ln_long = "lithuanian"
    elif ln == "lv":
        ln_long = "latvian"
    elif ln == "mk":
        ln_long = "macedonian"
    elif ln == "ml":
        ln_long = "malayalam"
    elif ln == "mr":
        ln_long = "marathi"
    elif ln == "ne":
        ln_long = "nepali"
    elif ln == "nl":
        ln_long = "dutch"
    elif ln == "no":
        ln_long = "norwegian"
    elif ln == "pa":
        ln_long = "punjabi"
    elif ln == "pl":
        ln_long = "polish"
    elif ln == "pt":
        ln_long = "portuguese"
    elif ln == "ro":
        ln_long = "romanian"
    elif ln == "ru":
        ln_long = "russian"
    elif ln == "sk":
        ln_long = "slovak"
    elif ln == "sl":
        ln_long = "slovene"
    elif ln == "so":
        ln_long = "somali"
    elif ln == "sq":
        ln_long = "albanian"
    elif ln == "sv":
        ln_long = "swedish"
    elif ln == "sw":
        ln_long = "swahili"
    elif ln == "ta":
        ln_long = "tamil"
    elif ln == "te":
        ln_long = "telugu"
    elif ln == "th":
        ln_long = "thai"
    elif ln == "tl":
        ln_long = "tagalog"
    elif ln == "tr":
        ln_long = "turkish"
    elif ln == "uk":
        ln_long = "ukrainian"
    elif ln == "ur":
        ln_long = "urdu"
    elif ln == "vi":
        ln_long = "vietnamese"
    elif ln == "zh-cn":
        ln_long = "chinese simplified"
    elif ln == "zh-tw":
        ln_long = "chinese traditional"
    else:
        ln_long = "unknown"
    return ln_long


if __name__ == "__main__":
    message = u""
    if '-' in sys.argv:
        for line in sys.stdin:
            message += line.decode("UTF-8")
        print detect_language_long(message)
    else:
        print "Usage: " + os.path.basename(__file__) + " - "
        print "Example: cat your_file | " + os.path.basename(__file__) + " - "
