import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import urls
import func

def trimmomatic(species_name, species_code):
    
    func.trimming('SRR14267546')
