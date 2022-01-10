import sys, os
import pandas as pd
import urls
from func import download_sample
sys.path.append('/disk4/bicjh/rna_seq/01_Trimmomatic/trimmomatic.py')
sys.path.append('/disk4/bicjh/rna_seq/02_HISAT/HISAT.py')
sys.path.append('/disk4/bicjh/rna_seq/03_FeatureCount/FeatureCount.py')

from . import trimmomatic
from . import HISAT
from . import FeatureCount
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
            species_name = species_input # Scientific_name
            species_code = species_data.Ensembl_Assembly[idx] # Ensembl_Assembly
            break

    if species_check:
        break
    else:
        print("The species does not exist. Please Re-input.")

print("SPECIES INPUT Scientific_Name : " + species_name)
print("SPECIES INPUT Ensembl_Assembly : " + species_code)

# primary -> toplevel

### REFERENCE GENOME FILE or ZIP FILE
file_rg = urls.url_species + species_name + '/' + species_name + '.' + species_code + urls.Extension_FASTA
file_rg_zip = urls.url_species + species_name + '/' + species_name + '.' + species_code + urls.Extension_FASTA_zip
if os.path.isfile(file_rg) or os.path.isfile(file_rg_zip):
    if not os.path.isfile(file_rg): # Decompress fasta.gz
        os.system('unpigz ' + file_rg_zip)
else:
    # Download fasta.gz
    print("##### DOWNLOAD REFERENCE GENOME")
    print("DOWNLOAD URL : " + urls.url_ensembl + 'fasta/' + species_name.lower() + '/dna/' + species_name + '.' + species_code + urls.Extension_FASTA_zip)
    os.system(
        'wget'
        + ' ' +
        '-P ' + urls.url_species + species_name + '/'
        + ' ' + 
        + urls.url_ensembl + 'fasta/' + species_name.lower() + '/dna/' + species_name + '.' + species_code + urls.Extension_FASTA_zip
    )
    # Decompress fasta.gz
    os.system('unpigz ' + file_rg_zip)

### GENE ANNOTATION FILE or ZIP FILE
file_ga = urls.url_species + species_name + '/' + species_name + '.' + species_code + urls.Extension_GTF
file_ga_zip = urls.url_species + species_name + '/' + species_name + '.' + species_code + urls.Extension_GTF_zip
if os.path.isfile(file_ga) or os.path.isfile(file_ga_zip):
    if not os.path.isfile(file_ga):
        os.system('unpigz ' + file_ga_zip)
else:
    # Download gtf.gz
    print("##### DOWNLOAD GENE ANNOTATION")
    print("DOWNLOAD URL : " + urls.url_ensembl + 'gtf/' + species_name.lower() + '/' + species_name + '.' + species_code + urls.Extension_GTF_zip)
    os.system(
        'wget'
        + ' ' +
        '-P ' + urls.url_species + species_name + '/'
        + ' ' + 
        + urls.url_ensembl + 'gtf/' + species_name.lower() + '/' + species_name + '.' + species_code + urls.Extension_GTF_zip
    )

sample_code = input("Input your sequencing sample code : ")
# 샘플 있는지 없는 지 확인 그리고 폴더생성...
download_sample(sample_code)

### 전체 과정 들어가기전에 샘플 다운로드

# 01.Trimming
trimmomatic(sample_code)

# 02.Hisat2
HISAT(species_name, species_code, sample_code)

# 03.FeatureCount
FeatureCount(species_name, species_code, sample_code)

# 모든 프로그램에서 변환이나 다운로드 전 파일 유무 확인!