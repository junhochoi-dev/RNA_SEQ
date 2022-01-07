import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import urls

# single end





# paired end

def trimming(sample_code):
    print("TRIMMING 실행")
    sample_code_forward = sample_code + '_1'
    sample_code_reverse = sample_code + '_2'
    os.system(
        'java -jar /program/Trimmomatic/trimmomatic-0.39.jar PE'
        + ' ' +
        '-threads 30'
        + ' '

        # + 'sample_code_forward.fq.gz sample_code_reverse.fq.gz'
        + '/disk4/bicjh/rna_seq/00_data/data__samples/' + sample_code + '/' + sample_code_forward + '.fastq.gz' + ' '
        + '/disk4/bicjh/rna_seq/00_data/data__samples/' + sample_code + '/' + sample_code_reverse + '.fastq.gz' + ' '

        # 'output_forward_paired.fq.gz output_forward_unpaired.fq.gz output_reverse_paired.fq.gz output_reverse_unpaired.fq.gz'
        + '/disk4/bicjh/rna_seq/00_data/data__samples/' + sample_code + '/' + sample_code_forward + '_paired.fastq.gz' + ' '
        + '/disk4/bicjh/rna_seq/00_data/data__samples/' + sample_code + '/' + sample_code_forward + '_unpaired.fastq.gz' + ' '
        + '/disk4/bicjh/rna_seq/00_data/data__samples/' + sample_code + '/' + sample_code_reverse + '_paired.fastq.gz' + ' '
        + '/disk4/bicjh/rna_seq/00_data/data__samples/' + sample_code + '/' + sample_code_reverse + '_unpaired.fastq.gz' + ' '

        'ILLUMINACLIP:/program/Trimmomatic/adapters/TruSeq3-PE.fa:2:30:10:2:True LEADING:3 TRAILING:3 MINLEN:36'
        + ' 2>' + urls.url_log + '/' + sample_code + '_log' + '$log'
    )
    # 로그에 트리모메틱이라는 명칭 넣어주면 좋을 것 같다.
    