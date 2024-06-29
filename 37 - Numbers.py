from collections import deque, defaultdict

first_number = int(input())
last_number = int(input())

previous = defaultdict(set)
previous[first_number] = set()
distances = {first_number: 0}
modifications = deque([first_number])

while last_number not in distances:
    cur_number = modifications.popleft()

    if cur_number // 1000 != 9:
        next_number = cur_number + 1000
        previous[next_number].add(cur_number)
        if next_number not in distances:
            distances[next_number] = distances[cur_number] + 1
            modifications.append(next_number)

    if cur_number % 10 != 1:
        next_number = cur_number - 1
        previous[next_number].add(cur_number)
        if next_number not in distances:
            distances[next_number] = distances[cur_number] + 1
            modifications.append(next_number)

    next_number = int(str(cur_number)[1:] + str(cur_number)[0])
    previous[next_number].add(cur_number)
    if next_number not in distances:
        distances[next_number] = distances[cur_number] + 1
        modifications.append(next_number)

    next_number = int(str(cur_number)[-1] + str(cur_number)[:3])
    previous[next_number].add(cur_number)
    if next_number not in distances:
        distances[next_number] = distances[cur_number] + 1
        modifications.append(next_number)

path = [last_number]
cur_number = last_number

while cur_number != first_number:
    for number in previous[cur_number]:
        if distances[cur_number] - distances[number] == 1:
            path.append(number)
            cur_number = number

for i in range(len(path) - 1, -1, -1):
    print(path[i])