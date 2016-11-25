#!/usr/bin/env python
# coding:utf-8
u"""Library for data conversions.
    requires pip install PyYaml
 """
import json
import yaml
from yaml import Loader, SafeLoader
import codecs


# configure yaml
def _c_yaml_str(self, node):
    return self.construct_scalar(node)

Loader.add_constructor(u'tag:yaml.org,2002:str', _c_yaml_str)
SafeLoader.add_constructor(u'tag:yaml.org,2002:str', _c_yaml_str)


def help():
    u"""Help function."""
    print "Library contains routines for converting data"
    print "from json to yaml and vice versa."


def json_load(json_filename):
    u"""Finction loads json file."""
    retval = None
    with codecs.open(json_filename, 'r', encoding='UTF-8') as my_file:
        retval = json.load(my_file)
    return retval


def json_dump(data):
    u"""Function dumps data into string"""
    retval = json.dumps(data, sort_keys=True,
                        indent=4, separators=(',', ': '),
                        ensure_ascii=False, encoding="UTF-8")
    return retval


def json_print(data):
    u"""Function print data in JSON format."""
    print(json_dump(data))


def json_save(data, json_filename):
    u"""Function saves data into file."""
    with codecs.open(json_filename, "w", "UTF-8") as my_file:
        my_file.write(json_dump(data))


def yaml_load(yaml_filename):
    u"""Finction loads yaml file."""
    retval = None
    with codecs.open(yaml_filename, 'r', encoding='UTF-8') as my_file:
        retval = yaml.load(my_file)
    return retval


def yaml_dump(data):
    u"""Function dumps data in yaml format into the string."""
    _ydump = yaml.safe_dump(data, default_flow_style=False, allow_unicode=True,
                       default_style='"', indent=4)
    retval = _ydump.decode("UTF-8")
    return retval


def yaml_print(data):
    u"""Function print data in YAML format."""
    print(yaml_dump(data))


def yaml_save(data, yaml_filename):
    u"""Function saves data in yaml format"""
    with codecs.open(yaml_filename, "w", "UTF-8") as my_file:
        my_file.write(yaml_dump(data))
