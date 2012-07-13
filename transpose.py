#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This application is meant to transpose chords from a tone to another
# TODO : accept a list of chords, coma separated

import sys

# Here the global tuple of chords.
globalchords=("A","A#","B","C","C#","D","D#","E","F","F#","G","G#")

chord=str("")
chord = input('What chord do you want to transpose?\n')

while chord not in globalchords:
	if chord == "":
		print("Please enter a chord")
		chord = input('What chord do you want to transpose?\n')
	elif chord.isnumeric():
		print("This is a number, please enter a chord")
		chord = input('What chord do you want to transpose?\n')
	else:
		print("This is definitely not a chord")
		chord = input('What chord do you want to transpose?\n')

# Making the transposition
trans = input('What transposition do you want to apply? (in semi-ton, examples: +4 or -2)\n')
trans = int(trans)
ind=globalchords.index(chord)
newind=ind+trans

# Prevent the IndexOutOfRange.
if newind >= 12:
	while newind >= 12:
		newind-=12

# Calculating the new value of the chord
newchord=globalchords.__getitem__(newind)
print("The new chord is ",newchord)
	
