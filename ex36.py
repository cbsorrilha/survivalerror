# -*- coding: UTF-8 -*-
def help():
    print """
    ===SURVIVALERROR 1.0========================================
    That's a little game Written in Python.
    It don't pretend to be awesome. Don't create expectations.
    To look better at 'x', type: \"examine 'x'\"
    To pick 'x', type: \"pick 'x'\"
    To interact with 'x', type: \"interact 'x'\"
    If you have a weapon and want to shot 'x', type: \"shot 'x'\"
    To simply look around, type: \"look\"
    this will give you a description of the place you're in.
    CTRL + C or quit on any momento to exit.
    YOUR PROGRESS DO NOT WILL BE SAVED!

    Obs: Ever use uncapitalized case letters.

    -----------

    A game by Cesar de Barros <cbsorrilha@hotmail.com> 2016
    """

def foyer():
    print """
    You enter a dark foyer with your clothes wet because of the rain.
    You can hear the thunders outside.
    The door behind you got locked after you enter.
    There's another door on the foyer, a rugged mat with the word 'Welcome'
    and a little corner table with a plant on top of it.
    """
    haveKey = False
    keyRevealed = False

    while True:
        action = raw_input("> ")

        plantBool = action == 'interact plant' or  action == 'look plant'
        cornerTableBool = action == 'interact corner table' or action == 'look corner table'

        if action == 'help':
            help()
        elif action == 'interact door' and haveKey == False:
            print "The door is locked."
        elif action == 'interact door' and haveKey == True:
            print "Enter corridor"
        elif action == 'look mat' or action == 'look rugged mat':
            print "It is a rugged mat with the word 'Welcome' written on it"
        elif action == 'interact mat' or action == 'interact rugged mat':
            print "You remove the mat and this reveals a key"
            keyRevealed = True
        elif action == 'pick key' and keyRevealed == True:
            print "You pick the key"
            haveKey = True
        elif action == "look key" and keyRevealed == True:
            print "Thats a key, wonder what door it will open."
        elif plantBool or cornerTableBool:
            print "It is just an ordinary corner table with a plant on top of it."
        elif action == 'quit':
            exit()
        else:
            print "I don't know what it means"

foyer()
