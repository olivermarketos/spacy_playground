import spacy
import re
from spacy.matcher import Matcher

# Load a pipeline and create the nlp object
nlp = spacy.load("en_core_web_sm")
doc = nlp("ase1\u0394::NatMx6 ase1D::NatMx6 test0::test0 test1::Dtest1 test2D::test2 test3Dtest3")

# Initialize the matcher with the shared vocab
matcher = Matcher(nlp.vocab)

# Add the pattern to the matcher
pattern = [{"TEXT":{"REGEX": "D::"}}]   # can overload this with all the rules we're looking for
matcher.add("GENOTYPE_PATTERN", [pattern])

# Call the matcher on the doc
matches = matcher(doc) # an object containing all the tokens in the string that match our patter

print("total matches found:", len(matches))

for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
    print("Suggested fix:", re.sub("D::","\u0394::",doc[start:end].text))

# output:
#   total matches found: 2

#   Match found: ase1D::NatMx6
#   Suggested fix: ase1Δ::NatMx6

#   Match found: test2D::test2
#   Suggested fix: test2Δ::test2

