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


with open('meteor.json', 'r') as f:
    text = f.read()


import json
import matplotlib.pyplot as plt
meteors = json.loads(text)
#times = json.loads(text)
import pprint

terms = ['Apollo', 'Aten', 'Amor']
term_counts = {}
for term in terms:
    term_counts[term] = 0

terms1 = ['2010', '2011', '2012', '2013', '2014', '2015']
term1_counts = {}
for term1 in terms1:
    term1_counts [term1] = 0

num_2010Ap = 0
num_2011Ap = 0
num_2012Ap = 0
num_2013Ap = 0
num_2014Ap = 0
num_2015Ap = 0

num_2010At = 0
num_2011At = 0
num_2012At = 0
num_2013At = 0
num_2014At = 0
num_2015At = 0

num_2010Am = 0
num_2011Am = 0
num_2012Am = 0
num_2013Am = 0
num_2014Am = 0
num_2015Am = 0

num_apollo = 0
num_aten = 0
num_amor = 0


#Numer of Apollo for each year
num_2010Ap = 0
for meteor in meteors:
    if '2010' in meteor['discovery_date']:
        if 'Apollo' in meteor['orbit_class']:
                num_2010Ap += 1

num_2011Ap= 0
num_2011Ap = 0
for meteor in meteors:
    if '2011' in meteor['discovery_date']:
        if 'Apollo' in meteor['orbit_class']:
                num_2011Ap += 1

num_2012Ap= 0
num_2012Ap = 0
for meteor in meteors:
    if '2012' in meteor['discovery_date']:
        if 'Apollo' in meteor['orbit_class']:
                num_2012Ap += 1

num_2013Ap= 0
num_2013Ap = 0
for meteor in meteors:
    if '2013' in meteor['discovery_date']:
        if 'Apollo' in meteor['orbit_class']:
                num_2013Ap += 1

num_2013Ap= 0
num_2013Ap = 0
for meteor in meteors:
    if '2013' in meteor['discovery_date']:
        if 'Apollo' in meteor['orbit_class']:
                num_2013Ap += 1

num_2014Ap= 0
num_2014Ap = 0
for meteor in meteors:
    if '2014' in meteor['discovery_date']:
        if 'Apollo' in meteor['orbit_class']:
                num_2014Ap += 1

num_2015Ap= 0
num_2015Ap = 0
for meteor in meteors:
    if '2015' in meteor['discovery_date']:
        if 'Apollo' in meteor['orbit_class']:
                num_2015Ap += 1

print('Apollo 2010 = ', num_2010Ap)
print('Apollo 2011 = ', num_2011Ap)
print('Apollo 2012 = ', num_2012Ap)
print('Apollo 2013 = ', num_2013Ap)
print('Apollo 2014 = ', num_2014Ap)
print('Apollo 2015 = ', num_2015Ap)

#Numer of Aten for each year
num_2010At = 0
for meteor in meteors:
    if '2010' in meteor['discovery_date']:
        if 'Aten' in meteor['orbit_class']:
                num_2010At += 1

num_2011At = 0
for meteor in meteors:
    if '2011' in meteor['discovery_date']:
        if 'Aten' in meteor['orbit_class']:
                num_2011At += 1

num_2012At = 0
for meteor in meteors:
    if '2012' in meteor['discovery_date']:
        if 'Aten' in meteor['orbit_class']:
                num_2012At += 1

num_2013At = 0
for meteor in meteors:
    if '2013' in meteor['discovery_date']:
        if 'Aten' in meteor['orbit_class']:
                num_2013At += 1

num_2013At = 0
for meteor in meteors:
    if '2013' in meteor['discovery_date']:
        if 'Aten' in meteor['orbit_class']:
                num_2013At += 1

num_2014At = 0
for meteor in meteors:
    if '2014' in meteor['discovery_date']:
        if 'Aten' in meteor['orbit_class']:
                num_2014At += 1

num_2015At = 0
for meteor in meteors:
    if '2015' in meteor['discovery_date']:
        if 'Aten' in meteor['orbit_class']:
                num_2015At += 1

print('Aten 2010 = ', num_2010At)
print('Aten 2011 = ', num_2011At)
print('Aten 2012 = ', num_2012At)
print('Aten 2013 = ', num_2013At)
print('Aten 2014 = ', num_2014At)
print('Aten 2015 = ', num_2015At)

#Numer of Amor for each year
num_2010Am = 0
for meteor in meteors:
    if '2010' in meteor['discovery_date']:
        if 'Amor' in meteor['orbit_class']:
                num_2010Am += 1

num_2011Am = 0
for meteor in meteors:
    if '2011' in meteor['discovery_date']:
        if 'Amor' in meteor['orbit_class']:
                num_2011Am += 1

num_2012Am = 0
for meteor in meteors:
    if '2012' in meteor['discovery_date']:
        if 'Amor' in meteor['orbit_class']:
                num_2012Am += 1

num_2013Am = 0
for meteor in meteors:
    if '2013' in meteor['discovery_date']:
        if 'Amor' in meteor['orbit_class']:
                num_2013Am += 1

num_2013Am = 0
for meteor in meteors:
    if '2013' in meteor['discovery_date']:
        if 'Aten' in meteor['orbit_class']:
                num_2013At += 1

num_2014Am = 0
for meteor in meteors:
    if '2014' in meteor['discovery_date']:
        if 'Amor' in meteor['orbit_class']:
                num_2014Am += 1

num_2015Am = 0
for meteor in meteors:
    if '2015' in meteor['discovery_date']:
        if 'Amor' in meteor['orbit_class']:
                num_2015Am += 1

print('Amor 2010 = ', num_2010Am)
print('Amor 2011 = ', num_2011Am)
print('Amor 2012 = ', num_2012Am)
print('Amor 2013 = ', num_2013Am)
print('Amor 2014 = ', num_2014Am)
print('Amor 2015 = ', num_2015Am)


counts = {'2010': num_2010Ap, '2011': num_aten, 'Amor': num_amor}



x= [2010, 2011, 2012, 2013, 2014, 2015]
y= [num_2010Ap, num_2011Ap, num_2012Ap, num_2013Ap, num_2014Ap, num_2015Ap]

x1= [2010, 2011, 2012, 2013, 2014, 2015]
y1= [num_2010At, num_2011At, num_2012At, num_2013At, num_2014At, num_2015At]

x2 = [2010, 2011, 2012, 2013, 2014, 2015]
y2= [num_2010Am, num_2011Am, num_2012Am, num_2013Am, num_2014Am, num_2015Am]

plt.plot(x, y, label= 'Apollo')
plt.plot(x1, y1, label= 'Aten')
plt. plot(x2, y2, label = 'Amor')
plt.xlabel('Years')
plt.ylabel('Number of Meteors')
plt.legend()
plt.show()



