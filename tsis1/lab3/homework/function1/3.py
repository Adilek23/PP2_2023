def solve(numheads, numlegs):
    ch = 0
    rb = 0
    rb = (numlegs - 2 * numheads)/2
    ch = numheads - rb
    print("rabbits: " , int(rb), " ", "chicken: " , int(ch))


solve(35, 94)