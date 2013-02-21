from random import randint
from string import punctuation

# Natural Language Toolkit imports
from nltk.tag import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize

#####################################################################
# Constants
#####################################################################

angela = "Angela: "
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
  "What should I do?",
  "What do you like to do?"
]

bases_simple = [
  "Your face ", 
  "Your mum "
]

bases_wishes = [
  "Your mum wishes she ",
  "Your mum wishes her face ",
  "Your mum wishes your face "
]

bases = [simple + "is " for simple in bases_simple] + [wish + "was " for wish in bases_wishes]

#####################################################################
# Helper function definitions
#####################################################################

# Returns a random member from the given list
def random_member(from_list):
  return from_list[randint(0, len(from_list) - 1)]

# Returns all token from the given list with the given tag
def tokens_by_tag(tagged_tokens, search_tag):
  return [token for (token, tag) in tagged_tokens if tag == search_tag]

# Builds a response based on one of the official bases, 
# a word in the source list, using and given connectives to bind them
def build_repartees(bases, from_list, connectives):
  return [angela + random_member(bases) + connectives + elem + "." for elem in from_list]

# Try to build a multiple word response
def multiword_responses(tokens, from_groups, to_groups):
  helper_responses = []
  responses = []
  for verb in from_groups:
    helper_responses += [tokens[i:] if i < len(tokens) else None for i in range(len(tokens)) if tokens[i] == verb]
  # up to noun/punctuation/... or the end
  for r in helper_responses:
    r = [r[:(i + 1)] if i < len(r) else None for i in range(len(r)) if r[i] in to_groups]
    if r and r[0]:
      response = " ".join(r[0])
      responses.append(response)
  return responses

# Extract the part to use as the insult
# TODO Some cases don't work well (eg adverb - however, nouns - fluffy...)
def generate_all_possible_repartees(tokens, groups): 
  to_groups = groups["punctuation"] + groups["nouns"] + groups["nouns_plural"] + groups["nouns_proper"] + groups["nouns_proper_plural"]
  mw_responses_non_3rd = multiword_responses(tokens, groups["verbs"] + groups["verbs_non_3rd"], to_groups)
  mw_responses_3rd = multiword_responses(tokens, groups["verbs_3rd"], to_groups)

  repartees = []
  repartees += build_repartees(bases_simple, groups["verbs_3rd"] + mw_responses_3rd, "")
  repartees += build_repartees(bases_wishes, groups["verbs"] + groups["verbs_non_3rd"] + mw_responses_non_3rd, random_member(modal_past))
  repartees += build_repartees(bases_wishes, groups["verbs_past"], "")
  repartees += build_repartees(bases_wishes, groups["verbs_past_participle"], random_member(modal_past) + "have ")
  repartees += build_repartees(bases_wishes, groups["nouns_plural"] + groups["nouns_proper_plural"], "had ")
  repartees += build_repartees(bases, groups["adjectives"] + groups["adjectives_comparative"] + groups["nouns_proper"], "")
  repartees += build_repartees(bases, groups["adjectives_superlative"] + groups["adverbs_superlative"] + groups["nouns"], "the ")
  repartees += build_repartees(bases, groups["adverbs"] + groups["adverbs_comparative"], "doing ")
  if repartees:
    return repartees
  return [angela + fail + "\n" + broken]
  #return [angela + random_member(bases) + response + "."] 

# Explanation: http://www.monlp.com/2011/11/08/part-of-speech-tags/
def group_by_tag(tagged):
  pos_punctuation = []
  for punct in punctuation:
    pos_punctuation += tokens_by_tag(tagged, punct)
  return {
    "adjectives"             : tokens_by_tag(tagged, "JJ"),
    "adjectives_comparative" : tokens_by_tag(tagged, "JJR"),
    "adjectives_superlative" : tokens_by_tag(tagged, "JJS"),
    "adverbs"                : tokens_by_tag(tagged, "RB"),
    "adverbs_comparative"    : tokens_by_tag(tagged, "RBR"),
    "adverbs_superlative"    : tokens_by_tag(tagged, "RBS"),
    "nouns"                  : tokens_by_tag(tagged, "NN"),
    "nouns_plural"           : tokens_by_tag(tagged, "NNS"),
    "nouns_proper"           : tokens_by_tag(tagged, "NNP"),
    "nouns_proper_plural"    : tokens_by_tag(tagged, "NNPS"),
    "verbs"                  : tokens_by_tag(tagged, "VB"),
    "verbs_past"             : tokens_by_tag(tagged, "VBD"),
    "verbs_3rd"              : tokens_by_tag(tagged, "VBZ"),
    "verbs_non_3rd"          : tokens_by_tag(tagged, "VBP"),
    "verbs_past_participle"  : tokens_by_tag(tagged, "VBN"),
    "verbs_gerund"           : tokens_by_tag(tagged, "VBG"),
    "pronouns_personal"      : tokens_by_tag(tagged, "PRP"),
    "punctuation"            : pos_punctuation
  }

#####################################################################
# Interactive part of the program
#####################################################################

if __name__=="__main__":
  # Start talking to Angela
  question = random_member(questions)
  print angela + question 
  response = raw_input("You: ")

  # Extract sentence parts (nouns, adjectives, maybe later verbs)
  #response = "".join([char for char in response if char not in punctuation])
  tokens = [word_tokenize(sentence) for sentence in sent_tokenize(response)]
  # Flatten the list of lists
  tokens = [elem for sublist in tokens for elem in sublist]
  tagged = pos_tag(tokens) # this causes the lag - but I doubt I can fix it
  groups = group_by_tag(tagged)

  # Select an insult as a response
  if ("Ruth" in question):
    print angela + "Yeah, I agree."
  else:
    print random_member(generate_all_possible_repartees(tokens, groups))
