# -*- coding: UTF-8 -*-

officeKey = False
sawMonster = False
haveShotgun = False



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
CTRL + C or quit on any moment to exit.
YOUR PROGRESS WILL NOT BE SAVED!

Obs: Ever use uncapitalized case letters.

-----------

A game by Cesar de Barros <cbsorrilha@hotmail.com> 2016
    """

def foyer():
    global haveShotgun
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
        elif action == "summon shotgun":
            print "I don't know what it means."
            haveShotgun = True;
        elif action == 'quit':
            exit()
        else:
            print "I don't know what it means"


def corridor():
    global sawMonster
    global haveShotgun
    global officeKey

    print """
You enter on a long, barely iluminated corridor with three doors.
One on the left wall(1) and two on the right wall (2, 3).
In the end of the corridor is another door (4).
You hear a click. The door from where you came is now blocked
from the otherside.
What will you do?
    """

    while True:
        action = raw_input("> ")


        isPrepared = sawMonster == True and haveShotgun == True
        isNotPrepared = sawMonster == True and haveShotgun == False

        # print isPrepared
        # print isNotPrepared

        if action == 'help':
            help()
        elif action == 'interact door' or action == 'look door':
            print "Winch door?"
        elif action == 'look door 1':
            print "there is a sign: Restroom"
        elif action == 'interact door 1':
            print "Room"
        elif action == 'look door 2':
            print "There is a sign: Weapons Room"
        elif action == 'interact door 2':
            print "The door is locked."
        elif action == 'look door 3':
            print "There is a sign: Office"
        elif action == 'interact door 3' and officeKey == False:
            print "The door is locked."
        elif action == 'interact door 3' and officeKey == True:
            print "Office"
        elif action == 'look door 4' and sawMonster == False:
            print "A heavy wooden door. No signs."
        elif action == 'look door 4' and sawMonster == True:
            print "The door where'd you saw the monster."
        elif action == 'interact door 4' and sawMonster == False:
            print "Monster"
            sawMonster = True
        elif action == 'interact door 4' and isNotPrepared:
            print "Is better to only go back there with a gun."
        elif action == 'interact door 4' and isPrepared:
            print "Monster"
        elif action == 'interact door 0' or action == 'look door 0':
            print "You're locked in the corridor, the foyer door is blocked by something on the other side."
        # elif action == 'summon shotgun':
        #     print "A shotgun appears in your hands like magic"
        #     haveShotgun = True
        # elif action == 'summon office key':
        #         print "The office key appears in your hands like magic"
        #         officeKey = True
        else:
            print "I don't know what it means."

def Diary():
    return """
Dear diary,

I don't know why my father keeps that gun on the closet and choose to
call it Weapons Room. By the way the key is ever with him.

Even now, that he is dead.

My father is a really cautious man.
"""

def room():
    print"""
You've entered a cozy room. There are beige walls, wooden floor
and soft lights.
There are too: a messy bed, a wooden chair and a book on top
of a dressing table.
What will you do?
    """
    while True:
        action = raw_input("> ")

        rest = action == "look bed" or action == "interact bed"
        rest = rest or action == "interact chair"

        if action == "help":
            help()
        elif rest:
            print "There's no need to rest now";
        elif action == "look chair":
            print "A wooden chair. Looks Rusty."
        elif action == "look book":
            print "A book with a black cover, probably made of leather."
        elif action == "interact book":
            print Diary()
        elif action == ""
        else:
            print "I don't know what it means"


room()
