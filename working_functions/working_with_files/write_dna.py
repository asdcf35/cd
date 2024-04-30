def write_dna(filepath, dna_seq):
  # open the file with write mode
  file_to_write_to = open(filepath, 'w') 
  # convert the DNA sequence to a string
  str_dna = str(dna_seq)
  # write to the file
  file_to_write_to.write(str_dna)
  # close the file
  file_to_write_to.close()