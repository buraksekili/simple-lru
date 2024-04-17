#!/usr/bin/python3
import argparse
from cache import Cache 

def main():
    parser = argparse.ArgumentParser(description='LRU Cache CLI')
    parser.add_argument('--capacity', type=int, default=3, help='Capacity of the cache.')
    args = parser.parse_args()

    cache = Cache(args.capacity)

    while True:
        action = input("> ")
        if action.lower().strip() == 'help':
            print('Enter command (put key value, get key, print, exit, help')
        elif action.lower().strip() == 'exit':
            break
        elif action.startswith('put'):
            _, key, value = action.split()
            cache.put(key, value)
            print(f"Put key: {key}, value: {value} into cache.")
        elif action.startswith('get'):
            _, key = action.split()
            value = cache.get(key)
            if value != -1:
                print(f"Value for key {key}: {value}")
            else:
                print(f"Key {key} not found in cache.")
        elif action.lower().strip() == 'print':
            print("Current cache contents:")
            cache.print()
        else:
            print("Invalid command. Please try again.")
            print('Enter command (put key value, get key, print, exit, help')

if __name__ == '__main__':
    main()

