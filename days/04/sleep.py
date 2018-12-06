
def sleeps(shift):
    return [
        shift[1:][i:i+2]
        for i in range(0, len(shift[1:]), 2)
    ]

# just get the minute, ex: 1518-11-01 00:36 => 36
def minute(ts):
    m = re.search("(\\d+)$", ts)
    return int(m.groups()[0])


# list of minutes in this sleep, ex: [20, 21, 22, ..., 39]
def minutes_asleep(sleep):
    [fell_asleep, woke_up] = sleep
    return list(range(
        minute(fell_asleep[0]),
        minute(woke_up[0])
    ))


def sleep_by_guard(shifts):
    d = {}
    for shift in shifts:
        guard = shift[0][1]
        for sleep in sleeps(shift):
            d[guard] = (d[guard] or []) + minutes_asleep(sleep)
    return sleep_by_guard

