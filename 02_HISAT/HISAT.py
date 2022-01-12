import func

def HISAT(species_name, species_code, sample_code, thread_value):
    func.indexing(species_name, species_code, thread_value)
    func.mapping(species_name, species_code, sample_code, thread_value)
    func.sambam(sample_code, thread_value)
    func.sorted_bam(sample_code, thread_value)
