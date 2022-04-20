from numpy import mean

interval = 10
P0 = 1
y = 0.87
t = 388

new_interval, interval_found, total = 0, 0, 0

intervals, developments_in_interval, static_densities = [], [], []

developments = [58, 14, 23, 70, 297, 112, 237, 475, 279, 738, 134, 4, 120, 90, 401, 13, 405, 52, 1007, 19,
                      77, 12, 32, 259, 46, 518, 52, 0, 172, 512, 13, 1, 119, 128, 310, 131, 235, 284, 79, 16, 69,
                      18, 305, 461, 12, 93, 85, 348, 48, 146, 121, 39, 126, 415, 419, 28, 39, 516, 65, 2, 36,
                      192, 34, 21, 346, 622, 617, 59, 330, 580, 80, 6, 960, 234, 52, 438, 170, 75, 92, 340, 403,
                      177, 113, 55, 87, 51, 165, 58, 1271, 4, 51, 300, 48, 56, 112, 139, 22, 226, 127, 186]

developments_length = len(developments)

#Calculation of average developments
average_developments = mean(developments)

development_max = max(developments)

interval_length = development_max / interval

for i in range(1, interval + 1):
    intervals.append(round(i * interval_length, 1))

intervals_length = len(intervals)

developments_sorted = sorted(developments)

for i in range(0, intervals_length):
    count = 0
    for j in range(new_interval, developments_length):
        if(developments_sorted[j] <= intervals[i]):
            count += 1
    developments_in_interval.append(count)
    new_interval += count

for i in range(0, intervals_length):
    static_densities.append(round(developments_in_interval[i] / (developments_length * interval_length), 6))

#Calculation of γ-percent operating time
P1 = round(1 - static_densities[0] * intervals[0], 6)

d = round((P1 - y) / (P1 - P0), 2)

T = round(intervals[0] - intervals[0] * d, 2)

#Calculation of the probability of failure-free operation
count = 0
for i in range(0, intervals_length):
    count += 1
    if intervals[i] > t:
        interval_found = intervals[i - 1]
        break

for i in range(0, count - 1):
    total += static_densities[i] * intervals[0]

P = round(1 - (total + static_densities[count - 1] * (t - interval_found)), 5)

# Calculation failure intensity
failure_intensity = round(static_densities[count - 1] / P, 6)

print(f"Average developments = {average_developments}\nγ-percent operating time = {T}\n"
      f"Probability of failure-free operation = {P}\nFailure intensity = {failure_intensity}")
