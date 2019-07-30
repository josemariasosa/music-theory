#!/usr/bin/env python
# coding=utf-8

# ------------------------------------------------------------------------------
# Scales harmonization | Music Theory
# ------------------------------------------------------------------------------
# jose maria sosa

import json
import math

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
        self.notes = self.importNotes()

        # 3. Import the steps.
        self.importSteps()

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

    def importNotes(self):

        file_name = "files/notes.json"
        with open(file_name, 'r') as f:
            notes = json.load(f)['notes']

        return notes

    # --------------------------------------------------------------------------

    def importSteps(self):

        file_name = "files/steps.json"
        with open(file_name, 'r') as f:
            steps = json.load(f)['steps']

        self.major3 = steps['major3']
        self.minor3 = steps['minor3']
        self.major7 = steps['major7']
        self.minor7 = steps['minor7']
        self.dim7 = steps['dim7']

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

    def formattingSteps(self, distance):

        """ If distance == 1.5, then return 1.5, else, if distance == 2.0, then
            return 2.
        """

        if math.modf(distance)[0] > 0:
            return distance

        else:
            return int(distance)

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
    
    def getStepsList(self, note_list):

        steps = []

        for ix in range(len(note_list)-1):
            steps.append(self.stepDistance(note_list[ix], note_list[ix+1]))

        return steps        

    # --------------------------------------------------------------------------
    
    def nameTriad(self, steps):

        if steps[0] == self.major3:
            if steps[1] == self.major3:
                return 'aug'

            elif steps[1] == self.minor3:
                return ''

        elif steps[0] == self.minor3:
            if steps[1] == self.major3:
                return 'min'

            elif steps[1] == self.minor3:
                return 'dim'

        return 'unnamed'

    # --------------------------------------------------------------------------
    
    def nameQuads(self, steps):

        if steps[0] == self.major3:
            if steps[1] == self.major3:
                if steps[2] == self.major3:
                    return 'augΔ7'
                
                elif steps[2] == self.minor3:
                    return 'unnamed'

            elif steps[1] == self.minor3:
                if steps[2] == self.major3:
                    return 'Maj7'           # Major 7th [M7 - Maj7]
                
                elif steps[2] == self.minor3:
                    return '7'              # Dominant 7th [7 - Δ7]

        elif steps[0] == self.minor3:
            if steps[1] == self.major3:
                if steps[2] == self.major3:
                    return 'mΔ7'
                
                elif steps[2] == self.minor3:
                    return 'm7'             # Minor 7th [m7 - min7]

            elif steps[1] == self.minor3:
                if steps[2] == self.major3:
                    return 'ø7'             # Half-diminished 7th [ø7 - min7b5]
                
                elif steps[2] == self.minor3:
                    return 'o7'             # Fully-diminished 7th [o7 - dim7]

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
    
    def getNotes(self, root, tones):

        results = [root]
        accum = 0
        for tone in tones:
            accum = self.formattingSteps(accum + tone)
            results.append(self.stepOperations(root, tones=accum))

        return [self.replacePositionNotes(x) for x in results]

    # --------------------------------------------------------------------------
    
    def generateAlternatives(self, note, quads_steps):

        Note = self.replacePositionNotes(note).title()
        results = []

        # (3.5) is the sum of a major3 + minor3
        seventh = self.major3 + self.minor3 + quads_steps[2]
        seventh = self.formattingSteps(seventh)

        if seventh == self.major7:
            # minor7
            alternative_1 = quads_steps.copy()
            alternative_1[2] = self.formattingSteps(quads_steps[2] - 0.5)

            if ((alternative_1[2] >= self.minor3)
                and (alternative_1[2] <= self.major3)):
                results.append({
                    "chord": Note + self.nameQuads(alternative_1),
                    "tones": alternative_1,
                    "notes": self.getNotes(note, alternative_1)
                })
            
            # dim7
            alternative_2 = quads_steps.copy()
            alternative_2[2] = self.formattingSteps(quads_steps[2] - 1)

            if ((alternative_2[2] >= self.minor3)
                and (alternative_2[2] <= self.major3)):
                results.append({
                    "chord": Note + self.nameQuads(alternative_2),
                    "tones": alternative_2,
                    "notes": self.getNotes(note, alternative_2)
                })

        elif seventh == self.minor7:
            # major7
            alternative_1 = quads_steps.copy()
            alternative_1[2] = self.formattingSteps(quads_steps[2] + 0.5)

            if ((alternative_1[2] >= self.minor3)
                and (alternative_1[2] <= self.major3)):
                results.append({
                    "chord": Note + self.nameQuads(alternative_1),
                    "tones": alternative_1,
                    "notes": self.getNotes(note, alternative_1)
                })

            # dim7
            alternative_2 = quads_steps.copy()
            alternative_2[2] = self.formattingSteps(quads_steps[2] - 1)

            if ((alternative_2[2] >= self.minor3)
                and (alternative_2[2] <= self.major3)):
                results.append({
                    "chord": Note + self.nameQuads(alternative_2),
                    "tones": alternative_2,
                    "notes": self.getNotes(note, alternative_2)
                })

        elif seventh == self.dim7:
            # major7
            alternative_1 = quads_steps.copy()
            alternative_1[2] = self.formattingSteps(quads_steps[2] + 1)

            if ((alternative_1[2] >= self.minor3)
                and (alternative_1[2] <= self.major3)):
                results.append({
                    "chord": Note + self.nameQuads(alternative_1),
                    "tones": alternative_1,
                    "notes": self.getNotes(note, alternative_1)
                })

            # minor7
            alternative_2 = quads_steps.copy()
            alternative_2[2] = self.formattingSteps(quads_steps[2] + 0.5)

            if ((alternative_2[2] >= self.minor3)
                and (alternative_2[2] <= self.major3)):
                results.append({
                    "chord": Note + self.nameQuads(alternative_2),
                    "tones": alternative_2,
                    "notes": self.getNotes(note, alternative_2)
                })

        return results

    # --------------------------------------------------------------------------
    
    def getChordVariation(self, note, quads_steps):

        # Major
        if (quads_steps[0], quads_steps[1]) == (self.major3, self.minor3):
            results = self.generateAlternatives(note, quads_steps)

        # Minor
        elif (quads_steps[0], quads_steps[1]) == (self.minor3, self.major3):
            results = self.generateAlternatives(note, quads_steps)

        # Diminished
        elif (quads_steps[0], quads_steps[1]) == (self.minor3, self.minor3):
            results = self.generateAlternatives(note, quads_steps)

        # Augmented
        elif (quads_steps[0], quads_steps[1]) == (self.major3, self.major3):
            results = self.generateAlternatives(note, quads_steps)

        else:
            results = []

        return results


    # --------------------------------------------------------------------------
    
    def formattingAlts(self, l):

        results = []
        if len(l) > 0:
            for alternative in l["alternatives"]:
                results.append({
                    "notes": "",
                    "name": alternative['tail']
                })

    # --------------------------------------------------------------------------
    
    def diatonicHarmonization(self):

        scale = self.positions
        long_scale = scale[:-1] + scale

        harmonized_scale = []
        for ix, note in enumerate(scale[:-1]):

            mode = self.getMode(note, scale)

            triad = self.getTriad(note, long_scale)
            quads = self.getQuads(note, long_scale)

            triad_steps = self.getStepsList(triad)
            triad_tail = self.nameTriad(triad_steps)

            quads_steps = self.getStepsList(quads)
            quads_tail = self.nameQuads(quads_steps)

            quads_chord_variation = self.getChordVariation(note, quads_steps)

            formatted_note = self.replacePositionNotes(note).title()

            harmonized_scale.append({
                "mode": mode,
                "grade": self.toRoman(ix+1),
                "triad": {
                    "notes": self.replacePositionNotes(triad),
                    "chord": formatted_note + triad_tail
                },
                "quads": {
                        "notes": self.replacePositionNotes(quads),
                        "chord": formatted_note + quads_tail,
                        "tones": quads_steps,
                        "alternatives": quads_chord_variation
                }
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

    D_minor = RootNote("c#").major

    Harmonization(D_minor).simple()

# ------------------------------------------------------------------------------


if __name__ == '__main__':
    main()


