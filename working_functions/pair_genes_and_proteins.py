

def pair_genes_and_proteins(dna_string):
  from Bio.Seq import Seq
  mydna = Seq("atgggtgatgttgatgaatttcgttgttttgttggttctttat")
  myrna = mydna.transcribe()
  myamino_acid_seq = myrna.translate()
  split_seq = Seq(myamino_acid_seq).split("*")
  print(myamino_acid_seq)
  print(split_seq)
  pass