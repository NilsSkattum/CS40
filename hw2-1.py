with open('gender.json', 'r') as g:
    text = g.read()

import json
import matplotlib.pyplot as plt
bios = json.loads(text)
import pprint

terms = ['M', 'F']
term_counts = {}
for term in terms:
    term_counts[term] = 0

num_M = 0
num_F = 0

for bio in bios:
    pprint.pprint(bio['bio']['gender'])
    if 'M' in bio['bio']['gender']:
        num_M +=1
    if 'F' in bio['bio']['gender']:
        num_F +=1

counts = {'Males': num_M, 'Females': num_F}

fig, ax = plt.subplots()
ax.set(xlabel= 'Gender of US House of Reps')
ax.set(ylabel= 'Number of each Gender')
plt.bar( counts.keys() , counts.values() )
plt.show()



