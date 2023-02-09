qs=["What is your name?->",
    "what is your fav. color?->",
    "what is your quest?->"]
n=0
while True:
    print("Type q to quit:")
    a=input(qs[n])
    if a=="q":
        break
    n=(n+1)%3