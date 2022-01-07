#!/bin/bash
while read line
do
	prefetch -O ./ -X 999999999 $line
	cd $line
	if [ -e $line.sra ]; then
		parallel-fastq-dump -s $line.sra -t 32 -O ../ --tmpdir ../ --split-files --gzip && rm $line.sra
		# single end -> fastq-dump <SRA format>
		# pairend end -> fastq-dump --split-files <SRA format>
	else
		echo '[ERROR]' $line 'apparently not successfully loaded' && exit 1
	fi
	cd ..
	rm -rf $line
done 