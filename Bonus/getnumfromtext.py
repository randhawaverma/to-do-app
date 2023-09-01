def get_avg_temp(file):
    with open(file, 'r') as f:
        temp_list = f.readlines()

    values = temp_list[1:]
    values = [float(i) for i in values]

    average_local = sum(values) / len(values)

    return average_local


average = get_avg_temp("data.txt")
print(average)
