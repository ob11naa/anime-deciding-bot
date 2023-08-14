from random import choice 

#list of animes
animes = ('naruto', 'one piece', 'forever', 'series', 'Gurren Lagann', 'Death Note', 'Cowboy Bebop Spirited Away', 'Princess Mononoke',
'Elfen Lied', 'Neon Genesis Evangelion', 'Code Geass: Lelouch of the Rebellion Bleach')

#input mood
print("how are you feeling today?")
mood = input()

#print a random anime from the anime
print (choice(animes))

        

