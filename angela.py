# Missing Angela? Want to talk to her? Then this script is for you.
# Author:  Andreja Kogovsek

import random
import nltk

angela = "Angela: "

questions = [
  "What do you think of Ruth?",
  "How was your day?"
]

insults = [
  "Your face is ", 
  "Your mum is ", 
  "Your mum wishes she was ",
  "Your mum wishes her face was ",
  "Your mum wishes your face was "
]

# Start talking to Angela
q = random.randint(0, len(questions) - 1)
print(angela + questions[q])
response = raw_input("You: ")

# Extract sentence parts (nouns, adjectives, maybe later verbs)

# adjective:          X -> X (negative positive ones later?)
# nouns:              X -> a/an? X
# nouns to adjective: X -> (more) like a X

tokens = nltk.word_tokenize(response)
print tokens
tagged = nltk.pos_tag(tokens)
print tagged

# Adjective: JJ, JJR (comparative), JJS (superlative)
# Adverb:    RB, RBR (comparative), RBS (suplerative)
# Noun:      NN, NNS (plural), NNP (proper), NNPS (proper plural)
# Verbs:     VB (base), VBD (past), VBZ (3rd person singular present) ...

def tokens_by_tag(tagged_tokens, search_tag):
  return [token for (token, tag) in tagged_tokens if tag == search_tag]

adjectives             = tokens_by_tag(tagged, "JJ")
adjectives_comparative = tokens_by_tag(tagged, "JJR")
adverbs_superlative    = tokens_by_tag(tagged, "RBS")
adverbs                = tokens_by_tag(tagged, "RB")
adverbs_comparative    = tokens_by_tag(tagged, "RBR")
adverbs_superlative    = tokens_by_tag(tagged, "RBS")
nouns                  = tokens_by_tag(tagged, "NN")
nouns_plural           = tokens_by_tag(tagged, "NNS")
verbs                  = tokens_by_tag(tagged, "VB")
verbs_past             = tokens_by_tag(tagged, "VBD")
verbs_3rd              = tokens_by_tag(tagged, "VBZ")

# Extract the part to use as the insult
if (q == 0):
  print(angela + "Yeah, I agree.")
else:
  print(angela + insults[random.randint(0, len(insults) - 1)] + response + ".")
