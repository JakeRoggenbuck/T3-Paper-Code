import threading


class T:
    def __init__(self, max=100_000, step=1):
        self._max = max
        self.step = step

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i / self.step >= self._max:
            raise StopIteration

        x = self.i
        self.i += self.step
        return "1" if bin(x).count('1') % 2 else "0"


def L(g, step):
    i = 0
    same_as_last = 1
    last = -1
    all = ""

    for x in g(step=step):
        if x == last:
            same_as_last += 1
        else:
            all += str(same_as_last)
            all += ","
            same_as_last = 1

        last = x
        i += 1

    with open(f"./outs/out_{step}.txt", "w") as file:
        file.write(all)


offset = 0
while 1:
    threads = []

    for n in range(1, 5):
        new = n + offset

        t = threading.Thread(
            target=L,
            args=(
                T,
                new,
            ),
        )

        t.start()
        threads.append(t)

        print(new)

    for t in threads:
        t.join()

    offset += 4
