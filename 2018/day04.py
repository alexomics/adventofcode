import sys
import re
import time
from collections import defaultdict

line_pat = re.compile(r"^\[(.*)\] (.*)$", flags=re.MULTILINE)
note_pat = re.compile(r"(\d+|falls asleep|wakes up)")
time_pat = "%Y-%m-%d %H:%M"

lines = sorted(line_pat.findall(sys.stdin.read()), key=lambda t: t[0])


def log_iter(log):
    for dt, line in log:
        if line.startswith("Guard"):
            guard = int(note_pat.findall(line)[0])
            break

    times = []
    for dt, line in log:
        dt = time.strptime(dt, time_pat)
        if line.startswith("Guard"):
            yield guard, times

            times = []
            guard = int(note_pat.findall(line)[0])
            continue
        times.append((note_pat.findall(line)[0], dt))
    yield guard, times


sleeping = defaultdict(lambda: [0 for _ in range(60)])
for guard, times in log_iter(lines):
    times = iter(times)
    for inst, start in times:
        _, end = next(times)
        for i in range(start.tm_min, end.tm_min):
            sleeping[guard][i] += 1

guard, times = max(sleeping.items(), key=lambda t: sum(t[1]))
idx_max = max(range(len(times)), key=times.__getitem__)
print(f"Part 1: {guard * idx_max}")

minute, g = 0, 0
for guard, times in sleeping.items():
    idx_max = max(range(len(times)), key=times.__getitem__)
    if idx_max > minute:
        minute = idx_max
        g = guard

print(f"Part 2: {g * minute}")
