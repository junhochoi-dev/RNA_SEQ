import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import urls
import func

# PAIRED END만 돌아가도록 설정.
# SINGLE END 설정 따로 해주자.
def trimmomatic(sample_code):
    func.trimming(sample_code)
