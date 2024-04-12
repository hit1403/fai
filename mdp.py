
states = ["PU", "PF", "RU","RF"]

# Define transition probabilities
transition_probs = {
    "PU": {"A":{"PU": 0.5, "PF": 0.5, "RU": 0,"RF":0},"S":{"PU": 1, "PF": 0, "RU": 0,"RF":0}},
    "PF": {"A":{"PU": 0, "PF": 1, "RU": 0,"RF":0},"S":{"PU": 0.5, "PF": 0, "RU": 0,"RF":0.5}},
    "RU": {"A":{"PU": 0.5, "PF": 0.5, "RU": 0,"RF":0},"S":{"PU": 0.5, "PF": 0, "RU": 0.5,"RF":0}},
    "RF": {"A":{"PU": 0, "PF": 1, "RU": 0,"RF":0},"S":{"PU": 0, "PF": 0, "RU": 0.5,"RF":0.5}}
}

# Define rewards
rewards = {
    "PU": 0,
    "PF": 0,
    "RU": 10,
    "RF": 10
}

# Discount factor
gamma = 0.9
clist = [[0,0,10,10]]
cdict = {
    "PU": 0,
    "PF": 0,
    "RU": 10,
    "RF": 10
}
diff = 1
while diff>0.03:
    pu = 0 + gamma*max((transition_probs['PU']['A']['PU']*cdict['PU'] + transition_probs['PU']['A']['PF']*cdict['PF']),transition_probs['PU']['S']['PU']*cdict['PU'])
    pf = 0 + gamma*max((transition_probs['PF']['A']['PF']*cdict['PF']),(transition_probs['PF']['S']['PU']*cdict['PU'] + transition_probs['PF']['S']['RF']*cdict['RF']))
    ru = 10 + gamma*max((transition_probs['RU']['A']['PU']*cdict['PU'] + transition_probs['RU']['A']['PF']*cdict['PF']),(transition_probs['RU']['S']['PU']*cdict['PU'] + transition_probs['RU']['S']['RU']*cdict['RU']))
    rf = 10 + gamma*max((transition_probs['RF']['A']['PF']*cdict['PF']),(transition_probs['RF']['S']['RU']*cdict['RU'] + transition_probs['RF']['S']['RF']*cdict['RF']))
    clist.append([pu,pf,ru,rf])
    diff = abs(cdict['PU'] - pu)+abs(cdict['PF'] - pf)+abs(cdict['RU'] - ru)+abs(cdict['RF'] - rf)
    cdict['PU'] = pu
    cdict['PF'] = pf
    cdict['RU'] = ru
    cdict['RF'] = rf

for i in clist:
    print(i)
print(cdict)
