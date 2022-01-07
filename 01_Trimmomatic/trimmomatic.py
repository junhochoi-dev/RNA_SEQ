import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import urls
import func

def trimmomatic(species_name, species_code):
    # REFERENCE GENOME 데이터 검사
    if os.path.isfile(urls.url_data + '/' + species_name + '.' + species_code + '.dna.toplevel.fa'):
        print('REFERENCE GENOME EXIST')
    else:
        if os.path.isfile('/disk4/bicjh/rna_seq/00_data/data__species/'+ species_name + '/' + species_name + '.' + species_code + '.dna.toplevel.fa.gz'):
            # 압축해제 코드
            #.dna.toplevel.fa.gz -> .dna.toplevel.fa
            os.system('unpigz ' + '/disk4/bicjh/rna_seq/00_data/data__species/'+ species_name + '/' + species_name + '.' + species_code + '.dna.toplevel.fa.gz')
        else:
            # REFERENCE GENOME 다운로드
            print('REFERENCE GENOME 다운로드')
            print("없어")
            # os.system('wget ' + urls.url_reference_genome)
            # 종료문 추가 *****

    # GENE ANNOTATION 데이터 검사
    if os.path.isfile(urls.url_data + '/' + species_name + '.' + species_code + '.105.gtf.gz'):
        print('GENE ANNOTATION EXIST')
    else:
        # GENE ANNOTATION 다운로드
        print("GENE ANNOTATION 다운로드")
        #os.system('wget ' + urls.url_gene_annotation)
    # func.trimming('SRR14267546')

trimmomatic('Homo_sapiens', 'GRCh38')