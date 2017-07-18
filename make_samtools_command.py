#!/usr/bin/python

"""
this script generate command for samtools
usage: python make_samtools_command.py mus.txt all_upstream.fa ISU-DSK-12.sam.bam.sorted.bam > command.samtools.mpileup.sh

"""
import sys

def main():
    #read mus
    d = {}
    bam = sys.argv[3]
    for n,line in enumerate(open(sys.argv[1],'r')):
        if n==0:
            continue
        spl = line.strip().split('\t')
        if spl[2] == '.' or spl[2] == 'MT':
            continue
        d[spl[3].split('.')[0]] = spl[1].lower()+spl[2]

    for line in open(sys.argv[2],'r'):
        if not line[:1] == ">":
            continue
        spl = line[1:].strip().split('\t')
        print "samtools mpileup -r "+d[spl[0]]+":"+spl[2]+"-"+spl[3]+" -f GRCm38.p5.genome.fa -o "+bam+spl[1]+".pileup "+bam

if __name__ == '__main__':
    main()
