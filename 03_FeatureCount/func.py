import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import urls

def Quantification(species_name, species_code, sample_code):
    os.system(
        '/program/subread/bin/featureCounts -T 30 -p -s 0 -t exon -g gene_id -a' # -p paired end, -a annotation
        + ' ' + 
        urls.url_species + species_name + '/' + species_name + '.' + species_code +urls.Extension_GTF
        + ' ' +
        '-o' # -o output
        + ' ' +
        urls.url_samples + sample_code + '/' + sample_code + '_result.txt'
        + ' ' +
        urls.url_samples + sample_code + '/' + sample_code + '_sorted.bam'
    )