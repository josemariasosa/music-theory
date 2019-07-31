#!/usr/bin/env python
# coding=utf-8

# ------------------------------------------------------------------------------
# Scales harmonization | Music Theory
# ------------------------------------------------------------------------------
# jose maria sosa


import json

class RootNote(object):

    def __init__(self):

        # 1. Define the list of 12 notes.
        self.notes = self.getNotes()
        self.num_notes = list(range(12))

        # 2. Define the root position.
        # self.root = root.lower()
        # self.root_position = self.getRootPosition(self.root)

        # 3. Import the patterns.
        self.pats = self.importPatterns()

        # 4. Default output notation.
        self.default_notation = self.setDefaultNotation()

    # --------------------------------------------------------------------------
    
    def __str__(self):

        message = "The root note is {}!".format(self.root.title())

        return message

    # --------------------------------------------------------------------------
    
    def getNotes(self):

        file_name = "files/notes.json"
        with open(file_name, 'r') as f:
            notes = json.load(f)['notes']

        return notes

    # --------------------------------------------------------------------------
    
    def getRootPosition(self, root):

        position = [x["position"] for x in self.notes if root in x['match']]

        if len(position) == 1:
            return position[0]

        else:
            print("Given note was not found, try again!")
            exit()

    # --------------------------------------------------------------------------

    def importPatterns(self):

        file_name = "files/patterns.json"
        with open(file_name, 'r') as f:
            patterns = json.load(f)['patterns']

        return patterns

    # --------------------------------------------------------------------------
    
    def setDefaultNotation(self):

        return 'sharp'

        if len(self.root) == 1:
            default_notation = 'sharp'

        elif self.root[-1] == 'b':
            default_notation = 'flat'

        elif '#' in self.root:
            default_notation = 'sharp'

        else:
            default_notation = 'sharp'

        return default_notation

    # --------------------------------------------------------------------------
    
    def positionPattern(self, scale_name):

        # Define the steps pattern.
        step_pattern = self.pats['scales'][scale_name]

        # 2. Resort the 12 notes into a basic pattern.
        basic = (self.num_notes[self.root_position:] 
                 + self.num_notes[:self.root_position])
        basic = basic + [basic[0]]

        # 3. Get the cumulative steps.
        step_pattern = [int(x * 2) for x in step_pattern]
        accum_steps = list(np.cumsum(step_pattern))

        # 4. Calculate the scale values.
        scale = []
        for index, value in enumerate(basic):
            if index == 0:
                scale.append(value)
            elif index in accum_steps:
                scale.append(value)

        return scale

    # --------------------------------------------------------------------------
    
    def replacePositionNotes(self, scale):
        return [self.notes[x][self.default_notation] for x in scale]

    # --------------------------------------------------------------------------
# ------------------------------------------------------------------------------

def stepDistance(from_note, to_note):

    if to_note > from_note:
        semitone = to_note - from_note

    elif to_note < from_note:
        semitone = (to_note + 12) - from_note

    else:
        semitone = 0

    if semitone % 2 == 0:
        return int(semitone / 2)
    
    else:
        return semitone / 2

def stepOperations(given_note, tones):

    semitone = int(tones * 2)
    results = given_note + semitone

    if results > 11:
        while results > 11:
            results -= 12
    elif results < 0:
        while results < 0:
            results += 12

    return results

def buildString(numeric_open_note, frets=20):
    frets = frets + 1 # Adding the open note.
    string = []
    for fret in range(frets):
        string.append(stepOperations(numeric_open_note, fret/2))
        # string.extend(RootNote().replacePositionNotes([stepOperations(numeric_open_note, fret/2)]))

    return string

e_string = buildString(4)
a_string = buildString(9)
d_string = buildString(2)
g_string = buildString(7)

strings = [
    e_string,
    a_string,
    d_string,
    g_string
]

def findFretPosition(string, note):

    return [x[0] for x in enumerate(string) if x[1] == 0]

for string in strings:

    fret_positions = findFretPosition(string, 0)

    print(string)
    print(fret_positions)
    print('--------------------')

def majorChordTab(note):

    text = "G |-----0------|\nD |-----2------|\nA |-----3------|\nE |------------|"

    return text

# eS = 

# text = """
# G |-----0------|
# D |-----2------|
# A |-----3------|
# E |------------|
# """

G |------------|
D |--------5---|
A |-----7------|
E |--8---------|

[12, 10, 8, 7, ]

# print (text)

# import json
# import math

# import numpy as np
# from root import RootNote

# from pprint import pprint


# class TabGenerator(object):

#     """ Generate Tabs.
#     """
    
#     def __init__(self):
        



#     # --------------------------------------------------------------------------
# # ------------------------------------------------------------------------------


# def main():

#     D_minor = RootNote("c#").major

#     TabGenerator(D_minor).simple()

# # ------------------------------------------------------------------------------


# if __name__ == '__main__':
#     main()


