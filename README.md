&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
     &&&&&  &&    &  &&          &&&&&  &&&&&  &&&&&
     &   &  & &   &  & &         &      &      &   &
     &&&&&  &  &  &  &&&&   &&&  &&&&&  &&&&&  & & &
     &  &   &   & &  &   &           &  &      &  &&
     &   &  &    &&  &    &      &&&&&  &&&&&  &&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# RNA - SEQ

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
01. TRIMMING

* TRIMMOMATIC
Input 	: FastQ(forward, reverse) -> SAMPLE 
output	: FastQ(forward, reverse X paired, unpaired)

&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
02. MAPPING (ALIGNMENT)
HISAT2

FASTQ -> SAM
Sequence Alignment data를 담고 있는 파일로 FASTQ 파일을 reference genome 등에 맵핑시킨 형태의 파일

HISAT2를 이용하여 reference에 대한 인덱스 생성 -> 맵핑 속도를 빠르게 하기 위해 HISAT2-build 명령어를 통해 인덱스 생성
02. INDEXING
Input 	: 
output	: 

02.  FastQ -> SAM -> HISAT2
Input 	: FastQ(forward, reverse) / Reference Genome(primary or toplevel)
output	: SAM

03. SAM -> BAM (sorted BAM) ->SAMTOOL 이용
Input 	: SAM
output	:
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
03. QUANTIFICATION
featureCounts

GEO DATASETS : https://www.ncbi.nlm.nih.gov/gds
SRA RUN SELECTOR : https://www.ncbi.nlm.nih.gov/Traces/study/

04. Quantification -> FeatureCount 이용
Input 	: BAM / Gene Annotation
output	: 
***********************************************************************
RNA_SEQ

01. Trimming (Paired End or Single End..?) -> Trimmomatic 
Input 	: FastQ(forward, reverse) -> SAMPLE 
output	: FastQ(forward, reverse X paired, unpaired)
* 필요한 것은 paired만!

01. & INDEXING
Input 	: 
output	: 

02.  FastQ -> SAM -> HISAT2
Input 	: FastQ(forward, reverse) / Reference Genome(primary or toplevel)
output	: SAM

03. SAM -> BAM (sorted BAM) ->SAMTOOL 이용
Input 	: SAM
output	:


& 각 부분 별로 log 만들기
성공 실패 여부 나누고.
time 반영하고.

마크다운 사용법 https://gist.github.com/ihoneymon/652be052a0727ad59601