import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import urls

def indexing(species_name, species_code): # input = species reference genome
    os.system(
        '/program/HISAT2/hisat2-build'
        + ' ' +
        '-p 30' # -p 쓰레드값 : 서버에 무리가 갈 수 있으니 적당히.. 30 안넘기게..
        # -p : indexing 할 때 사용할 cpu 갯수 입니다.
        + ' ' +
        '00_data/data__species/' + species_name + '/' + species_name + '.' + species_code + '.dna.toplevel.fa'
        + ' ' +
        '00_data/data__species/' + species_name + '/' + species_code
        )

# ht2 파일 폴더 따로 지정 후 넣기...

# 대부분 인덱싱한 파일의 명칭은 종 코드 번호로 한다..
# 만약에 인덱싱한 파일이 존재한다면, 그 파일을 이용하는 것이 좋을 것 같다.

# data
# species
# Gallus_gallus
# 1. reference genome 2. gene annotation 3. hisat indexing files(ht files)
# 4.SAM 기존의 샘플이 들어가니까 빼자 5. BAM 같은 폴더에 BAM 분류

def HISAT(species_name, species_code, sample_code):
    os.system(
        # FASTQ -> SAM
        '/program/HISAT2/hisat2'
        + ' ' +
        '-p 40'
        + ' ' +
        '-x ' + urls.url_data + '/data__species/' + species_name + '/' + species_code # 인덱싱
        + ' ' +
        '-1 ' + urls.url_data + '/data__samples/' + sample_code + '/' + sample_code + '_1_paired.fastq.gz' # forward
        + ' ' +
        '-2 ' + urls.url_data + '/data__samples/' + sample_code + '/' + sample_code + '_2_paired.fastq.gz' # reverse
        + ' ' +
        '-S ' + urls.url_data + '/data__samples/' + sample_code + '/' + sample_code + '.sam'
    )

def sambam(sample_code):
    os.system(
        # SAM -> BAM 

        '/program/samtools/bin/samtools view -Sb -@ 30'
        + ' ' +
        urls.url_data + '/data__samples/' + sample_code + '/' + sample_code + '.sam'
        + ' > ' +
        urls.url_data + '/data__samples/' + sample_code + '/' + sample_code + '.bam'
    )

def sorted_bam(sample_code):
    os.system(
        # BAM -> SORTED BAM

        '/program/samtools/bin/samtools sort -@ 30 -o'
        + ' ' +
        urls.url_data + '/data__samples/' + sample_code + '/' + sample_code + '_sorted.bam'
        + ' ' +
        urls.url_data + '/data__samples/' + sample_code + '/' + sample_code + '.bam'
    )
# hisat2 -p 8 -x IndexName -1 forward.fastq -2 reverse.fastq -S output.sam  --dta-cufflinks