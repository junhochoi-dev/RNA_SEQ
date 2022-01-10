#!/bin/bash
line=$1
path=$2
prefetch -O $path -X 999999999 $line
cd $line
if [ -e $line.sra ]; then
	parallel-fastq-dump -s $line.sra -t 30 -O $path --tmpdir ../ --split-files --gzip && rm $line.sra
	# single end -> fastq-dump <SRA format>
	# pairend end -> fastq-dump --split-files <SRA format>pre
	#-t|--threads         number of threads
	#-s|--sra-id          SRA id
	#-O|--outdir          output directory
else
	echo '[ERROR]' $line 'Apparently Not Successfully Downloaded' && exit 1
fi
cd ..
rm -rf $line


# $1, $2 ... $n 셀 실행 후 입력되는 매개변수를 해당 인자로 받는다.