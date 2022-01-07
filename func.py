import os
import pandas as pd

def download_sra():
    # input SRA CODE
    code = 'SRR12937416'
    # 셀 실행
    os.system(
        'sh download_via_parallel.sh'
        + ' ' +
        code # 이게 될까라는 게 의문이다..
        
    )


def make_species_dir():
    species_data = pd.read_csv("/disk4/bicjh/rna_seq/species.csv")

    # os.system('pwd')
    # os.system('cd /disk4/bicjh/rna_seq/')
    for idx in range(species_data.shape[0]):
        os.system('mkdir /disk4/bicjh/rna_seq/00_data/data__species/' + species_data.Scientific_name[idx])
