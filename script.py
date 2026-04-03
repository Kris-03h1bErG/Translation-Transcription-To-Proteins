# to convert DNA to Protein Strains 
# Note to self try to optimize code as much as possible 

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
    {                  #Looking for last letter just a shorter way to make 2 keys asoiated to one value
        "UU" : 
        {
            "U" : "Phe",
            "C" : "Phe",
            "A" : "Leu",
            "G" : "Leu"
        },         
        "UA" : 
        {
            "U" : "Tyr",
            "C" : "Tyr",
            "A" : "Stop",
            "G" : "Stop"
        },  
        "CA" : 
        {
            "U" : "His",
            "C" : "His",
            "A" : "Gln",
            "G" : "Gln"
        },  
        "AA" : 
        {
            "U" : "Asn",
            "C" : "Asn",
            "A" : "Lys",
            "G" : "Lys"
        },  
        "GA" : 
        {
            "U" : "Asp",
            "C" : "Asp",
            "A" : "Glu",
            "G" : "Glu"
        },  
        "UG" : 
        {
            "U" : "Cys",
            "C" : "Cys",
            "A" : "Stop",
            "G" : "Trp"
        },  
        "AG" : 
        {
            "U" : "Ser",
            "C" : "Ser",
            "A" : "Arg",
            "G" : "Arg"
        },  
        "AU" : 
        {
            "U" : "Ile",
            "C" : "Ile",
            "A" : "Ile",
            "G" : "Met"
        },  
    }
}

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
#getDnaAndConvertToRNA()
def convertRNAToProteinStrand(rna_Codon_strand):
    polypeptide_strand = []
    for codon in rna_Codon_strand:
        if len(codon) == 3:
                first_two = codon[0] + codon[1]
                resulting_protein = protein_synthisis.get(first_two)
                if resulting_protein != None:
                    polypeptide_strand.append(resulting_protein)
                else:
                    last_one = codon[2] 
                    try:
                        protein = protein_synthisis["2"][first_two].get(last_one)
                        polypeptide_strand.append(protein)
                    except:
                        protein = "Error"
                        polypeptide_strand.append(protein)
        else:
            protein = "Error"
            polypeptide_strand.append(protein)
            
        
    return polypeptide_strand
print(convertRNAToProteinStrand(getDnaAndConvertToRNA()))