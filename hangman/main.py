import random
file = open('words.txt').read().splitlines()
word = list(random.choice(file))
print('-'*15,'HANGMAN','-'*15)
vowels = list('aeiou')
guess = []
for _ in range(len(word)):
    guess.append('_')
for i in range(len(word)):
    if word[i] in vowels:
        guess[i] = word[i]
print(' '.join(guess))
c = 5
wordt = list(word)
while c!=0:
    att = input(f'gues the letter, you have {c} chances left->')
    if att in word:
        n = word.index(att)
        guess[n] = word[n]
        word[n] = '0'
        print(' '.join(guess))
    else:
        print(' '.join(guess))
        c-=1
    if guess==wordt:
        print('Yay you guessed the word correctly')
        break

if guess!=wordt:
    print('you could not guess it right')
print('correct word is',''.join(wordt))


