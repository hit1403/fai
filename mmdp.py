# Define the states and their initial values
states = {
    "Poor & Unknown": 0,
    "Poor & Famous": 0,
    "Rich & Famous": 10,
    "Rich & Unknown": 10
}
states_intial = {
    "Poor & Unknown": 0,
    "Poor & Famous": 0,
    "Rich & Famous": 10,
    "Rich & Unknown": 10
}

# Define the transitions with probabilities
transitions = {
    "Poor & Unknown": {"Poor & Unknown": [1, 0.5], "Poor & Famous": [0, 0.5], "Rich & Famous": [0, 0], "Rich & Unknown": [0, 0]},
    "Poor & Famous": {"Poor & Unknown": [0.5, 0], "Poor & Famous": [0, 1], "Rich & Famous": [0.5, 0], "Rich & Unknown": [0, 0]},
    "Rich & Famous": {"Poor & Unknown": [0, 0], "Poor & Famous": [0, 1], "Rich & Famous": [0.5, 0], "Rich & Unknown": [0.5, 0]},
    "Rich & Unknown": {"Poor & Unknown": [0.5, 0.5], "Poor & Famous": [0, 0.5], "Rich & Famous": [0, 0], "Rich & Unknown": [0.5, 0]}
}

# Define the discount factor
discount_factor = 0.9
print("Iteration 0:")
print("PU: {:.3f}, PF: {:.3f}, RU: {:.3f}, RF: {:.3f}".format(states_intial["Poor & Unknown"], states_intial["Poor & Famous"], states_intial["Rich & Unknown"], states_intial["Rich & Famous"]))
# Iterate the process for three times
for iteration in range(3):
    print(f"Iteration {iteration + 1}:")
    for state in states:
        max_value = max(sum(transitions[state][next_state][0]* states_intial[next_state] for next_state in transitions[state]),sum(transitions[state][next_state][1]* states_intial[next_state] for next_state in transitions[state]))
        states_intial[state] =states[state]+ discount_factor*max_value
    print("PU: {:.3f}, PF: {:.3f}, RU: {:.3f}, RF: {:.3f}".format(states_intial["Poor & Unknown"], states_intial["Poor & Famous"], states_intial["Rich & Unknown"], states_intial["Rich & Famous"]))
