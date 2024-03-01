import random
members = ["Mo","Mo", "Wilson","Wilson", "Sean", "Sean"]
exercises = [x for x in range(1,6)]

for x in exercises:
    rando = random.randint(0,len(members)-1)
    print(f"Exercise: {x} -{members[rando]}")
    members.pop(rando)

