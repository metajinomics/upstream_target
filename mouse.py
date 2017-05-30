#!/usr/bin/python
#This script generate nucloetide sequence from genbank in fasta form
#gzip(gz) support
#Usage: python genbank_to_fna.py genbankfile.gbk > output.fna
#usage: python genbank_to_fna.py genbankfile.gbk.gz > output.fna

import sys
import gzip
from Bio import SeqIO

def main():
    if sys.argv[1][-2:] == 'gz':
        gb_file = gzip.open(sys.argv[1],'rb')
    else:
        gb_file = open(sys.argv[1],'r')

    for gb_record in SeqIO.parse(gb_file,"genbank") :
        genome_name = gb_record.name
        for feat in gb_record.features:
            if feat.type == "gene":
                name = "unkown"
                if("locus_tag" in feat.qualifiers):
                    name = feat.qualifiers['locus_tag'][0]
                elif("gene" in feat.qualifiers):
                    name = feat.qualifiers['gene'][0]
                elif("db_xref" in feat.qualifiers):
                    name = feat.qualifiers['db_xref'][0]
                fstart = feat.location.start
                fend = feat.location.end
                strand = feat.location.strand
#                print ">%s from %s\n%s" %(name,genome_name,feat.extract(gb_record.seq))
                print ">%s\t%s\t%s\t%s" %(name, fstart, fend, strand)
                if strand == 1:
                    print gb_record.seq[int(fstart)-400:int(fstart)]
                elif strand == -1:
                    print gb_record.seq[int(fend):int(fend)+400].reverse_complement()


if __name__ == '__main__':
    main()
