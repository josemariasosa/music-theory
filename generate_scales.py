#!/usr/bin/env python
# coding=utf-8

# ------------------------------------------------------------------------------
# Update Product Body in Shopify | Mi Refacción
# ------------------------------------------------------------------------------
# jose maria sosa

import numpy as np


class RootNote(object):

    """docstring for RootNote"""

    def __init__(self, root):
        self.notes_sharp = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]
        self.notes_flat = ["a", "bb", "b", "c", "db", "d", "eb", "e", "f", "gb", "g", "ab"]

        self.root = root
        
    # --------------------------------------------------------------------------
    
    @property
    def major(self):
        step_pattern = [1, 1, 0.5, 1, 1, 1, 0.5]

        if self.root in self.notes_sharp:
            key_index = self.notes_sharp.index(self.root)
            sorted_notes = self.notes_sharp[key_index:] + self.notes_sharp[:key_index]

        elif self.root in self.notes_flat:
            key_index = self.notes_flat.index(self.root)
            sorted_notes = self.notes_flat[key_index:] + self.notes_flat[:key_index]

        sorted_notes = sorted_notes + [sorted_notes[0]]

        step_pattern = [int(x*2) for x in step_pattern]
        step_pattern = list(np.cumsum(step_pattern))

        scale = []
        for index, value in enumerate(sorted_notes):
            if index == 0:
                scale.append(value)
            elif index in step_pattern:
                scale.append(value)

        return scale
    
    # --------------------------------------------------------------------------

    @property
    def minor(self):
        step_pattern = [1, 0.5, 1, 1, 0.5, 1, 1]

        if self.root in self.notes_sharp:
            key_index = self.notes_sharp.index(self.root)
            sorted_notes = self.notes_sharp[key_index:] + self.notes_sharp[:key_index]

        elif self.root in self.notes_flat:
            key_index = self.notes_flat.index(self.root)
            sorted_notes = self.notes_flat[key_index:] + self.notes_flat[:key_index]

        sorted_notes = sorted_notes + [sorted_notes[0]]

        step_pattern = [int(x*2) for x in step_pattern]
        step_pattern = list(np.cumsum(step_pattern))

        scale = []
        for index, value in enumerate(sorted_notes):
            if index == 0:
                scale.append(value)
            elif index in step_pattern:
                scale.append(value)

        return scale

    # --------------------------------------------------------------------------

    @property
    def natural_minor(self):
        step_pattern = [1, 0.5, 1, 1, 0.5, 1, 1]

        if self.root in self.notes_sharp:
            key_index = self.notes_sharp.index(self.root)
            sorted_notes = self.notes_sharp[key_index:] + self.notes_sharp[:key_index]

        elif self.root in self.notes_flat:
            key_index = self.notes_flat.index(self.root)
            sorted_notes = self.notes_flat[key_index:] + self.notes_flat[:key_index]

        sorted_notes = sorted_notes + [sorted_notes[0]]

        step_pattern = [int(x*2) for x in step_pattern]
        step_pattern = list(np.cumsum(step_pattern))

        scale = []
        for index, value in enumerate(sorted_notes):
            if index == 0:
                scale.append(value)
            elif index in step_pattern:
                scale.append(value)

        return scale

    # --------------------------------------------------------------------------

    @property
    def harmonic_minor(self):
        step_pattern = [1, 0.5, 1, 1, 0.5, 1.5, 0.5]

        if self.root in self.notes_sharp:
            key_index = self.notes_sharp.index(self.root)
            sorted_notes = self.notes_sharp[key_index:] + self.notes_sharp[:key_index]

        elif self.root in self.notes_flat:
            key_index = self.notes_flat.index(self.root)
            sorted_notes = self.notes_flat[key_index:] + self.notes_flat[:key_index]

        sorted_notes = sorted_notes + [sorted_notes[0]]

        step_pattern = [int(x*2) for x in step_pattern]
        step_pattern = list(np.cumsum(step_pattern))

        scale = []
        for index, value in enumerate(sorted_notes):
            if index == 0:
                scale.append(value)
            elif index in step_pattern:
                scale.append(value)

        return scale

    # --------------------------------------------------------------------------

    @property
    def melodic_minor(self):
        step_pattern = [1, 0.5, 1, 1, 1, 1, 0.5]

        if self.root in self.notes_sharp:
            key_index = self.notes_sharp.index(self.root)
            sorted_notes = self.notes_sharp[key_index:] + self.notes_sharp[:key_index]

        elif self.root in self.notes_flat:
            key_index = self.notes_flat.index(self.root)
            sorted_notes = self.notes_flat[key_index:] + self.notes_flat[:key_index]

        sorted_notes = sorted_notes + [sorted_notes[0]]

        step_pattern = [int(x*2) for x in step_pattern]
        step_pattern = list(np.cumsum(step_pattern))

        scale = []
        for index, value in enumerate(sorted_notes):
            if index == 0:
                scale.append(value)
            elif index in step_pattern:
                scale.append(value)

        return scale

    # --------------------------------------------------------------------------
# ------------------------------------------------------------------------------

def stepDistance(from_note, to_note):

    notes = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "g#"]

    from_index = notes.index(from_note)

    sorted_notes = notes[from_index:] + notes[:from_index]

    to_index = sorted_notes.index(to_note)

    if to_index % 2 == 0:
        results = int(to_index/2)
    else:
        results = to_index/2

    return results

# ------------------------------------------------------------------------------

def getMode(note, scale):

    scale = scale[:-1]

    note_index = scale.index(note)

    sorted_notes = scale[note_index:] + scale[:note_index]
    sorted_notes = sorted_notes + [sorted_notes[0]]

    steps = []

    for index, value in enumerate(sorted_notes):
        if index > 0:
            f = sorted_notes[index-1]
            t = sorted_notes[index]
            steps.append(stepDistance(f, t))

    ionian = [1, 1, 0.5, 1, 1, 1, 0.5]
    dorian = [1, 0.5, 1, 1, 1, 0.5, 1]
    phrigian = [0.5, 1, 1, 1, 0.5, 1, 1]
    lydian = [1, 1, 1, 0.5, 1, 1, 0.5]
    mixolydian = [1, 1, 0.5, 1, 1, 0.5, 1]
    aolian = [1, 0.5, 1, 1, 0.5, 1, 1]
    locrian = [0.5, 1, 1, 0.5, 1, 1, 1]

    if all([x==0 for x in np.subtract(steps, ionian)]):
        return 'ionian'
    elif all([x==0 for x in np.subtract(steps, dorian)]):
        return 'dorian'
    elif all([x==0 for x in np.subtract(steps, phrigian)]):
        return 'phrigian'
    elif all([x==0 for x in np.subtract(steps, lydian)]):
        return 'lydian'
    elif all([x==0 for x in np.subtract(steps, mixolydian)]):
        return 'mixolydian'
    elif all([x==0 for x in np.subtract(steps, aolian)]):
        return 'aolian'
    elif all([x==0 for x in np.subtract(steps, locrian)]):
        return 'locrian'

# ------------------------------------------------------------------------------

def harmonization(scale):

    major3 = 2
    minor3 = 1.5

    seven_notes = scale[:-1]

    long_scale = seven_notes + scale

    for note in seven_notes:

        mode = getMode(note, scale)
        note_index = long_scale.index(note)

        triad = [long_scale[note_index], long_scale[note_index+2], long_scale[note_index+4]]
        steps = [stepDistance(triad[0], triad[1]), stepDistance(triad[1], triad[2])]

        if (steps[0] == major3) and (steps[1] == minor3):
            tail = 'major'

        elif (steps[0] == minor3) and (steps[1] == major3):
            tail = 'minor'

        elif (steps[0] == minor3) and (steps[1] == minor3):
            tail = 'diminished'

        elif (steps[0] == major3) and (steps[1] == major3):
            tail = 'augmented'

        else:
            tail = 'unnamed'

        print(triad[0], tail, '---', mode)
        print(triad)

        print ('------------------------------')

# ------------------------------------------------------------------------------

def main():

    a = RootNote("d")
    harmonization(a.melodic_minor)
    # print(stepDistance("b", "a"))
    # print(harmonization(a.major))


if __name__ == '__main__':
    main()

