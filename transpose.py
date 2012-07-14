#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This application is meant to transpose chords from a tone to another
# TODO : accept a list of chords, coma separated

import sys

# Here the global tuple of chords.
globalchords=("A","A#","B","C","C#","D","D#","E","F","F#","G","G#")

chords=str("")
newchords=str("")
trans=str("")

chords = input('What chords do you want to transpose (space separated)?\n')
chords = chords.split(' ')

trans = input('What transposition do you want to apply? (in semi-tone, examples: +4 or -2)\n')
while trans.lstrip('+-').isnumeric() is False:
	print('This is not a valid transposition value. Examples: 5 or -9 or +3.')
	trans = input('What transposition do you want to apply? (in semi-tone, examples: +4 or -2)\n')
	
trans = int(trans)


for c in chords:
	hasMajor=False
	hasMinor=False
	while c.upper().rstrip('M') not in globalchords:
		if c.isnumeric():
			print(c, "is a number, please enter a chord")
			c = input('What chord do you want to transpose instead?\n')
		else:
			print(c," is definitely not a chord")
			c = input('What chord do you want to transpose instead?\n')

	#Detecting any suffix (minor,major...)
	if c.endswith('M'):
		hasMajor=True
	elif c.endswith('m'):
		hasMinor=True

	# Making the transposition
	ind=globalchords.index(c.upper().rstrip('M'))
	newind=ind+trans

	# Prevent the IndexOutOfRange.
	if newind >= 12:
		while newind >= 12:
			newind-=12

	# Calculating the new value of the chord
	newc=globalchords.__getitem__(newind)
	
	#Addind the suffix
	if hasMajor == True:
		newc=newc+'M'
	elif hasMinor == True:
		newc=newc+'m'

	newchords=newchords+newc+" "
	
print("The new chords are:")
print(newchords)
