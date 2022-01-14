import os
import pandas as pd
import urls

def download_sample(sample_code):
    print("##### START DOWNLOAD SAMPLE :: " + sample_code)
    ### 파일 존재여부
    os.system('mkdir ' + urls.url_samples + sample_code)
    os.system('sh download_via_parallel.sh ' + sample_code + ' ./data/data__samples/')
    print("##### END DOWNLOAD SAMPLE" + sample_code)

def make_species_dir():
    species_data = pd.read_csv("/disk4/bicjh/rna_seq/species.csv")
    # os.system('pwd')
    # os.system('cd /disk4/bicjh/rna_seq/')
    for idx in range(species_data.shape[0]):
        os.system('mkdir ' + urls.url_species + species_data.Scientific_name[idx])
