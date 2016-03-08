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
            corridor()
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


def corridor():
    print """
    You enter on a long, barely iluminated corridor with three doors.
    One on the left wall(1) and two on the right wall (2, 3).
    In the end of the corridor is another door (4).
    What will you do?
    """
    while True:
        action = raw_input("> ")

        if action == 'help':
            help()
        elif action == 'interact door' or action == 'look door':
            print "Winch door?"
        elif action == 'interact door 1':
            print "You enter the leftside door"
        elif action == 'look door 1':
            print "there is a sign saying: Restroom"
        elif action == 'interact door 2':
            print "You enter the first right door"
        elif action == 'look door 2':
            print "There is a sign on the door saying: Weapons Room"
        elif action == 'interact door 3':
            print "You enter the second right door"
        elif action == 'look door 3':
            print "There is a sign saying: office"
        elif action == 'interact door 4':
            print "You enter the monster door"
        elif action == 'look door 4':
            print "A heavy wooden door."
        elif action == 'interact door 0':
            print "You're locked in the corridor, the foyer door is locked."
        else:
            print "I don't know what you mean."



foyer()
