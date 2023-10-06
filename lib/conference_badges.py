def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_messages = []
    for name in names:
        badge_messages.append(f"Hello, my name is {name}.")
    return badge_messages

def assign_rooms(names):
    badge_messages = []
    for room_number, name in enumerate(names, start=1):
        badge_messages.append(f"Hello, {name}! You'll be assigned to room {room_number}!")
    return badge_messages

def printer(names):
    badges = batch_badge_creator(names)

    for badge in badges:
        print(badge)
    
    room_assignments = assign_rooms(names)
    
    for assignment in room_assignments:
        print(assignment)

