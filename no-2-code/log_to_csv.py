with open("./july_2_logs.log") as file:
    lines = file.readlines()

with open("./out.csv", "w") as out:
    out.write("start,end,num\n")
    for line in lines:
        if "New" in line:
            _, numbers = line.split("from ")
            found_range, _, _, num, _ = numbers.split()
            start, end = found_range.split(":")
            out.write(f"{start},{end},{num} \n")
