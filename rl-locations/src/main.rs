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
    let mut line = String::new();
    println!("Ready? ");
    std::io::stdin().read_line(&mut line).unwrap();

    let limit = 100_000_000;
    let mut count = 0;
    let mut n: i8;

    let mut count_zeros = 1;
    let mut count_ones = 1;
    let mut last = 1;

    let mut file1 = std::fs::File::create("data_locations_of_ones.csv").expect("create failed");
    let mut file2 = std::fs::File::create("data_locations_of_zeros.csv").expect("create failed");
    let mut file3 = std::fs::File::create("data_counts_two_of_ones.csv").expect("create failed");
    let mut file4 = std::fs::File::create("data_counts_two_of_zeros.csv").expect("create failed");

    let one_percent = limit / 100;
    let mut count_percent = 0.0;

    let mut threes_as_1 = 0;
    let mut sixes_as_1 = 0;
    let mut sevens_as_1 = 0;
    let mut eights_as_1 = 0;

    let mut threes_as_0 = 0;
    let mut sixes_as_0 = 0;
    let mut sevens_as_0 = 0;
    let mut eights_as_0 = 0;

    file1
        .write_all(format!("x,start,finish\n",).as_bytes())
        .expect("write failed");

    file2
        .write_all(format!("x,start,finish\n",).as_bytes())
        .expect("write failed");

    file3
        .write_all(format!("x,y,type\n",).as_bytes())
        .expect("write failed");

    file4
        .write_all(format!("x,y,type\n",).as_bytes())
        .expect("write failed");

    loop {
        if ((count as f32) > (count_percent as f32) * (one_percent as f32))
            && (count as f32) < ((count_percent as f32) + 0.5) * (one_percent as f32)
        {
            println!("{}% done.", count_percent);

            file3
                .write_all(format!("{},{},3\n", count / 3, threes_as_1).as_bytes())
                .expect("write failed");

            file3
                .write_all(format!("{},{},6\n", count / 3, sixes_as_1).as_bytes())
                .expect("write failed");

            file3
                .write_all(format!("{},{},7\n", count / 3, sevens_as_1).as_bytes())
                .expect("write failed");

            file3
                .write_all(format!("{},{},8\n", count / 3, eights_as_1).as_bytes())
                .expect("write failed");

            threes_as_1 = 0;
            sixes_as_1 = 0;
            sevens_as_1 = 0;
            eights_as_1 = 0;

            file4
                .write_all(format!("{},{},3\n", count / 3, threes_as_0).as_bytes())
                .expect("write failed");

            file4
                .write_all(format!("{},{},6\n", count / 3, sixes_as_0).as_bytes())
                .expect("write failed");

            file4
                .write_all(format!("{},{},7\n", count / 3, sevens_as_0).as_bytes())
                .expect("write failed");

            file4
                .write_all(format!("{},{},8\n", count / 3, eights_as_0).as_bytes())
                .expect("write failed");

            threes_as_0 = 0;
            sixes_as_0 = 0;
            sevens_as_0 = 0;
            eights_as_0 = 0;

            count_percent += 0.5;
        }

        n = nth(count);

        if n == 1 {
            if last == 1 {
                count_ones += 1;
            } else {
                if count_ones > 1 {
                    match count_ones {
                        3 => threes_as_1 += 1,
                        6 => sixes_as_1 += 1,
                        7 => sevens_as_1 += 1,
                        8 => eights_as_1 += 1,
                        _ => {
                            println!("{} at {} Hmm?", count_ones, count / 3)
                        }
                    }

                    file1
                        .write_all(
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
                    match count_zeros {
                        3 => threes_as_0 += 1,
                        6 => sixes_as_0 += 1,
                        7 => sevens_as_0 += 1,
                        8 => eights_as_0 += 1,
                        _ => {
                            println!("{} at {} Hmm?", count_zeros, count / 3)
                        }
                    }

                    file2
                        .write_all(
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
