
import re

genotype_list = "ase1\u0394::NatMx6 ase1D::NatMx6 leu1byr1::ura4"
expression = "D::"


for genotype in genotype_list.split():
    if re.search(expression, genotype) is not None:
    
        print("Found error in:", genotype)
        print("Suggested fix:", re.sub("D::","\u0394::",genotype))

# Output:
# Found error in: ase1D::NatMx6
# Suggested fix: ase1Δ::NatMx6
