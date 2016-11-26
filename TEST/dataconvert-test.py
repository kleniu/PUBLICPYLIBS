#!/usr/bin/env python
# coding:utf-8
u"""The Utility for testing library libformatconv.py.

DO NOT forget to export PYTHONPATH with directory
containing libkeywords.py before you run this script
"""
import libformatconv as t
# helper
import json
import hashlib
import os


def hash_dict(data):
    u"""Helper function for calculating the hash of the dictionary."""
    return hashlib.sha1(json.dumps(data, sort_keys=True)).hexdigest()


def hash_file(filename):
    u"""Helper function for calculating hash of file."""
    with open(filename, 'r') as my_file:
        filecont = my_file.read()
    return hashlib.sha1(filecont).hexdigest()


def testme():
    u"""Test function."""
    t.help()

    print "\n######### Load JSON ##############"
    jf = "../DATA/keywords.json"
    jdata = t.json_load(jf)
    print "Data loaded from json file: " + jf
    # t.json_print(jdata)
    # t.yaml_print(jdata)
    t.json_save(jdata, jf + "-DeleteMe")
    print "Data saved to json file: " + jf + "-DeleteMe"
    hf1 = hash_file(jf)
    hf2 = hash_file(jf + "-DeleteMe")
    if (hf1 == hf2):
        print ":) - json file hashes are the same"
    else:
        print ":( - json file hashes are different"
    os.remove(jf + "-DeleteMe")

    print "\n######### Load YAML ##############"
    yf = "../DATA/keywords.yaml"
    ydata = t.yaml_load(yf)
    print "Data loaded from yaml file: " + yf
    # t.yaml_print(ydata)
    t.yaml_save(ydata, yf + "-DeleteMe")
    print "Data saved to yaml file: " + yf + "-DeleteMe"
    hf1 = hash_file(yf)
    hf2 = hash_file(yf + "-DeleteMe")
    if (hf1 == hf2):
        print ":) - yaml file hashes are the same"
    else:
        print ":( - yaml file hashes are different"
    os.remove(yf + "-DeleteMe")
    

    print "\n######### Compare data ###########"
    h1 = hash_dict(jdata)
    h2 = hash_dict(ydata)
    print "hash(data loaded from JSON) = " + h1
    print "hash(data loaded from YAML) = " + h2
    if (h1 == h2):
        print ":) - hashes are the same"
    else:
        print ":( - hashes are different"

    print "\n######### Detect format ###########"
    print "detected format for json file     : >" + t.detect_format("../DATA/keywords.json") + "<" 
    print "detected format for bad json file : >" + t.detect_format("../DATA/bad_keywords.json") + "<"
    print "detected format for yaml file     : >" + t.detect_format("../DATA/keywords.yaml") + "<" 
    print "detected format for bad yaml file : >" + t.detect_format("../DATA/bad_keywords.yaml") + "<"


if __name__ == "__main__":
    testme()
