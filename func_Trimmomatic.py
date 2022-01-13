import sys, os
import urls

# single end





# paired end

def trimming(sample_code, thread_value):
    print("TRIMMING 실행")
    sample_code_forward = sample_code + '_1'
    sample_code_reverse = sample_code + '_2'
    os.system('mkdir ' + urls.url_log + '/' + sample_code + '/')
    os.system(
        'java -jar /program/Trimmomatic/trimmomatic-0.39.jar PE'
        + ' ' +

        '-threads' +
        + ' ' +
        thread_value
        + ' '
        
        # + 'sample_code_forward.fq.gz sample_code_reverse.fq.gz'
        + urls.url_samples + sample_code + '/' + sample_code_forward + '.fastq.gz' + ' '
        + urls.url_samples + sample_code + '/' + sample_code_reverse + '.fastq.gz' + ' '

        # 'output_forward_paired.fq.gz output_forward_unpaired.fq.gz output_reverse_paired.fq.gz output_reverse_unpaired.fq.gz'
        + urls.url_samples + sample_code + '/' + sample_code_forward + '_paired.fastq.gz' + ' '
        + urls.url_samples + sample_code + '/' + sample_code_forward + '_unpaired.fastq.gz' + ' '
        + urls.url_samples + sample_code + '/' + sample_code_reverse + '_paired.fastq.gz' + ' '
        + urls.url_samples + sample_code + '/' + sample_code_reverse + '_unpaired.fastq.gz' + ' '

        'ILLUMINACLIP:/program/Trimmomatic/adapters/TruSeq3-PE.fa:2:30:10:2:True LEADING:3 TRAILING:3 MINLEN:36'
        + ' 2>' + urls.url_log + '/' + sample_code + '/' + sample_code + '_Trimmomatic_log' + '$log'
    )
    