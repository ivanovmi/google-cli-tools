#!/usr/bin/env python
# -- coding: utf-8 --

__author__ = 'michael'
import gmail
import getpass


def read():
    exit = ''
    while exit != 'q':
        num = int(raw_input('Num of mail: '))-1
        print unreads[num].body
        unreads[num].read()
        exit = raw_input('Type q for exit...')
    return

def init():
    login = raw_input('Gmail user: ')
    password = getpass.getpass()
    g = gmail.Gmail()
    g.login(login, password)
    return g

def main():
    account = init()
    unreads = account.inbox().mail(unread=True)
    count = 0
    wanna = ''
    unreads = list(reversed(unreads))
    while count < len(unreads):
        print 'NUM\t|\tTHEME\t\t\t\t\t\t\t\t\t|\tFROM'
        for i in xrange(count, count+10):
            unreads[i].fetch()
            if len(unreads[i].subject) < 70:
                space = 70 - len(unreads[i].subject)
            print i+1, '\t|\t', unreads[i].subject, ' '*space, '|\t', unreads[i].fr

        while wanna.lower() not in ['y', 'yes', 'n', 'no', 'r']:
            wanna = raw_input('You wanna see next 10 messages?[y/n] ')
        if wanna.lower() in ['y', 'yes']:
            count += 10
            wanna = ''
        elif wanna.lower() == 'r':
            read()
            wanna = ''
        else:
            break

    account.logout()

main()