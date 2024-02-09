# Exercise 4

## Question 1
**Describe the algorithm you will use to find the room. Assume all the information you have is the one given by the sign; you have no knowledge of the floor plan** [0.5 pts]

I would go with a simple modified approach taking inspiration from linear search. Linear search seems practical here since the amount of rooms is not a lot considering it's not a ton of rooms shown on the sign. Depending on the room I'm looking for, I will start with the left if my room ranges from 100-130 and the right if it does not fall within that range. I would then start from whatever side that was chosen, comparing room numbers all around the floor until I find the room I seek.

## Question 2
**How many "steps" it will take to find room EY128? And what is a "step" in this case?** [0.25 pts]

Assuming each room I reach is a step, it would take 15 steps.

## Question 3
**Is this a best-case scenario, worst-case scenario, or neither?** [0.25 pts]

This is neither a best or worst case scenario.

## Question 4
**With this particular sign and floor layout, explain what a worst-case or best-case scenario would look like** [0.5 pts]

The worst-case scenario would be that the room is EY130, in which I go left and traverse through 16 steps to find the room. The best-case scenario would be either EY138 or EY100, both of which I would have to either go to the first room on the right or left, respectively. Both these scenarios are the best-case with 1 step taken.

## Question 5
**Suppose after a few weeks in the term you memorize the layout of the floor. How would you improve the algorithm to make it more efficient?** [0.5 pts]

With knowledge of the floor plan, I would modify the initial conditions of the search of my modified linear search algorithm. If my floor ranges from 100-118 (inclusive), I will scan starting from the left as I know it increases in ascending order. If my floor falls into 118-138 (not inclusive of 118), then I would start scanning from the right. This would increase the efficiency of the algorithm by not getting misled by the sign.
