#!/usr/bin/env python

import numpy as np
import argparse
import os


def initialize():

    parser = argparse.ArgumentParser(description='generate a random swim workout of a given length')

    parser.add_argument('-l', '--length', default=2000, type=int, help='length of workout')
    parser.add_argument('-sets', default=2, type=int, help='Number of sets')

    args = parser.parse_args()

    return args


class Workout(object):

    def __init__(self):

        self.file_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.workout = []
        self.workout.append('------------ Swim Workout Generator -----------')
        with open('%s/warmup.txt' % self.file_location, 'r') as f:
            for line in f:
                if line[0] != ";":
                    self.workout.append(line)

    def write_workout(self, name='workout.txt'):

        with open(name, 'w') as f:
            for line in self.workout:
                f.write(line)

if __name__ == "__main__":

    args = initialize()

    workout = Workout()
    workout.write_workout()