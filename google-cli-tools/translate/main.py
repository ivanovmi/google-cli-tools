#!/usr/bin/env python
# -- coding: utf-8 --

__author__ = 'michael'

import goslate
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__))[:-10:])
global tools
import tools


def help_language(start=None):
    """
    Print in cli all available languages and it's codes
    :param start: can show only languages started with
           this start sequence. By default equal to None
    :return: Nothing. Just print result in cli.
    """
    for key, values in tools.swap_key_values(
            goslate.Goslate().get_languages()).iteritems():
        if start is not None:
            if key.startswith(start):
                print key, values
        else:
            print key, values


def quick_translate(text, end_lang, start_lang=None):
    """
    This function trying determine text language,
     and translate from it to end language
    :param text: some string
    :param end_lang: string, code of language
           (you can determine it in help_language function)
    :return: print translated text to cli
    """
    if start_lang is not None:
        print goslate.Goslate().translate(str(text),
                                          str(end_lang), str(start_lang))
    else:
        print goslate.Goslate().translate(str(text), str(end_lang))


def translate():
    """
    This function allow translate multiline stdin to required language
    :return:
    """
    start_lang = ''
    end_lang = ''
    text = ''
    stop_word = 'EOF'

    while start_lang not in goslate.Goslate().get_languages().keys():
        start_lang = raw_input('Enter original text language: ')
    while end_lang not in goslate.Goslate().get_languages().keys():
        end_lang = raw_input('Enter language for translate: ')

    print 'Start input text. When end, just type EOF.'
    while True:
        line = raw_input()
        if line.strip() == stop_word:
            break
        text += "%s\n" % line
    quick_translate(text, end_lang, start_lang)
