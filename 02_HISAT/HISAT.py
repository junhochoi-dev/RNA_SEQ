import func

def HISAT(species_name, species_code, sample_code):
    func.indexing(species_name, species_code)
    func.mapping(species_name, species_code, sample_code)
    func.sambam(sample_code)
    func.sorted_bam(sample_code)
