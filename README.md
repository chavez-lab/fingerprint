# fingerprint toolset

- v1.1
- 4 nov 2015
- volker hovestadt
- german cancer research center
- v.hovestadt@dkfz.de

the fingerprint toolset provides functionality for in-silico genotyping.

the toolset can be used to __confirm expected genotype matches__ (e.g. tumor & normal, WGBS & 450k array), or to __detect unexpected matches__ (e.g. different DNA sources, sample swaps). it consists of two major parts:

#### generate fingerprint files (.fp):
- from BAM alignment files (python script):

```Shell
python fingerprint/bsnp.py fingerprint/snp141Common_RS-CG.n150.vh20151103.bed sample.bam > sample.bam.fp
```

- from 450k data files (R script, RData input file must contain a minfi RGset object of a single sample):

```Shell
Rscript fingerprint/asnp.R fingerprint/snp141Common_RS-CG.n150.vh20151103.bed sample.RData sample sample.fp
```

#### analyze fingerprint files to identify genotype matches:
- R script, input arguments can be individual files and directories, separated by comma:

```Shell
Rscript fingerprint/bsnp_analyze.R -i sampleset/ -o sampleset
```

more detailed information is provided with the help messages and headers of the tools. it is recommended to __understand__ and __adapt__ the settings used in `bsnp_analyze.R`. often it also helps to look at the pairwise correlation table directly (e.g. in excel using conditional color formatting).

the `bsnp_analyze.R` tool follows a very simple statistical approach (i.e. just calculating the pearson correlation), but provides reasonable results. because of that it requires SNPs that are highly variable within the population (avHet >0.2). anyone is invited to come up with a more sophisticated approach.
 

#### included SNP files:
- `snp138Common.n1000.vh20140318.bed`: set of 1000 SNPs (avHet >0.25), selected for coverage in RNA-, Exome- and ChIP-seq datasets, including 450k RS probes. **this file is recommended for comparing sequencing data**.
- `snp141Common_RS-CG.n436.vh20151103.bed`: original set of 436 SNPs (major allele freq <0.95) that can be assessed on the 450k arrays (RS probes and informative CG type I probes).
- `snp141Common_RS-CG.n385.vh20151104.bed`: subset of the previous (consitancy with WGS data, i.e. some probes with very high/low intensities were removed).
- `snp141Common_RS-CG.n192.vh20151103.bed`: subset of the previous (avHet >0.2). **this file is recommended for comparing 450k data, and for comparing 450k to sequencing data**.
- `snp141Common_RS-CG.n50.vh20151104.bed`: subset of the previous (filtered for coverage in Exome- and RNA-seq data).

