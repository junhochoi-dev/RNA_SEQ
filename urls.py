from os import system

# url 뒤에 다 / 붙여주자.

url_program = '/program/'

url = "/disk4/bicjh/rna_seq"
url_samples = url + '/00_data/data__samples/'
url_species = url + '/00_data/data__species/'

url_log = "/disk4/bicjh/rna_seq/00_data/log"

url_ensembl = "http://ftp.ensembl.org/pub/release-105/"

Extension_FASTA = ".dna.toplevel.fa"
Extension_GTF = ".105.gtf"
Extension_FASTA_zip = ".dna.toplevel.fa.gz"
Extension_GTF_zip = ".105.gtf.gz"

## 각 프로그램 툴 별로 url 지정
# Trimming : /program/Trimmomatic/trimmomatic-0.39.jar
# indexing : /program/HISAT2/hisat2-build
# mapping : /program/HISAT2/hisat2
# sam to bam : /program/samtools/bin/samtools
# bam to sorted_bam : /program/samtools/bin/samtools
# featurecount : /program/subread/bin/featureCounts

url_data = "/disk4/bicjh/rna_seq/00_data"


# name -> download_# 바꾸자...
url_reference_genome = "http://ftp.ensembl.org/pub/release-105/fasta/gallus_gallus/dna/Gallus_gallus.GRCg6a.dna.toplevel.fa.gz"
url_gene_annotation = "http://ftp.ensembl.org/pub/release-105/gtf/gallus_gallus/Gallus_gallus.GRCg6a.105.gtf.gz"
