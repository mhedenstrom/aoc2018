import re
from string import ascii_uppercase

step_order = open("steps.txt", "r").read().split('\n')

# step_order = [
#     "Step C must be finished before step A can begin.",
#     "Step C must be finished before step F can begin.",
#     "Step A must be finished before step B can begin.",
#     "Step A must be finished before step D can begin.",
#     "Step B must be finished before step E can begin.",
#     "Step D must be finished before step E can begin.",
#     "Step F must be finished before step E can begin."
# ]

all_steps = []
deps = {}
for s in step_order:
    m = re.search("Step (\\w+) must be finished before step (\\w+) can begin.", s)
    
    (dependency, step) = m.groups()
    if step not in all_steps:
        all_steps.append(step)
    if dependency not in all_steps:
        all_steps.append(dependency)

    deps[step] = [dependency] + deps[step] if step in deps else [dependency]

all_steps = sorted(all_steps)

completed_steps = []

def dependencies(step):
    return deps[step] if step in deps else []

def is_available(step):
    return all(step in completed_steps for step in dependencies(step))


completed_steps = []

available_steps = [
    step
    for step in all_steps
    if is_available(step)
]


# task: worker: (task, started)
worker_tasks = {}

def in_progress(step):
    return step in [task for (task, _) in worker_tasks.values()]

def next_step():
    steps = sorted([
        s
        for s in all_steps
        if s not in completed_steps and not in_progress(s) and (s not in deps or all(dep in completed_steps for dep in deps[s]))
    ])

    return steps[0] if len(steps) > 0 else None



completed_steps += available_steps[0]
while (len(completed_steps) < len(all_steps)):
    step = next_step()
    completed_steps.append(step)
# Part 1
print("Order of steps is %s" % ''.join(completed_steps))


#clean
completed_steps = []


workers = list(range(5))
# print(workers)





def step_time(step):
    # print("%s takes %d seconds" % (step, ascii_uppercase.index(step) + 1))
    return ascii_uppercase.index(step) + 1 + 60

time = -1

def done(task):
    (step, started) = task
    return time >= started + step_time(step)


def start_work(worker):
    step = next_step()
    if step is not None:
        # print("worker %d started working on %s" % (worker, step))
        worker_tasks[w] = (step, time)


def finish_work(worker):
    (step, _) = worker_tasks[w]
    # print("worker %d finished %s" % (worker, step))
    completed_steps.append(step)
    del worker_tasks[w]




while (len(completed_steps) < len(all_steps)):
    time += 1
    # print("time = %d" % time)
    for w in workers:
        if w in worker_tasks:
            if done(worker_tasks[w]):
                finish_work(w)
                start_work(w)
        else:
            start_work(w)

print("Workers finished after %d seconds" % time)