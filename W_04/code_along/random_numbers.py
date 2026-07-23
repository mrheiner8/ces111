import random

words = ['big', 'red', 'funny', 'baby', 'yellow', 'wait', 'python', 'Joseph']

def main():
    numbers_list = [16.2, 75.1, 52.3]
    w_list = []
    print(f'The list before adding from the function {numbers_list}')
    append_random_numbers(numbers_list)
    print(f'The list after adding from the function {numbers_list}')
    append_random_numbers(numbers_list,3)
    print(f'The list after adding from the function with quantity {numbers_list}')

    print(f'The list of words {words}')
    append_random_words(w_list)
    print(f'One random word from the list after running the function {w_list}')
    append_random_words(w_list,4)
    print(f'Random words from the list after running the function with quantity {w_list}')

def append_random_words(words_list,quantity=1):
    for _ in range(quantity):
        words_list.append(random.choice(words))

def append_random_numbers(num_list,quantity=1):
    for _ in range(quantity):
        num=random.uniform(0,100)
        num=round(num,1)
        num_list.append(num)

if __name__ == "__main__":
    main()




"""
#import library module
import random    
#print random number by calling on the module wit 2 argument(0,100) or from 0-100 
print (random.uniform(0,100))
# using built in rounding function
print (round(random.uniform(0,100),1))

# or write it out the long way with a var (variable)
r=random.uniform (0,100)
r=round(r,1)
print(r)
"""