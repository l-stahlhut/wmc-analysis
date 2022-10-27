#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Laura Stahlhut
# date: 26.08.2022

import os
import sys
import re

from participant import Participant


def get_filenames():
    """Read all files in the data directory and return a list of dictionaries.
    files_list = [{'041': ['MU-041.dat', 'OS-041.dat', 'SS-041.dat', 'SSTM-041.dat']}, ...] """

    directory = sys.argv[1]
    filenames = [f for f in os.listdir(directory) if f.endswith('.dat')]
    ids = sorted(set([re.sub(r'(MU|OS|SS|SSTM)-', '', f.rstrip(".dat")) for f in filenames]))


    files_list = [] # list of files per participant

    for id in ids:
        d = {id: []}
        d[id] = [file for file in filenames if id in file]
        d[id].sort()
        files_list.append(d)

    return files_list


def main():
    # get a list of dictionaries {ID: [file1, file2, file3, file3]} for each participant
    with open("scores.txt", "w") as outfile:
        outfile.write("ID\tMU Score\tOS Score\tSS Score\tSSTM score\tTotal score\t")
        for file in get_filenames():
            p = Participant(file)

            outfile.write(str(p.id) + "\t" + str(p.mu_score()) + "\t" + str(p.operation_span_score()) + "\t" +
                          str(p.sentence_span_score()) + "\t" + str(p.sstm_score()) + "\t" + str(p.total_score()) + "\n")

    print("An overview of the scores can be found in the file scores.txt")

    # printing average overall score of all participants to terminal
    all_total_scores = []
    for file in get_filenames():
        p = Participant(file)
        all_total_scores.append(p.total_score())
    average_overall_score = sum(all_total_scores)/len(all_total_scores)

    print("Average overall score of all participants:", average_overall_score)


if __name__ == "__main__":
    main()