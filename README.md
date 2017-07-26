# upstream_target

Download genbank file of GRCm38.p5
```
python upstream_target/fetch_genbank.py mouse_ncbi_id mouse_genbank
```

Find upstream reagion of gene of interest
```
for x in mouse_genbank/*.gbk;do python upstream_target/get_upstream.py $x target_gene_upregulated_by_300_q_0_05.csv;done > all_upstream.fa
```

Make samtools pileup command line
```
for x in fastq/*.sorted.bam;do python upstream_target/make_samtools_command.py mus.txt all_upstream.fa $x;done > command.samtools_pileup.sh
```

Run samtools pileup
```
cat command.samtools_pileup.sh |parallel
```

