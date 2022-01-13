#!/bin/bash
line=$1 # sample code
path=$2 # sample folder path
# echo $line
# echo $path
# echo $path$line/$line.sra
# pwd
prefetch -O $path -X 999999999 $line
if [ -e $path$line/$line.sra ]; then
	parallel-fastq-dump --sra-id $path$line/$line.sra -t 30 --outdir $path$line --tmpdir ../ --split-files --gzip # && rm $path.sra
	# single end -> fastq-dump <SRA format>
	# pairend end -> fastq-dump --split-files <SRA format>pre
	#-t | --threads         number of threads
	#-s | --sra-id          SRA id
	#-O | --outdir          output directory
else
	echo '[ERROR]' $line 'Apparently Not Successfully Downloaded' && exit 1
fi
rm -rf $path$line/$line.sra

# $1, $2 ... $n 셀 실행 후 입력되는 매개변수를 해당 인자로 받는다.

# METADATA 도 다운로드 해야한다. *****