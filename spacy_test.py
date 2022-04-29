import spacy
import re
from spacy.matcher import Matcher

# Load a pipeline and create the nlp object
nlp = spacy.load("en_core_web_sm")
doc = nlp("ase1\u0394::NatMx6 ase1D::NatMx6 leu1byr1::ura4")

# Initialize the matcher with the shared vocab
matcher = Matcher(nlp.vocab)

# Add the pattern to the matcher
pattern = [{"TEXT":{"REGEX": "D::"}}]
matcher.add("GENOTYPE_PATTERN", [pattern])

# Call the matcher on the doc
matches = matcher(doc)

print("total matches found:", len(matches))

for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
    print("Suggested fix:", re.sub("D::","\u0394::",doc[start:end].text))

