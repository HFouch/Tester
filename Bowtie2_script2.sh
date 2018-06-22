#!/bin/bash
#PBS -l nodes=1:ppn=4
#PBS -l mem=20Gb
#PBS -l walltime=1:00:00

cd $PBS_O_WORKDIR

module load app/bowtie/2.2.8

#bowtie2-build Test_Genome_sequence.fasta GenomeINDEX

bowtie2 --mp 2,0.9999 --score-min L,-2,-2 -x GenomeINDEX -U TD_fragments_1bp_offset.fastq -S SAM18.sam


