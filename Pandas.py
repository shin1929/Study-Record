from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import pandas as pd

def calculate_gc_content(sequence):
    if not sequence:
        return 0.0
    total_length = len(sequence)
    gc_count = sequence.count('G') + sequence.count('C')
    gc_content = (gc_count / total_length) * 100
    return gc_content

def analyze_sequence(record):
    print(f"--- [서열 분석 리포트: {record.id}] ---")
    print(f"1. 서열 길이: {len(record)} bp")
    print(f"2. GC 함량: {calculate_gc_content(record.seq):.2f}%")
    print(f"3. 앞 10개 염기: {record.seq[:10]}")
    print("-" * 30)

data=[]
path="../sequence/sequences.fasta"
with open(path,"r") as handle:
    record=list(SeqIO.parse(handle,"fasta"))
    for i in range(5):
        data.append({
            "ID": record[i].id,
            "Length": len(record[i]),
            "GC_Content": calculate_gc_content(record[i].seq)
        })
df = pd.DataFrame(data)
long_df=df[df["Length"] > 11600]
sorted_df=df.sort_values(by="GC_Content", ascending=False)
df.describe()

print(df)
print(long_df)
print(sorted_df)