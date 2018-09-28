"""
Cache using First In First Out (FIFO) Algorithm
"""
import ast

MODULE_NAME = 'First In First Out'
CACHE_SIZE = 16

# For FIFO implementation, we can use a list
# Push from left -> |-|-|-|-|-| -> pop from right

"""
Push to the left of the list
rd: redis object
key: list name
value: user (type dictionary)
Instead of rd.lpop(), rd.lset() can also be used
"""
def add_to_cache(rd, cache_key, value, set_key=None):
    rd.lpush(cache_key, value)
    
    if rd.llen(cache_key) > CACHE_SIZE: # (CACHE_SIZE - 1) because length is 0 at first
        popped_user = ast.literal_eval(pop_cache(rd, cache_key)) # Convert string to dictionary
        
        # Return popped_user id
        return popped_user['id']

    return -1


# Pop the rightmost element
def pop_cache(rd, key):
    return rd.rpop(key)


# Find and remove the 'value' from the list
def remove_from_cache(rd, key, count, value):
    rd.lrem(key, count, value)


# Return the specified user_id from cache
def get_value(rd, key, user_id):
    i = 0
    while i < CACHE_SIZE:
        user = ast.literal_eval(rd.lindex(key, i))

        if user['id'] == user_id:
            return user
        
        i = i + 1

    return None  # User is not in cache
