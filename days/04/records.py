import re

records = open("records.txt", "r").read().split('\n')

records = [
    "[1518-11-01 00:30] falls asleep",
    "[1518-11-01 23:58] Guard #99 begins shift",
    "[1518-11-01 00:25] wakes up",
    "[1518-11-05 00:45] falls asleep",
    "[1518-11-03 00:24] falls asleep",
    "[1518-11-04 00:36] falls asleep",
    "[1518-11-05 00:55] wakes up",
    "[1518-11-04 00:02] Guard #99 begins shift",
    "[1518-11-02 00:40] falls asleep",
    "[1518-11-05 00:03] Guard #99 begins shift",
    "[1518-11-03 00:05] Guard #10 begins shift",
    "[1518-11-04 00:46] wakes up",
    "[1518-11-02 00:50] wakes up",
    "[1518-11-01 00:55] wakes up",
    "[1518-11-01 00:00] Guard #10 begins shift",
    "[1518-11-01 00:05] falls asleep",
    "[1518-11-03 00:29] wakes up",
]

BEGINS_SHIFT = "begins shift"

def action(r):
    return r[2]

# segments list of records into shifts
def shifts(rs):
    shifts = []
    current_shift = None
    for (ts, guard, action) in rs:
        if action == "begins shift":
            if current_shift:
                shifts.append(current_shift)
            current_shift = []
        current_shift.append((ts, guard, action))

    if current_shift:
        shifts.append(current_shift)

    return shifts


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



regex = ''.join([
    "^\[(\d+-\d+-\d+ \d+:\d+)\] ", # [1518-11-05 00:36]
    "(?:Guard #(\\d+) )?", # Guard #99 (optional)
    "(begins shift|falls asleep|wakes up)$" # action
])

sorted = sorted([
    re.match(regex, r).groups()
    for r in records
], key = lambda t: t[0], )

sorted_records = sorted

sleep_by_guard = {}

for shift in shifts(sorted):
    for sleep in sleeps(shift):
        d = minutes_asleep(sleep)
        g = shift[0][1]
        sleep_by_guard[g] = sleep_by_guard[g] + d if g in sleep_by_guard else d



most_sleeping_guard = max(
    sleep_by_guard.items(), 
    key = lambda t: len(t[1])
)

(guard, minutes) = most_sleeping_guard

def count_minutes(minutes):
    count = {}
    for m in minutes:
        count[m] = count[m] + 1 if m in count else 1
    return count


def most_slept_minute(minutes):
    return max(
        count_minutes(minutes).items(),
        key = lambda t: t[1]
    )


# print([m for m in count_minutes(minutes) if m > 1])

print("Guard #%s spent the most minutes asleep, a total of %d minutes" % (guard, len(minutes)))
(msm, _) = max(count_minutes(minutes).items(), key = lambda t: t[1])
print("Guard #%s was asleep most during minute %d" % (guard, msm))

print("the answer is %d" % (msm * int(guard)))


guard_asleep_at_minute_with_count = [
    tuple([g] + list(most_slept_minute(ms)))
    for (g, ms) in sleep_by_guard.items()
]


(guard, most_slept_minute, _) = max(
    guard_asleep_at_minute_with_count, 
    key = lambda t: t[2])


print("Guard #%s spent minute %d asleep more than any other guard/minute" % (guard, most_slept_minute))
print("the second anwser is %d" % (int(guard) * most_slept_minute))