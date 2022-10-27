#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Laura Stahlhut
# date: 26.08.2022
import os
import sys


class Participant:
    def __init__(self, participant_data):
        self.data = list(participant_data.items())[0]
        self.id = self.data[0]
        self.mu_file = self.data[1][0]
        self.os_file = self.data[1][1]
        self.ss_file = self.data[1][2]
        self.sstm_file = self.data[1][3]

    def mu_score(self):
        """Proportion of items recalled correctly."""

        with open(os.path.join(sys.argv[1], self.mu_file), 'r') as infile:
            scores_all_trials = []

            # get a score for each trial
            for line in infile.readlines():
                values = [int(x) for x in line.rstrip("\n").split(" ")]  # str -> list; digits seperated by whitespace
                scores_without_padding = list(filter(lambda a: a != -1, values[7:12]))  # 1=true, 0=false
                scores_all_trials.append(
                    (sum(scores_without_padding), len(scores_without_padding)))  # possible score, actual score

            # sum up the scores of the different trials
            sums = [sum(tup) for tup in
                    zip(*scores_all_trials)]  # sum of reached points & all possible points (all trials)
            score = round(sums[0] / sums[1], 3)

            return score

    def operation_span_score(self):
        """Proportion of items recalled in the correct list position."""

        with open(os.path.join(sys.argv[1], self.os_file), 'r') as infile:
            score = self.os_ss_score_calculation(infile.readlines())

            return score

    def sentence_span_score(self):
        """Proportion of items recalled in the correct list position."""

        with open(os.path.join(sys.argv[1], self.ss_file), 'r') as infile:
            score = self.os_ss_score_calculation(infile.readlines())

            return score

    def os_ss_score_calculation(self, lines):
        """Data Structure for OS and SS is identical.
        Proportion of items recalled in the correct list position."""
        scores_all_trials = []

        for line in lines:
            values = [x for x in line.rstrip("\n").split(" ")]
            max_trial_score = int(values[1])

            # get one score per trial (items in the correct position)
            letters_on_screen = list(filter(lambda a: a != "%", values[2:9]))  # remove padding
            typed_letters = list(filter(lambda a: a != "%", values[10:17]))

            count = 0
            for solution, guess in zip(letters_on_screen, typed_letters):
                if solution == guess:
                    count += 1

            scores_all_trials.append((count, max_trial_score))

        # sum up the scores of the different trials
        sums = [sum(tup) for tup in zip(*scores_all_trials)]
        score = round(sums[0] / sums[1], 3)

        return score

    def sstm_score(self):
        """Dividing score by full score (240)."""
        with open(os.path.join(sys.argv[1], self.sstm_file), 'r') as infile:
            score = round(int(infile.readlines()[1].split(" ")[1])/240, 3)

            return score


    def total_score(self):
        """Arithmetic mean of all scores.
        TODO: Check if SSTM should also be included in the mean score."""
        score = round(sum([self.mu_score(), self.operation_span_score(), self.sentence_span_score(), self.sstm_score()])/4, 3)
        return score
