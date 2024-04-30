
def read_dna(filepath):
  # read file
  file = open(filepath)
  dna_input = file.read()
  print(dna_input)
  # close file
  file.close()

  return dna_input