from datetime import datetime
from time import sleep
from random import randint


odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 
         33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, ]


for _ in range(5):
    current_minute = datetime.today().minute
    if current_minute in odds:
        print('This minute seems a little odd.')
        print('Cool, eh?')
    else:
        print('Not an odd minute.')
        print('Groovy.')
    how_long = randint(1, 30)
    # print('Waiting', how_long, 'seconds...')
    # print(f"Waiting {sleep(randint(1, 30))} seconds...")
    print(f'Waiting {how_long} seconds...')
    sleep(how_long)
    
    
print('Done.')