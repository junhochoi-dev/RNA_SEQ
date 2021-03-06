import sys, os
import urls

def indexing(species_name, species_code, thread_value): # input = species reference genome
    print("##### START INDEXING :: " + species_code)
    # ht2 파일 폴더 따로 지정 후 넣기...

    # 대부분 인덱싱한 파일의 명칭은 종 코드 번호로 한다..
    # 만약에 인덱싱한 파일이 존재한다면, 그 파일을 이용하는 것이 좋을 것 같다.
    os.system(
        '/program/HISAT2/hisat2-build'
        + ' ' +
        '-p ' + thread_value # thread value
        + ' ' +
        urls.url_species + species_name + '/' + species_name + '.' + species_code + urls.Extension_FASTA
        + ' ' +
        urls.url_species + species_name + '/' + species_code
        )
    print("##### END INDEXING :: " + species_code)

def mapping(species_name, species_code, sample_code, thread_value):
    print("##### START MAPPING :: " + species_code)
    sam = urls.url_samples + sample_code + '/' + sample_code + '.sam'
    if os.path.isfile(sam):
        print("##### RESULT FILES ALREADY EXIST")
    else:
        os.system(
            # FASTQ -> SAM
            '/program/HISAT2/hisat2'
            + ' ' +
            '-p ' + thread_value # thread value
            + ' ' +
            '-x ' + urls.url_species + species_name + '/' + species_code # indexing files
            + ' ' +
            '-1 ' + urls.url_samples + sample_code + '/' + sample_code + '_1_paired.fastq.gz' # forward
            + ' ' +
            '-2 ' + urls.url_samples + sample_code + '/' + sample_code + '_2_paired.fastq.gz' # reverse
            + ' ' +
            '-S ' + sam
            + ' 2>' + urls.url_log + '/' + sample_code + '/' + sample_code + '_HISAT_log' + '$log'
        )
    print("##### END MAPPING :: " + species_code)

def sambam(sample_code, thread_value):
    print("##### START CONVERT SAM TO BAM :: " + sample_code)
    sam = urls.url_samples + sample_code + '/' + sample_code + '.sam'
    bam = urls.url_samples + sample_code + '/' + sample_code + '.bam'
    if os.path.isfile(bam):
        print("##### RESULT FILES ALREADY EXIST")
    else:
        os.system(
            # SAM -> BAM 

            '/program/samtools/bin/samtools view -Sb'
            + ' ' +

            '-@ ' + thread_value # thread value
            + ' ' + 
            
            sam + ' > ' + bam
        )
    print("##### END CONVERT SAM TO BAM :: " + sample_code)

def sorted_bam(sample_code, thread_value):
    print("##### START CONVERT BAM TO SORTED BAM :: " + sample_code)
    bam = urls.url_samples + sample_code + '/' + sample_code + '.bam'
    sorted_bam = urls.url_samples + sample_code + '/' + sample_code + '_sorted.bam'
    if os.path.isfile(sorted_bam):
        print("##### RESULT FILES ALREADY EXIST")
    else:
        os.system(
            # BAM -> SORTED BAM

            '/program/samtools/bin/samtools sort'
            + ' ' +

            '-@ ' + thread_value # thread value
            + ' ' +

            '-o'
            + ' ' + sorted_bam
            + ' ' + bam
        )
    print("##### END CONVERT BAM TO SORTED BAM :: " + sample_code)