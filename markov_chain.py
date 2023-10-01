import numpy as np

# given the transition matrix for the weather markov chain

#                Sunny   Cloudy   Rainy
# Sunny         0.7     0.2      0.1
# Cloudy        0.3     0.4      0.3
# Rainy         0.2     0.3      0.5


# transition matrix 
transition_matrix = np.array([
    [0.7, 0.2, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.3, 0.5]
])

# print(transition_matrix)

# initial state starts with sunny
current_state = 0
num_days = 7

# simulate the markov chain
weather_sequence = []
for _ in range(num_days):
    weather_sequence.append(current_state)
    current_state = np.random.choice([0, 1, 2], p = transition_matrix[current_state])


# convert state numbers to weather labels
weather_labels = ["sunny", "cloudy", "rainy"]
weather_forecast = [weather_labels[state] for state in weather_sequence]

print("7 day weather forecast")
print(weather_forecast)