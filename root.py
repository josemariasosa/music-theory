#!/usr/bin/env python
# coding=utf-8

# ------------------------------------------------------------------------------
# Building scales from any root note | Music Theory
# ------------------------------------------------------------------------------
# jose maria sosa

import json
import inspect
import numpy as np


class RootNote(object):

    """ Available scales:
            aeolian_dominant
            algerian
            arabic
            balinese_pelog
            byzantine
            chinese
            diminished
            dominant_diminished
            egyptian
            eight_tones_spanish
            enigmatic
            geez
            harmonic_major
            harmonic_minor
            hirajoshi
            hungarian_gypsy
            japanese
            lydian_dominant
            major
            major_bebop
            major_pentatonic
            major_pentatonic_blues
            melodic_major
            melodic_minor
            minor
            minor_bebop
            minor_pentatonic
            minor_pentatonic_blues
            natural_major
            natural_minor
            neapolitan_minor
            nine_tone
            octatonic_half_whole
            octatonic_whole_half
            oriental
            romanian_minor
            spanish_gypsy
            super_locrian
            symmetrical_augmented
            whole_tone
            yo
    """

    def __init__(self, root):

        # 1. Define the list of 12 notes.
        self.notes = self.getNotes()
        self.num_notes = list(range(12))

        # 2. Define the root position.
        self.root = root.lower()
        self.root_position = self.getRootPosition(self.root)

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
    
    @property
    def aeolian_dominant(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------
    
    @property
    def algerian(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def arabic(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def balinese_pelog(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def byzantine(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def chinese(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def diminished(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def dominant_diminished(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def egyptian(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def eight_tones_spanish(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def enigmatic(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def geez(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def harmonic_major(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def harmonic_minor(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def hirajoshi(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def hungarian_gypsy(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def japanese(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def lydian_dominant(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def major(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def major_bebop(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def major_pentatonic(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def major_pentatonic_blues(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def melodic_major(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def melodic_minor(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def minor(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def minor_bebop(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def minor_pentatonic(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def minor_pentatonic_blues(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def natural_major(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def natural_minor(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def neapolitan_minor(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def nine_tone(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def octatonic_half_whole(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def octatonic_whole_half(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def oriental(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def romanian_minor(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def spanish_gypsy(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def super_locrian(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def symmetrical_augmented(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def whole_tone(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------

    @property
    def yo(self):
        scale_name = inspect.stack()[0][3]
        positions = self.positionPattern(scale_name)
        return {
            'positions': positions,
            'notes': self.replacePositionNotes(positions),
            'root': self.root,
            'scale_name': scale_name
        }

    # --------------------------------------------------------------------------
# ------------------------------------------------------------------------------


def main():

    note = RootNote("G")

    print(note)
    print('\nThe major scale is: ')
    print(note.major['notes'])
    print('\nThe symmetrical augmented scale is: ')
    print(note.symmetrical_augmented['notes'])
    print('\nThe japanese scale is: ')
    print(note.japanese['notes'])

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
