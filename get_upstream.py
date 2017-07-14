#!/usr/bin/python
#This script generate nucloetide sequence from genbank in fasta form
#gzip(gz) support
#Usage: python genbank_to_fna.py genbankfile.gbk > output.fna
#usage: python genbank_to_fna.py genbankfile.gbk.gz > output.fna
#usage: python mouse.py genbankfile gene_of_intestest.txt > upstreat.fa

import sys
import gzip
from Bio import SeqIO


def main():
    num = 1000
    d = {}
    for line in open(sys.argv[2],'r'):
        gene_name = line.strip()
        d[gene_name] = gene_name

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
                
                if d.has_key(name):

                    fstart = feat.location.start
                    fend = feat.location.end
                    strand = feat.location.strand
                    
                    if strand == 1:
                        st = int(fstart)-num
                        ed = int(fstart) 
                        print ">%s\t%s\t%s\t%s\t%s" %(genome_name,name, st, ed, strand)
                        print gb_record.seq[st:ed]
                    elif strand == -1:
                        st = int(fend)
                        ed = int(fend)+num
                        print ">%s\t%s\t%s\t%s\t%s" %(genome_name,name, st, ed, strand)
                        print gb_record.seq[st:ed].reverse_complement()

if __name__ == '__main__':
    main()
