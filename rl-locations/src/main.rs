use std::io::Write;

fn nth_full_iter(n: i64) -> String {
    let mut s = String::from("0");
    let mut ns: String;

    for i in 0..n {
        println!("{}", i);
        ns = String::new();
        for c in s.chars() {
            ns += if c == '1' { "0" } else { "1" }
        }

        s += &ns;
    }

    return s;
}

fn nth(n: i64) -> i8 {
    let mut count = 0;

    let bin = format!("{:b}", n);
    for x in bin.chars() {
        if x == '1' {
            count += 1;
        }
    }

    return if count % 2 == 0 { 0 } else { 1 };
}

fn main() {
    let limit = 100_000_000;
    let mut count = 0;
    let mut n: i8;

    let mut count_zeros = 1;
    let mut count_ones = 1;
    let mut last = 1;

    let mut file = std::fs::File::create("data.csv").expect("create failed");

    let one_percent = limit / 100;
    let mut count_percent = 0;

    loop {

        if count > count_percent * one_percent && count < (count_percent + 1) * one_percent{
            println!("{}% done.", count_percent);
            count_percent += 1;
        }

        n = nth(count);

        if n == 1 {
            if last == 1 {
                count_ones += 1;
            } else {
                if count_ones > 1 {
                    file.write_all(
                        format!(
                            "{},{},{}\n",
                            count_ones,
                            count / 3,
                            (count / 3) + count_ones
                        )
                        .as_bytes(),
                    )
                    .expect("write failed");
                }
                count_ones = 1;
            }
        } else {
            if last == 0 {
                count_zeros += 1;
            } else {
                if count_zeros > 1 {
                    file.write_all(
                        format!(
                            "{},{},{}\n",
                            count_zeros,
                            count / 3,
                            (count / 3) + count_zeros
                        )
                        .as_bytes(),
                    )
                    .expect("write failed");
                }
                count_zeros = 1;
            }
        }

        last = n;

        count += 3;

        if count > limit {
            break;
        }
    }
}
