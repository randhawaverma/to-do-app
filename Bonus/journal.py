j_date = input("Enter today's date: ")
mood = input("Rate your mood today: 1 - 10 - ")
thoughts = input("Let your thoughts flow :\n")
with open(f'{j_date}.txt', 'w') as file:
    file.write(f"Mood Score: {mood} \n")
    file.writelines(thoughts)


