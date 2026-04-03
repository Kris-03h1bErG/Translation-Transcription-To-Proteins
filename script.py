# to convert DNA to Protein Strains 
# Note to self try to optimize code as much as possible 

def getDnaStrand():
    return input("Please enter DNA with spaces seperating each Codon: ")

def getDnaAndConvertToRNA():
    dna_strand = getDnaStrand()
    codon_strand = dna_strand.split(" ")
    #print(codon_strand)
    pair_for_nucleotide = {"T" : "A", "A" : "U", "U" : "C", "C" : "G", "G" : "C"}
    #print(codon_strand)
    new_Codon_Strand = []
    for codon in codon_strand:
        new_Codon = []
        for nucleotide in codon:
            nucleotide = pair_for_nucleotide[nucleotide]
            new_Codon.append(nucleotide)
        new_Codon_Strand.append(new_Codon)
    #print(new_Codon_Strand)
    return new_Codon_Strand
getDnaAndConvertToRNA()
def convertRNAToProtein(rna_Codon_strand):
    for codon in rna_Codon_strand:
        for nucleotide in codon:
            # Logic here is to check the least amount of datta possible 4-2-3-1
            # 4's only need to check first 2 in Codon 2's need all 3 but is still 1 check but have to check 3 letters than 1 or 2
            # 3's and 1's are shown 1 and 3 times with 3 preffered as it has a greater chance and less data than 1's 
            protein_synthisis = {
                "CU" : "Leu",
                "GU" : "Val",
                "UC" : "Ser",
                "CC" : "Pro",
                "AC" : "Thr",
                "GC" : "Ala",
                "CG" : "Arg",
                "GG" : "Gly",
                "2" : 
                {                  #Looking for last letter 
                    "UU" : dict.fromkeys(["U", "C"], "Phe"),              
                }
            

            }