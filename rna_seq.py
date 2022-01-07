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

print("INPUT SPECIES Scientific_Name : " + species_SN)
print("INPUT SPECIES Ensembl_Assembly : " + species_EA)

# primary -> toplevel

### REFERENCE GENOME FILE or ZIP FILE
file_rg = urls.url_species + species_SN + '/' + species_SN + '.' + species_EA + urls.Extension_FASTA
file_rg_zip = urls.url_species + species_SN + '/' + species_SN + '.' + species_EA + urls.Extension_FASTA_zip
if os.path.isfile(file_rg) or os.path.isfile(file_rg_zip):
    if not os.path.isfile(file_rg): # Decompress fasta.gz
        os.system('unpigz ' + file_rg_zip)
else:
    # Download fasta.gz
    print("##### DOWNLOAD REFERENCE GENOME")
    print("DOWNLOAD URL : " + urls.url_ensembl + 'fasta/' + species_SN.lower() + '/dna/' + species_SN + '.' + species_EA + urls.Extension_FASTA_zip)
    os.system(
        'wget'
        + ' ' +
        '-P ' + urls.url_species + species_SN + '/'
        + ' ' + 
        + urls.url_ensembl + 'fasta/' + species_SN.lower() + '/dna/' + species_SN + '.' + species_EA + urls.Extension_FASTA_zip
    )
    # Decompress fasta.gz
    os.system('unpigz ' + file_rg_zip)

### GENE ANNOTATION FILE or ZIP FILE
file_ga = urls.url_species + species_SN + '/' + species_SN + '.' + species_EA + urls.Extension_GTF
file_ga_zip = urls.url_species + species_SN + '/' + species_SN + '.' + species_EA + urls.Extension_GTF_zip
if os.path.isfile(file_ga) or os.path.isfile(file_ga_zip):
    if not os.path.isfile(file_ga):
        os.system('unpigz ' + file_ga_zip)
else:
    # Download gtf.gz
    print("##### DOWNLOAD GENE ANNOTATION")
    print("DOWNLOAD URL : " + urls.url_ensembl + 'gtf/' + species_SN.lower() + '/' + species_SN + '.' + species_EA + urls.Extension_GTF_zip)
    os.system(
        'wget'
        + ' ' +
        '-P ' + urls.url_species + species_SN + '/'
        + ' ' + 
        + urls.url_ensembl + 'gtf/' + species_SN.lower() + '/' + species_SN + '.' + species_EA + urls.Extension_GTF_zip
    )

# 01.Trimming

# 02.Hisat2

# 03.FeatureCount