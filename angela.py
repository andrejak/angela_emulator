# Missing Angela? Want to talk to her? Then this script is for you.
# Author:  Andreja Kogovsek

import random

# Start talking to Angela
print("Angela: 'What's up?'")
response = raw_input("You: ")

insults = [
  "Your face is ", 
  "Your mum is ", 
  "Your mum wishes she was ",
  "Your mum wishes her face was "]

# Extract the part to use as the insult
print("Angela: " + insults[random.randint(0, 3)] + response)
