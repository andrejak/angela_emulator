# Missing Angela? Want to talk to her? Then this script is for you.
# Author:  Andreja Kogovsek

import random

angela = "Angela: "

questions = [
  "How was your day?"
]

insults = [
  "Your face is ", 
  "Your mum is ", 
  "Your mum wishes she was ",
  "Your mum wishes her face was "
]

index = random.randint(0, len(questions) - 1)

# Start talking to Angela
print(angela + questions[index])
response = raw_input("You: ")

# Extract sentence parts (nouns, adjectives, maybe later verbs)

# adjective:          X -> X
# nouns:              X -> a/an? X
# nouns to adjective: X -> (more) like a X

# Extract the part to use as the insult
print(angela + insults[random.randint(0, len(insults) - 1)] + response)
