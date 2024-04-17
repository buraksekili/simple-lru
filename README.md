# Simple LRU Cache

## Description

Simple LRU cache for learning purposes

## Usage

To use the Cache CLI Application, run the `main.py` script with the desired cache capacity as an argument. By default, capacity is 3. 

For example:

```bash
./main.py --capacity=5
```

Once the application is running, you can interact with the cache by entering commands directly in the terminal. The available commands are:

- `put key value`: Adds a new key-value pair to the cache.
- `get key`: Retrieves the value associated with the specified key.
- `print`: Prints the current contents of the cache.
- `exit`: Exits the application.

## Commands

### put

To add a new key-value pair to the cache, use the `put` command followed by the key and value. For example:

```bash
put 3 2
```

This command adds the key `3` with the value `2` to the cache.

### get

To retrieve the value associated with a specific key, use the `get` command followed by the key. For example:

```bash
get 3
```

This command retrieves the value associated with the key `3`.

### print

To print the current contents of the cache, simply enter the `print` command. This will display all key-value pairs currently stored in the cache.

### exit

To exit the application, enter the `exit` command.
