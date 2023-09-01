characters = ['Monkey D. Luffy', 'Naruto Uzumaki', 'Tanjiro']
animelist = ['One-Piece.txt', 'Naruto.txt', 'Demon-Slayer.txt']

for hero, anime in zip(characters, animelist):
    with open(f"../files/{anime}", 'w') as file:
        file.writelines(hero)
