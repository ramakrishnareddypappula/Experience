

def tower_of_hanoi(disks, src, dst, temp):
    if disks == 1:
        print("Move disk from " + src + " to " + dst)
    else:
        tower_of_hanoi(disks - 1, src, temp, dst)
        print("Move disk from " + src + " to " + dst)
        tower_of_hanoi(disks - 1, temp,  dst, src)

tower_of_hanoi(3, "A", "B", "C")

