dna_seq=input("Enter your DNA sequence")
lengthseq= len(dna_seq)
ATcontent= ((dna_seq.count("A") + dna_seq.count("T"))/lengthseq)*100
print(" The DNA sequence is: " + dna_seq + " and AT content is: " + str(ATcontent) + "%")