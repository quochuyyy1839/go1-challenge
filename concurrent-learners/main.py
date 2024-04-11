import json

# Calculate the maximum concurrent streams
def max_concurrent_streams(streams):
    events = []
    for stream in streams:
        events.append((stream[1], 1)) # start event => concurrent +1
        events.append((stream[2], -1)) # end event => concurrent -1

    events.sort() # Sort events

    max_concurrent = 0
    concurrent = 0
    for _, event in events: # caculate the maximum concurrent stream
        concurrent += event
        max_concurrent = max(max_concurrent, concurrent) 

    return max_concurrent

with open('data.json', 'r') as file: 
    streams = json.load(file)

# Calculate the maximum concurrent streams

result = max_concurrent_streams(streams)
print(f"\nMaximum concurrent streams: {result}")

def concurrent_streams_with_users(streams):
    events = []
    for stream in streams:
        events.append((stream[1], stream[0], 1)) # Event start  => concurrent +1
        events.append((stream[2], stream[0], -1)) # event end => concurrent -1
    
    events.sort() # Sort events
    max_concurrent = 0
    concurrent = 0
    concurrent_users = set()
    for time, user_id, event in events:
        concurrent += event
        if concurrent >= 2:
            concurrent_users.add(user_id)
        elif user_id in concurrent_users:
            concurrent_users.remove(user_id)

    return concurrent_users

with open('data.json', 'r') as file: 
    streams = json.load(file)

result = concurrent_streams_with_users(streams)
print(f"\nConcurrent streams with users: {result}")