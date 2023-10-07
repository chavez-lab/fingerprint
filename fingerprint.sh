#!/bin/bash

# Usage: sbatch fingerprint.sh [bam_file] [hg19 or hg38]
# output to current directory.
# Requires:
#	python 2.7
#	pysam  0.7.8

MYDIR="$(dirname "$(readlink -f "$0")")"
BAM=$1
REF=$2

# Parse inputs
SAMPLENAME=$(basename $BAM .bam)
if [ $REF = "hg19" ]; then
	BED=$MYDIR/snp138Common.n1000.vh20140318.bed
elif [ $REF = "hg38" ]; then
	BED=$MYDIR/snp138Common.n1000.vh20140318.hg38.bed
else
	echo "2nd arg should be 'hg19' or 'hg38'"
	exit 1
fi
CMD=$MYDIR/bsnp.py
python2 $CMD $BED $BAM \
	> ${SAMPLENAME}.fp
