def solve(heads,legs):
    r=0.5*legs-heads
    c=heads-r
    print("chickens: "+str(round(c)))
    print("rabbits: "+str(round(r)))
solve(35,94)