import sys, os
import urls

# single end

def trimming_se(sample_code, thread_value):
    print("##### START TRIMMOMATIC SE :: " + sample_code)
    
    # java -jar trimmomatic-0.35.jar SE -phred33 input.fq.gz output.fq.gz ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36
    
    print("##### END TRIMMOMATIC SE :: " + sample_code)



# paired end

def trimming(sample_code, thread_value):
    print("##### START TRIMMOMATIC :: " + sample_code)
    sample_code_forward = sample_code + '_1'
    sample_code_reverse = sample_code + '_2'

    result_forward_paired = urls.url_samples + sample_code + '/' + sample_code_forward + '_paired.fastq.gz'
    result_forward_unpaired = urls.url_samples + sample_code + '/' + sample_code_forward + '_unpaired.fastq.gz'
    result_reverse_paired = urls.url_samples + sample_code + '/' + sample_code_reverse + '_paired.fastq.gz'
    result_reverse_unpaired = urls.url_samples + sample_code + '/' + sample_code_reverse + '_unpaired.fastq.gz'
    if os.path.isfile(sample_forward_paired) and os.path.isfile(sample_forward_unpaired) and os.path.isfile(sample_reverse_paired) and os.path.isfile(sample_reverse_unpaired):
        print("##### RESULT FILES ALREADY EXIST")
    else:
        os.system('mkdir ' + urls.url_log + '/' + sample_code + '/')
        os.system(
            'java -jar /program/Trimmomatic/trimmomatic-0.39.jar PE'
            + ' ' +

            '-threads'
            + ' ' +
            thread_value
            + ' '
            
            # + 'sample_code_forward.fq.gz sample_code_reverse.fq.gz'
            + urls.url_samples + sample_code + '/' + sample_code_forward + '.fastq.gz' + ' '
            + urls.url_samples + sample_code + '/' + sample_code_reverse + '.fastq.gz' + ' '

            # 'output_forward_paired.fq.gz output_forward_unpaired.fq.gz output_reverse_paired.fq.gz output_reverse_unpaired.fq.gz'
            + result_forward_paired + ' '
            + result_forward_unpaired + ' '
            + result_reverse_paired + ' '
            + result_reverse_unpaired + ' '

            'ILLUMINACLIP:/program/Trimmomatic/adapters/TruSeq3-PE.fa:2:30:10:2:True LEADING:3 TRAILING:3 MINLEN:36'
            + ' 2>' + urls.url_log + '/' + sample_code + '/' + sample_code + '_Trimmomatic_log' + '$log'
    )
    
    print("##### END TRIMMOMATIC :: " + sample_code)