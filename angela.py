# Missing Angela? Want to talk to her? Then this script is for you.
# Author:  Andreja Kogovsek

import random

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

# Extract the part to use as the insult
if (q == 0):
  print(angela + "Yeah, I agree.")
else:
  print(angela + insults[random.randint(0, len(insults) - 1)] + response + ".")
