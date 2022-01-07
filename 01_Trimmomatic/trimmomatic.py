import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import urls
import func

def trimmomatic(sample_code):
    func.trimming(sample_code)
