move = 0
opportunities = 3
path = str("SSSSSNS")
track = str("")
while True:

    command = str(input("This is the magic maze. Which way you must go? (N,S,E,W):"))
    track += command
    print(track)
    move += 1


    if track == path:
        print("You have escaped the maze in", move, "moves!")


        break
    else:


        if move % 10 == 0:
            opportunities -= 1
            print("You have", opportunities, "lives left")
        if opportunities == 0:
            print("Game over")
            break
        if path.__contains__(track) and track.startswith("S"):
            continue
        else:
            print("Wrong move, starting over")
            track = str("")