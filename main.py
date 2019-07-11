#!/usr/bin/env python
# coding=utf-8

# ------------------------------------------------------------------------------
# Scales harmonization | Music Theory
# ------------------------------------------------------------------------------
# jose maria sosa

import json

import numpy as np
from root import RootNote

from pprint import pprint


class Harmonization(object):

    """ Harmonization of a music scale.
    """
    
    def __init__(self, scale=False):
        
        # 1. Extract the scale parameters.
        self.setScaleParameters(scale)

        # 2. Define the list of 12 notes.
        self.notes = self.getNotes()

        # 3. Import the steps.
        self.steps = self.importSteps()

        # 4. Default output notation.
        self.default_notation = self.setDefaultNotation()
        
    # --------------------------------------------------------------------------
    
    def setScaleParameters(self, scale):

        if isinstance(scale, dict):
            if 'positions' in scale.keys():
                self.positions = scale['positions']

            if 'root' in scale.keys():
                self.root = scale['root']

            if 'scale_name' in scale.keys():
                self.scale_name = scale['scale_name']

    # --------------------------------------------------------------------------

    def getNotes(self):

        file_name = "files/notes.json"
        with open(file_name, 'r') as f:
            notes = json.load(f)['notes']

        return notes

    # --------------------------------------------------------------------------

    def importSteps(self):

        file_name = "files/steps.json"
        with open(file_name, 'r') as f:
            steps = json.load(f)['steps']

        return steps

    # --------------------------------------------------------------------------

    def setDefaultNotation(self):

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
    
    def importModes(self):

        file_name = "files/patterns.json"
        with open(file_name, 'r') as f:
            modes = json.load(f)['patterns']['modes']

        return modes

    # --------------------------------------------------------------------------

    def stepDistance(self, from_note, to_note):

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

    # --------------------------------------------------------------------------
    
    def stepOperations(self, given_note, tones):

        semitone = int(tones * 2)
        results = given_note + semitone

        if results > 11:
            while results > 11:
                results -= 12
        elif results < 0:
            while results < 0:
                results += 12

        return results

    # --------------------------------------------------------------------------

    def replacePositionNotes(self, scale_or_note):

        if isinstance(scale_or_note, list):
            return [self.notes[x][self.default_notation] for x in scale_or_note]

        else:
            return self.notes[scale_or_note][self.default_notation]

    # --------------------------------------------------------------------------
    
    def getMode(self, note, scale):

        # 1. Import all the modes patterns.
        modes = self.importModes()

        # 2. Get the position of the current note and sort the scale.
        scale = scale[:-1]
        note_index = scale.index(note)
        sorted_notes = scale[note_index:] + scale[:note_index]
        sorted_notes = sorted_notes + [sorted_notes[0]]

        # 3. Calculate the step pattern, and compare with the default patterns.
        steps = []
        for index, value in enumerate(sorted_notes):
            if index > 0:
                f = sorted_notes[index-1]
                t = sorted_notes[index]
                steps.append(self.stepDistance(f, t))

        for mode in modes.keys():
            if all([x==0 for x in np.subtract(steps, modes[mode])]):
                return mode

        return None

    # --------------------------------------------------------------------------
    
    def getTriad(self, note, long_scale):

        note_index = long_scale.index(note)

        return [
            long_scale[note_index],
            long_scale[note_index+2],
            long_scale[note_index+4]
        ]

    # --------------------------------------------------------------------------
    
    def getQuads(self, note, long_scale):

        note_index = long_scale.index(note)

        return [
            long_scale[note_index],
            long_scale[note_index+2],
            long_scale[note_index+4],
            long_scale[note_index+6]
        ]

    # --------------------------------------------------------------------------
    
    def getQuadsDom7(self, note, long_scale):

        # THIS MAY NOT BE CORRECT, CHECK IT FIRST

        note_index = long_scale.index(note)

        return [
            long_scale[note_index],
            long_scale[note_index+2],
            long_scale[note_index+4],
            self.stepOperations(long_scale[note_index+6], tones=-0.5)
        ]

    # --------------------------------------------------------------------------
    
    def getStepsList(self, note_list):

        steps = []

        for ix in range(len(note_list)-1):
            steps.append(self.stepDistance(note_list[ix], note_list[ix+1]))

        return steps        

    # --------------------------------------------------------------------------
    
    def nameTriad(self, steps):

        major3 = self.steps['major3']
        minor3 = self.steps['minor3']

        if steps[0] == major3:
            if steps[1] == major3:
                return 'aug'

            elif steps[1] == minor3:
                return ''

        elif steps[0] == minor3:
            if steps[1] == major3:
                return 'min'

            elif steps[1] == minor3:
                return 'dim'

        return 'unnamed'

    # --------------------------------------------------------------------------
    
    def nameQuads(self, steps):

        major3 = self.steps['major3']
        minor3 = self.steps['minor3']

        if steps[0] == major3:
            if steps[1] == major3:
                if steps[2] == major3:
                    return 'unnamed'
                
                elif steps[2] == minor3:
                    return 'unnamed'

            elif steps[1] == minor3:
                if steps[2] == major3:
                    return 'maj7'
                
                elif steps[2] == minor3:
                    return '7'

        elif steps[0] == minor3:
            if steps[1] == major3:
                if steps[2] == major3:
                    return 'unnamed'
                
                elif steps[2] == minor3:
                    return 'm7'

            elif steps[1] == minor3:
                if steps[2] == major3:
                    return 'ø'
                
                elif steps[2] == minor3:
                    return 'unnamed'

        return 'unnamed'

    # --------------------------------------------------------------------------
    
    def toRoman(self, n):

        return {
            1: 'i',
            2: 'ii',
            3: 'iii',
            4: 'iv',
            5: 'v',
            6: 'vi',
            7: 'vii'
        }[n]

    # --------------------------------------------------------------------------
    
    def diatonicHarmonization(self):

        scale = self.positions
        long_scale = scale[:-1] + scale

        harmonized_scale = []
        for ix, note in enumerate(scale[:-1]):

            mode = self.getMode(note, scale)

            triad = self.getTriad(note, long_scale)
            quads = self.getQuads(note, long_scale)
            quads_dom7 = self.getQuadsDom7(note, long_scale)

            triad_steps = self.getStepsList(triad)
            triad_tail = self.nameTriad(triad_steps)

            quads_steps = self.getStepsList(quads)
            quads_tail = self.nameQuads(quads_steps)

            formatted_note = self.replacePositionNotes(note).title()

            harmonized_scale.append({
                "mode": mode,
                "grade": self.toRoman(ix+1),
                "triad": {
                    "notes": self.replacePositionNotes(triad),
                    "name": formatted_note + triad_tail
                },
                "quads": [
                    {
                        "notes": self.replacePositionNotes(quads),
                        "name": formatted_note + quads_tail
                    }
                ]
            })

        return {
            "harmonization": harmonized_scale
        }

    # --------------------------------------------------------------------------

    def simple(self):

        if (len(self.positions) - 1) == 9:
            pass

        elif (len(self.positions) - 1) == 7:
            harmony = self.diatonicHarmonization()

            pprint (harmony)
        
        else:
            print('not available yet')



    # --------------------------------------------------------------------------
# ------------------------------------------------------------------------------


def main():

    D_minor = RootNote("G").major

    Harmonization(D_minor).simple()

# ------------------------------------------------------------------------------


if __name__ == '__main__':
    main()


