import sys, os
import pandas as pd
import urls
import func__main
import func_Trimmomatic
import func_HISAT
import func_FeatureCount

# import urllib3.request

species_data = pd.read_csv("/disk4/bicjh/rna_seq/species.csv")

print("################################")
print("##                            ##")
print("## RNA SEQ _ AUTO PROGRAMMING ##")
print("##                            ##")
print("################################")

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

### thread 값입력
while True:
    thread_value = int(input("Input thread value to use(0 ~ 30) : "))
    if thread_value > 0 and thread_value <= 30:
        thread_value = str(thread_value)
        break

sample_code = input("Input your sequencing sample code : ")
# 샘플 있는지 없는 지 확인 그리고 폴더생성...
func__main.download_sample(sample_code)

# 01.Trimming
func_Trimmomatic.trimming(sample_code, thread_value)

# 02.Hisat2
func_HISAT.indexing(species_name, species_code, thread_value)
func_HISAT.mapping(species_name, species_code, sample_code, thread_value)
func_HISAT.sambam(sample_code, thread_value)
func_HISAT.sorted_bam(sample_code, thread_value)

# 03.FeatureCount
func_FeatureCount.quantification(species_name, species_code, sample_code, thread_value)


# DEVELOP NOTE
### 전체 과정 들어가기전에 샘플 다운로드
# 모든 프로그램에서 변환이나 다운로드 전 파일 유무 확인!
# 영문 전환
# 파일이 있을 시 이미 존재한다는 alert
# SE PL 구분
# 실행중단되었을 시 Error try 처리
# thread value string으로 안받을 시 에러 생긴다. -> to string으로 수정하자 -> int로 하지말자

# 샘플 별 말고 따로 Trimmomatic Hisat 등등등 끼리...

## 터미널 모든 기록 log로 남기는것
# https://medium.com/@jinnyjinnyjinjin/nohup-%EB%AA%85%EB%A0%B9%EC%96%B4%EB%A1%9C-%EC%96%B4%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EC%8B%A4%ED%96%89%ED%95%98%EA%B8%B0-d66cc85d4f9