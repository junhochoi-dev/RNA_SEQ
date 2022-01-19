import sys, os
import urls

def quantification(species_name, species_code, sample_code, thread_value):
    print("##### START QUANTIFICATION :: " + sample_code)
    os.system(
        '/program/subread/bin/featureCounts'
        + ' ' +
        '-T'
        + ' ' +
        thread_value
        + ' ' +
        '-p -s 0 -t exon -g gene_id -a' # -p paired end, -a annotation
        + ' ' + 
        urls.url_species + species_name + '/' + species_name + '.' + species_code +urls.Extension_GTF
        + ' ' +
        '-o' # -o output
        + ' ' +
        urls.url_samples + sample_code + '/' + sample_code + '_result.txt'
        + ' ' +
        urls.url_samples + sample_code + '/' + sample_code + '_sorted.bam'
    )
    print("##### END QUANTIFICATION :: " + sample_code)


    #    + ' 2>' + urls.url_log + '/' + sample_code + '/' + sample_code + '_FeatureCount_log' + '$log'