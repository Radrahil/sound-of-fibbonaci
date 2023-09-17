import musicalbeeps


player = musicalbeeps.Player(volume=1, mute_output=False)

player.play_note("C", 0.2)

fib1 = 0
fib2 = 1

for i in range(100):
    tempfib = fib1 + fib2
    fib1 = fib2 % 7
    fib2 = tempfib % 7
    match fib1:
        case 0:
            player.play_note("C", 0.2)
        case 1:
            player.play_note("D", 0.2)
        case 2:
            player.play_note("E", 0.2)
        case 3:
            player.play_note("F", 0.2)
        case 4:
            player.play_note("G", 0.2)
        case 5:
            player.play_note("A", 0.2)
        case 6:
            player.play_note("B", 0.2)
        case other:
            pass
