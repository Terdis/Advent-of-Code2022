from collections import defaultdict
from pathlib import Path

##### PART ONE

with open("./Day07/input.txt", "r") as f:
    cwd = Path("/").as_posix()
    dirs = defaultdict(int)

    for line in f.read().splitlines():
        match line.split():
            case ["$", "cd", newdir]:
                cwd = cwd / newdir
                cwd = cwd.resolve()
            case [size, _] if size.isdigit():
                size = int(size)
                for path in [cwd, *cwd.parents]:
                    dirs[path] += size

    print(sum(x for x in dirs.values() if x <= 100000))

f.close()

##### PART TWO

with open("./Day07/input.txt", "r") as g:
    cwd = Path("/")
    dirs = defaultdict(int)

    for line in g.read().splitlines():
        match line.split():
            case ["$", "cd", newdir]:
                cwd = cwd / newdir
                cwd = cwd.resolve()
            case [size, _] if size.isdigit():
                size = int(size)
                for path in [cwd, *cwd.parents]:
                    dirs[path] += size

    print(min(x for x in dirs.values() if dirs[Path("C:/")] - x <= 70000000 - 30000000))

f.close()