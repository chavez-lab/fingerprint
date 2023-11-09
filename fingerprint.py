#!/usr/bin/env python3

import argparse
import subprocess
import pathlib

def run_methylation():
    # Replace this with the command for script A
    subprocess.run(["Rscript", "asnp.R", ])

def run_sequencing():
    # Replace this with the command for script B
    subprocess.run(["python", "script_b.py"])

def main():
    parser = argparse.ArgumentParser(description="Entry program for fingerprinting analysis.")
    parser.add_argument('-i','--input',required=True, help="Path to .bam or .idat file. Should end with either suffix.")
    parser.add_argument('-b','--snp_set', help="Path to a set of snp positions in .bed format. Default is platform-specific.")
    parser.add_argument('-n','--name', help="Sample name for output files. Default is basename of input.")
    parser.add_argument('-o','--output', help="Output filename. Default is [name].fp.")

    args = parser.parse_args()

    fingerprint_home=pathlib.Path(__file__).parent.resolve()
    asnp = pathlib.Path(fingerprint_home,"asnp.R")
    bsnp = pathlib.Path(fingerprint_home,"bsnp.py")
    dnam_bed=pathlib.Path(fingerprint_home,"snp141Common_RS-CG.n192.vh20151104.bed")
    seq_bed=pathlib.Path(fingerprint_home,"snp138Common.n1000.vh20140318.bed")

    input_file=pathlib.Path(args.input)
    if args.name == None:
        args.name = input_file.stem
    if args.output == None:
        args.output = pathlib.Path(pathlib.Path.cwd(),args.name+'.fp')

    # Detect file type and construct fingerprint command
    if input_file.suffix == '.idat':
        if args.snp_set == None:
            args.snp_set = dnam_bed
        command = ['Rscript', asnp, args.snp_set, input_file, args.name, args.output]
        subprocess.run(command)
    elif input_file.suffix == '.bam':
        if args.snp_set == None:
            args.snp_set = seq_bed
        outfile = open(args.output,'w')
        command = ['python', bsnp, args.snp_set, input_file, '--name', args.name]
        subprocess.call(command, stdout=outfile)
        outfile.close()
    else:
        raise ValueError("Input file should be .bam or .idat")

    print("finished running command:\n"+" ".join(map(str,command)))
if __name__ == "__main__":
    main()
