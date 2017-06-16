#!/usr/bin/python

"""
this script find transcription start site from transcriptome date
usage: python find_tc_start_site.py pileupfile
example: python find_tc_start_site.py filename.mpileup
"""

import sys
import numpy

def main():
    window = 10
    inc_factor = 4
    loc = []
    count = []
    start = 0
    for line in open(sys.argv[1],'r'):
        spl = line.strip().split('\t')
        loc.append(int(spl[1]))
        count.append(int(spl[3]))
    
    for i in range(0,len(count)- (2*window) ):
        first = numpy.mean(count[i:i+window])
        second = numpy.mean(count[i+window:i+(window*2)])

        if second/first > inc_factor:
            start = i+window
            break
    print loc[start]

if __name__ == '__main__':
    main()
