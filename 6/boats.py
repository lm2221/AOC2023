
file_path = '../data/6.txt'

def distance_traveled(button_time, max_time):
    speed = button_time
    remaining_time = max_time - button_time
    return remaining_time * speed


def boats_question1(file_path):
    
    data = {'Time': [], 'Distance': []}

    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into label and values
            label, *values = line.split()
            
            # Convert values to integers or floats
            values = list(map(int, values))
            
            # Store the values in the corresponding list based on the label
            data[label.strip(':')].extend(values)

    # Process the data as needed
    race_array = []
    for t,d in zip(data['Time'], data['Distance']):
        current_race = 0
        for ti in range(1,t+1):
            distance_trial = distance_traveled(ti, t) 
            if distance_trial > d:
                current_race+=1
        race_array.append(current_race)

    print(race_array)
    result = 1
    for element in race_array:
        result *= element
    return result

def boats_question2(file_path):
    time_values = []
    distance_values = []

    with open(file_path, 'r') as file:
        for line in file:
            label, *values = line.split()
            values = ''.join(values)

            if label.startswith('Time'):
                time_values.append(values)
            elif label.startswith('Distance'):
                distance_values.append(values)

    agg_time = int(time_values[0])
    agg_distance = int(distance_values[0])

    current_race = 0
    for ti in range(1, agg_time+1):
        distance_trial = distance_traveled(ti, agg_time) 
        if distance_trial > agg_distance:
            current_race+=1

    return current_race




def main():
    print('q1:', boats_question1(file_path))
    print('q2', boats_question2(file_path))

if __name__ == '__main__':
    main()
