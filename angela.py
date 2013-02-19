# Missing Angela? Want to talk to her? Then this script is for you.
# Author:  Andreja Kogovsek

from random import randint
from string import punctuation
# Natural language toolkit
from nltk.tag import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize

# Constants

angela = "Angela: "
was    = "was "
have   = "have "
had    = "had "
doing  = "doing "
the    = "the "
fail   = "Your mum's face wishes her face's mum was... I mean... Wait..."
broken = "Well done. You broke Angela. I hope you're happy now."

modal_past = [
  "could ", 
  "would "
]

questions = [
  "What do you think about Ruth?",
  "How was your day?",
  "How are you doing?",
  "What have you been up to?",
  "What do you think about me?",
  "Where's Rebecca?",
  "When was the last time you saw Dave?",
  "What's the best thing about cats?",
  "Do you know what Andreja's plotting now?",
  "How do you feel about glitter?" ,
  "Ponies?",
  "What should I do?"
]

bases_wishes = [
  "Your mum wishes she ",
  "Your mum wishes her face ",
  "Your mum wishes your face "
]

bases = [
  "Your face is ", 
  "Your mum is "
] + [wish + was for wish in bases_wishes]

# Helper function definitions

def random_member(from_list):
  return from_list[randint(0, len(from_list) - 1)]

def tokens_by_tag(tagged_tokens, search_tag):
  return [token for (token, tag) in tagged_tokens if tag == search_tag]

def build_repartees(bases, from_list, additions):
  return [angela + random_member(bases) + additions + elem + "." for elem in from_list]

# Start talking to Angela
question = random_member(questions)
print angela + question 
response = raw_input("You: ")

# Extract sentence parts (nouns, adjectives, maybe later verbs)
response = "".join([char for char in response if char not in punctuation])
tokens = [word_tokenize(sentence) for sentence in sent_tokenize(response)]
# Flatten the list of lists
tokens = [elem for sublist in tokens for elem in sublist]
tagged = pos_tag(tokens) # this causes the lag

# http://www.monlp.com/2011/11/08/part-of-speech-tags/
# Adjective: JJ, JJR (comparative), JJS (superlative)
# Adverb:    RB, RBR (comparative), RBS (superlative)
# Noun:      NN, NNS (plural), NNP (proper), NNPS (proper plural)
# Verbs:     VB (base), VBD (past), VBZ (3rd person singular present) ...
adjectives             = tokens_by_tag(tagged, "JJ")
adjectives_comparative = tokens_by_tag(tagged, "JJR")
adjectives_superlative = tokens_by_tag(tagged, "JJS")
adverbs                = tokens_by_tag(tagged, "RB")
adverbs_comparative    = tokens_by_tag(tagged, "RBR")
adverbs_superlative    = tokens_by_tag(tagged, "RBS")
nouns                  = tokens_by_tag(tagged, "NN")
nouns_plural           = tokens_by_tag(tagged, "NNS")
nouns_proper           = tokens_by_tag(tagged, "NNP")
nouns_proper_plural    = tokens_by_tag(tagged, "NNPS")
verbs                  = tokens_by_tag(tagged, "VB")
verbs_past             = tokens_by_tag(tagged, "VBD")
verbs_3rd              = tokens_by_tag(tagged, "VBZ")
verbs_non_3rd          = tokens_by_tag(tagged, "VBP")
verbs_past_participle  = tokens_by_tag(tagged, "VBN")
#print tagged # DEBUG

# Extract the part to use as the insult
# Some cases don't work well (eg adverb - however, nouns - fluffy...)
def generate_all_possible_repartees():
  repartees = []
  repartees += build_repartees(bases, adjectives + adjectives_comparative + nouns_proper, "")
  repartees += build_repartees(bases, adjectives_superlative + adverbs_superlative + nouns, the)
  repartees += build_repartees(bases, adverbs + adverbs_comparative, doing)
  repartees += build_repartees(bases_wishes, verbs + verbs_non_3rd, random_member(modal_past))
  repartees += build_repartees(bases_wishes, verbs_past, "")
  repartees += build_repartees(bases_wishes, verbs_past_participle, random_member(modal_past) + have)
  repartees += build_repartees(bases_wishes, nouns_plural + nouns_proper_plural, had)
  if repartees:
    return repartees
  return [angela + fail + "\n" + broken]
  #return [angela + random_member(bases) + response + "."]

# Select an insult as a response
if ("Ruth" in question):
  print angela + "Yeah, I agree."
else:
  print random_member(generate_all_possible_repartees())
