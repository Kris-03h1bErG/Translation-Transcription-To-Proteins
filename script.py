# to convert DNA to Protein Strains 
# Note to self try to optimize code as much as possible 
import math

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
            "A" : "Stp",
            "G" : "Stp"
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
            "A" : "Stp",
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

def convertDNAToRNA(dna_strand):
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
#convertDNAToRNA()
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

def getMutatedDnaStrandAndCompare(dna_strand, rna_strand, polypeptide_strand):
    mutated_dna_strand = input("Please enter DNA with spaces seperating each Codon: ")
    mutated_dna_strand = mutated_dna_strand.upper()
    mutated_rna_strand = convertDNAToRNA(mutated_dna_strand)
    mutated_polypeptide_strand = convertRNAToProteinStrand(mutated_rna_strand)
    if dna_strand == mutated_dna_strand:
        print("DNA strands are the same! ")
        exit 
    elif dna_strand == '' or mutated_dna_strand == '':
        print("Either DNA strand or Mutated DNA is not entered!")
        exit
    else:
        codon_changed_list = []
        codon_changed = 1
        for current_codon in range(0 , len(rna_strand)):
            if rna_strand[current_codon] != mutated_rna_strand[current_codon]:
                codon_changed_list.append(codon_changed)
                codon_changed += 1 
                if polypeptide_strand == mutated_polypeptide_strand:
                    hidden_mutation = True
                else:
                    hidden_mutation = False
            else:
                codon_changed += 1
    return mutated_dna_strand , mutated_rna_strand , mutated_polypeptide_strand , codon_changed_list , hidden_mutation

                
def getDNAToCovertToProteinStrand():
    dna_strand = getDnaStrand()
    dna_strand = dna_strand.upper()
    rna_strand = convertDNAToRNA(dna_strand)
    polypeptide_strand = convertRNAToProteinStrand(rna_strand)

    printable_rna_strand = ""
    for rna_codon in rna_strand:
        printable_rna_strand += " "
        for nucleotide in rna_codon:
            printable_rna_strand += nucleotide        
    
    printable_polypeptide_strand = ""
    for peptide in polypeptide_strand:
        printable_polypeptide_strand += peptide + " "
    
    choice = input("Check Strand against its mutated version? Y/N: ")
    if "Y" in choice.upper():
        mutated_dna_strand , mutated_rna_strand , mutated_polypeptide_strand , changed_list , hidden_mutation = getMutatedDnaStrandAndCompare(dna_strand, rna_strand, polypeptide_strand)
        printable_mutated_rna_strand = ""
        for rna_codon in mutated_rna_strand:
            printable_mutated_rna_strand += " "
            for nucleotide in rna_codon:
                printable_mutated_rna_strand += nucleotide   

        printable_mutated_polypeptide_strand = ""
        for peptide in mutated_polypeptide_strand:
            printable_mutated_polypeptide_strand += peptide + " "     
    print(f" DNA Strand:      {dna_strand}")
    print(f" RNA Strand:     {str(printable_rna_strand)}")
    print(f" Protein Strand:  {str(printable_polypeptide_strand)}\n")
    #start = 1
    change = "" 
    for start in range(1 , len(polypeptide_strand) + 1):
        # distance = abs(start - changes)
        # change += "    " * distance 
        if start in changed_list:
            change += "^^^ "
        else:
            change += "    "
        start += 1

    print(f" DNA Strand:      {mutated_dna_strand}")
    print(f"                  {change}")
    print(f" RNA Strand:     {str(printable_mutated_rna_strand)}")
    print(f"                  {change}")
    print(f" Protein Strand:  {str(printable_mutated_polypeptide_strand)}")
    print(f"                  {change}")
#need to add another part where it checks if each codon is the same with mutated strand and if it changes the resulting protein 
getDNAToCovertToProteinStrand()