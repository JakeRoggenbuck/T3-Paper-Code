import logging
import threading

logging.basicConfig(
    filename="logs.log",
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

quantity = {
    1: 1000,
    2: 1000,
    3: 1000,
    4: 1000,
    5: 1000,
    6: 1000,
    7: 1000,
    8: 1000,
    9: 1000,
    10: 1000,
    11: 1000,
    12: 1000,
    13: 1000,
    14: 1000,
    15: 1000,
}


def find_thue_morse(lower=0, upper=1000, step=1):
    logging.warning(f"Started looking from {lower} to {upper} at a step of {step}")

    largest = 0
    index = 0

    cur = 0
    for x in range(lower, upper, step):
        c = bin(x).count('1') % 2

        if c:
            cur += 1
        else:
            if quantity.get(cur, 0) > 0:
                quantity[cur] -= 1
                largest = cur
                index = x

                start = index - (largest * 3)
                end = index
                logging.warning(f"New largest found from {start}:{end} and is {largest} long")
            cur = 0

    logging.warning(f"Finished looking from {lower} to {upper} at a step of {step}")


thread_step = 300_000_000
cover_window = 30

x = 0
y = thread_step

while 1:
    threads = []
    for _ in range(4):

        print(f"Starting thread for {x} to {y}")

        t = threading.Thread(
            target=find_thue_morse,
            args=(
                x,
                y,
                3,
            ),
        )

        x = y - 30
        y += thread_step

        t.start()
        threads.append(t)

    for t in threads:
        t.join()
