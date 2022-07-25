def find_cycle(n):
    seen = [False for i in range(n)]
    done = False
    next= 1
    curr_ind = 0
    while not done:
        next = (next * 10) % n
        curr_ind += 1
        if next == 0:
            return 0
        if seen[next - 1] is False:
                seen[next - 1] = curr_ind
        else:
                return (curr_ind - seen[next - 1])


def find_max_cycle(max_num):
    max, num = 0, 0
    for i in range(2, max_num):
        curr_num, curr_max = i, find_cycle(i)
        if curr_max > max:
            max = curr_max
            num = curr_num
    return num, max


print(find_max_cycle(1000))

# props to hbomb4564 at https://projecteuler.net/thread=26;page=8
# "not that you need it" "no but that *is* a weakness"... <- this is unrelated. Anyway, I stole this from the internet
# and I won't bother trying to understand it.
