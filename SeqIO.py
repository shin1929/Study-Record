from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

def analyze_sequence(record):
    print(f"--- [서열 분석 리포트: {record.id}] ---")
    print(f"1. 서열 길이: {len(record)} bp")
    print(f"2. GC 함량: {gc_fraction(record.seq) * 100:.2f}%")
    print(f"3. 앞 10개 염기: {record.seq[:10]}")
    print("-" * 30)

path="../sequence/hav.fasta"
with open(path,"r") as handle:
    record=SeqIO.read(handle, "fasta")
    analyze_sequence(record)

path="../sequence/sequences.fasta"
with open(path,"r") as handle:
    record=list(SeqIO.parse(handle,"fasta"))
    for i in range(5):
        print(f"{i}번째 바이러스 분석")
        analyze_sequence(record[i])
