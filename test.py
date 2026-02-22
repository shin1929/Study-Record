from Bio import Entrez, SeqIO
Entrez.email = "ssh031103@naver.com"

# 1. esearch: Entrez.read() 사용
with Entrez.esearch(db="nucleotide", term="Zika virus[Org]", retmax=1) as handle:
    search_record = Entrez.read(handle) 
    target_id = search_record["IdList"][0]

# 2. efetch: SeqIO.read() 사용
with Entrez.efetch(db="nucleotide", id=target_id, rettype="fasta", retmode="text") as handle:
    seq_record = SeqIO.read(handle, "fasta")

# 결과 확인
print(f"ID: {seq_record.id}")
print(f"Sequence: {seq_record.seq[:50]}") # 앞 50자만 출력