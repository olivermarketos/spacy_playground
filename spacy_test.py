import spacy
import re
from spacy.matcher import Matcher

# Load a pipeline and create the nlp object
nlp = spacy.load("en_core_web_sm")

# Initialize the matcher with the shared vocab
#matcher = Matcher(nlp.vocab)

# Add the pattern to the matcher
#pattern = [{"TEXT": {"REGEX": }}] # PATTERN
#matcher.add("GENOTYPE_PATTERN", [pattern])

doc = nlp("ase1\u0394::NatMx6 ase1D::NatMx6 leu1byr1::ura4")


# Call the matcher on the doc
#matches = matcher(doc)

#expression = r"D::" 
expression = r"NatMx6" 

for match in re.finditer(expression,  doc.text):
    start, end = match.span()
    span = doc.char_span(start, end)
    
    print("Found error: ", span.text)

'''

nlp = spacy.load("en_core_web_sm")
doc = nlp("ase1\u0394::NatMx6 ase1D::NatMx6")

expression = r"[Uu](nited|\.?) ?[Ss](tates|\.?)"
for match in re.finditer(expression, doc.text):
    start, end = match.span()
    span = doc.char_span(start, end)
    # This is a Span object or None if match doesn't map to valid token sequence
    if span is not None:
        print("Found match:", span.text)

import re
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("A complex-example,!")
print([token.text for token in doc])
print(doc[0])

s = 'ase1\u0394::NatMx6 ase1D::NatMx6'

print(re.sub('D::', '\u0394::', s))

'''
