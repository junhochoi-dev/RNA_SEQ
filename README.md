*****

# RNA - SEQ


## About RNA Sequencing...

>[RNA-SEQ](https://en.wikipedia.org/wiki/RNA-Seq) (named as an abbreviation of RNA sequencing) is a sequencing technique which uses next-generation sequencing (NGS) to reveal the presence and quantity of RNA in a biological sample at a given moment, analyzing the continuously changing cellular transcriptome.

![RNASEQ](https://media.springernature.com/lw685/springer-static/image/art%3A10.1186%2Fs13045-020-01005-x/MediaObjects/13045_2020_1005_Fig4_HTML.png?raw=true)

>
    [Reference]
    ENSEMBL             : https://asia.ensembl.org/index.html
    GEO DATASETS        : https://www.ncbi.nlm.nih.gov/gds
    SRA RUN SELECTOR    : https://www.ncbi.nlm.nih.gov/Traces/study/
    TRIMMOMATIC         : http://www.usadellab.org/cms/?page=trimmomatic
    HISAT2              : http://daehwankimlab.github.io/hisat2/manual/
    SAMTOOL             : http://www.htslib.org/doc/samtools.html
    FeatureCounts       : http://subread.sourceforge.net/

*****

>## 01. TRIMMING :: Trimmomatic

[..code](https://github.com/junhochoi-dev/RNA_SEQ/blob/main/func_Trimmomatic.py)

##### TRIMMING [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic)
>
    Input 	: FastQ(forward, reverse) -> SAMPLE 
    output	: FastQ(forward, reverse X paired, unpaired)

*****

>## 02. MAPPING (ALIGNMENT) :: HISAT2 & SAMTOOL

[..code](https://github.com/junhochoi-dev/RNA_SEQ/blob/main/func_HISAT.py)

##### INDEXING [HISAT2](http://daehwankimlab.github.io/hisat2/manual/)
>
    Input 	: FASTA
    output	: 8 indexing files

##### FastQ -> SAM [HISAT2](http://daehwankimlab.github.io/hisat2/manual/)
>
    Input 	: FastQ(forward, reverse X paired) + Reference Genome(primary or toplevel)
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

> ## 03. QUANTIFICATION :: FeatureCounts

[..code](https://github.com/junhochoi-dev/RNA_SEQ/blob/main/func_FeatureCount.py)

##### QUANTIFICATION [FeatureCounts](http://subread.sourceforge.net/)
>
    Input 	: sorted BAM / Gene Annotation
    output	: result & result.summary

*****

> ## STUDY LIST

1. ## Natural Mucosal Barriers and COVID-19 in Children

    STUDY_CODE : GSE172274

    SAMPLE_CODE : SRR14267546 - SRR14267560

    [..link](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE172274)


*****

[Reference] How to use MARKDOWN : https://gist.github.com/ihoneymon/652be052a0727ad59601