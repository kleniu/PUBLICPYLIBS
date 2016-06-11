#!/usr/bin/env python
# coding:utf-8
u"""The first lib."""


def depunctate(text_data):
    u"""Function gets rid of punctation chars."""
    ufrom_ = u'!"$%(),-/:;<=>?[]^_`{-}~\'\\\n'
    uto___ = u'                            '
    translate_map = dict(
                        zip(map(ord, ufrom_),
                            map(ord, uto___))
                        )
    result = unicode(text_data).translate(translate_map)
    result = ' '.join(result.split())
    return result



if __name__ == "__main__":
    def testme():
        u"""Just for tests."""
        print "### This is a test of " + __file__
        testtxt = u"""
            this is just a simple test to depunktation function. (Use) it with
            anything you want! Test! , Test2, Test3!
        """
        print "# depunctate >>", depunctate(testtxt).encode('UTF-8'), "<<"
    testme()
