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
        urls.url_ensembl + 'fasta/' + species_name.lower() + '/dna/' + species_name + '.' + species_code + urls.Extension_FASTA_zip
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
        urls.url_ensembl + 'gtf/' + species_name.lower() + '/' + species_name + '.' + species_code + urls.Extension_GTF_zip
    )

### thread ?????????
while True:
    thread_value = int(input("Input thread value to use(0 ~ 30) : "))
    if thread_value > 0 and thread_value <= 30:
        thread_value = str(thread_value)
        break

sample_code = input("Input your sequencing sample code : ")
# ?????? ????????? ?????? ??? ?????? ????????? ????????????...
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
### ?????? ?????? ?????????????????? ?????? ????????????
# ?????? ?????????????????? ???????????? ???????????? ??? ?????? ?????? ??????!
# ?????? ??????
# ????????? ?????? ??? ?????? ??????????????? alert -> indexing ?????? ????????? ????????????.
# SE PL ??????
# ????????????????????? ??? Error try ??????

## ????????? ?????? ?????? log??? ????????????
# https://medium.com/@jinnyjinnyjinjin/nohup-%EB%AA%85%EB%A0%B9%EC%96%B4%EB%A1%9C-%EC%96%B4%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EC%8B%A4%ED%96%89%ED%95%98%EA%B8%B0-d66cc85d4f9

# ???????????? ????????? ???, ?????????????????? ??????.
