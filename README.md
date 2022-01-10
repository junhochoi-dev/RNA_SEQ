# RNA - SEQ

*****

### About RNA SEQUENCING

>[RNA-SEQ](https://en.wikipedia.org/wiki/RNA-Seq) (named as an abbreviation of RNA sequencing) is a sequencing technique which uses next-generation sequencing (NGS) to reveal the presence and quantity of RNA in a biological sample at a given moment, analyzing the continuously changing cellular transcriptome.

![RNASEQ](./disk4/bicjh/rna_seq/rnaseq.png?raw=true)

>
    [Reference]
    GEO DATASETS        : https://www.ncbi.nlm.nih.gov/gds
    SRA RUN SELECTOR    : https://www.ncbi.nlm.nih.gov/Traces/study/
    TRIMMOMATIC         : http://www.usadellab.org/cms/?page=trimmomatic
    HISAT2              : http://daehwankimlab.github.io/hisat2/manual/
    SAMTOOL             : http://www.htslib.org/doc/samtools.html
    FeatureCounts       : http://subread.sourceforge.net/

*****

### 01. TRIMMING :: Trimmomatic

##### TRIMMING [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic)
>
    Input 	: FastQ(forward, reverse) -> SAMPLE 
    output	: FastQ(forward, reverse X paired, unpaired)

*****

### 02. MAPPING (ALIGNMENT) :: HISAT2 & SAMTOOL

##### INDEXING [HISAT2](http://daehwankimlab.github.io/hisat2/manual/)
>
    Input 	: FASTA
    output	: 8 indexing files

##### FastQ -> SAM [HISAT2](http://daehwankimlab.github.io/hisat2/manual/)
>
    Input 	: FastQ(forward, reverse) + Reference Genome(primary or toplevel)
    output	: SAM

##### SAM -> BAM [SAMTOOL](http://www.htslib.org/doc/samtools.html)
>
    Input 	: SAM
    output	: BAM

##### BAM -> sorted BAM [SAMTOOL](http://www.htslib.org/doc/samtools.html)
>
    Input 	: BAM
    output	: sorted BAM

*****

### 03. QUANTIFICATION :: FeatureCounts

##### QUANTIFICATION [FeatureCounts](http://subread.sourceforge.net/)
>
    Input 	: BAM / Gene Annotation
    output	: result & result.summary

*****

[Reference] How to use MARKDOWN : https://gist.github.com/ihoneymon/652be052a0727ad59601