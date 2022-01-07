import sys, os
import pandas as pd
import urls
sys.path.append('/disk4/bicjh/rna_seq/01_Trimmomatic/trimmomatic.py')
sys.path.append('/disk4/bicjh/rna_seq/02_HISAT/HISAT.py')

from . import trimmomatic
from . import HISAT
# import urllib3.request

species_data = pd.read_csv("/disk4/bicjh/rna_seq/species.csv")

print("##############################")
print("#                            #")
print("# RNA SEQ _ AUTO PROGRAMMING #")
print("#                            #")
print("##############################")

while True:
    species_input = input("Input your sequencing sample species : ")
    species_check = False
    
    for idx in range(species_data.shape[0]):
        if species_data.Scientific_name[idx] == species_input:
            species_check = True
            species_SN = species_input # Scientific_name
            species_EA = species_data.Ensembl_Assembly[idx] # Ensembl_Assembly
            break

    if species_check:
        break
    else:
        print("The species does not exist. Please Re-input.")

print(species_SN)
print(species_EA)

# primary assembly > toplevel 

# 프라이머리 어셈블리가 있다면
# 탑레벨이있다면

# 일단 프라이머리 제외

if os.path.isfile('/disk4/bicjh/rna_seq/00_data/data__species/' + species_SN + '/' + species_SN + '.' + species_EA + urls.Extension_FASTA):
    print("파일이 이미 존재하므로 다운로드를 하지 않습니다.")

## 압축파일, 압축해제파일 둘 중에 하나만 존재해도 다운로드 취소

print("DOWNLOAD GENOME ASSEMBLY(DNA SEQUENCE) URL : ")
print(urls.url_ensembl + 'fasta/' + species_SN.lower() + '/dna/' + species_SN + '.' + species_EA + urls.Extension_FASTA)
# os.system(
#     'wget'
#     + ' ' +
#     '-P ' + '/disk4/bicjh/rna_seq/00_data/data__species/' + species_SN + '/'
#     + ' ' + 
#     + url_main + 'fasta/' + species_SN.lower() + '/dna/' + species_SN + '.' + species_EA + Extension_FASTA
# )

# 압축해제 코드 ( 대신 다 다운로드 받은 뒤. ) pigz...
os.system(
    print('압축 파일 풀기')
)

if os.path.isfile('/disk4/bicjh/rna_seq/00_data/data__species/' + species_SN + '/' + species_SN + '.' + species_EA + urls.Extension_GTF):
    print("파일이 이미 존재하므로 다운로드를 하지 않습니다.")

print("DOWNLOAD GENE ANNOTATION URL : ") # 재정리...
print(urls.url_ensembl + 'gtf/' + species_SN.lower() + '/' + species_SN + '.' + species_EA + urls.Extension_GTF)
# os.system(
#     'wget'
#     + ' ' +
#     '-P ' + '/disk4/bicjh/rna_seq/00_data/data__species/' + species_SN + '/'
#     + ' ' + 
#     + url_main + 'gtf/' + species_SN.lower() + '/' + species_SN + '.' + species_EA + Extension_GTF
# )

# 01.Trimming

# 02.Hisat2

# 03.FeatureCount