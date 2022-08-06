use std::io::Write;

const TN: i64 = 3;
const MAX: i64 = 100_000_000;

fn nth(n: i64) -> i8 {
    let mut count = 0;

    let bin = format!("{:b}", n);
    for a in bin.chars() {
        if a == '1' {
            count += 1;
        }
    }

    return count % 2;
}

fn main() {
    let mut last: i8 = -1;
    let mut count: i64 = 1;

    let mut x;
    let mut tn_location = 0;
    // Basically tn_location * TN
    let mut t_location = 0;

    let mut loc_of_ones =
        std::fs::File::create("data_locations_of_ones.csv").expect("create failed");
    let mut loc_of_zeros =
        std::fs::File::create("data_locations_of_zeros.csv").expect("create failed");

    loc_of_ones
        .write_all(format!("count,loc_in_t,loc_in_tn\n").as_bytes())
        .expect("write failed");

    loc_of_zeros
        .write_all(format!("count,loc_in_t,loc_in_tn\n").as_bytes())
        .expect("write failed");

    let mut file: &std::fs::File;

    let one_percent = MAX / 100;
    let mut percents_done = 0;

    let mut threes = 0.0;
    let mut not_threes = 0.0;
    let mut ratio: f64;

    loop {
        if t_location > one_percent * percents_done {
            percents_done += 1;

            print!("\x1b[1A\x1b[2K");
            println!("{percents_done}%");
        }

        x = nth(t_location);
        t_location += TN;
        tn_location += 1;

        // continue run
        if last == x {
            count += 1;
        // end of run
        } else {
            if count == 3 {
                threes += 1.0;
            } else {
                not_threes += 1.0;
            }

            if x == 1 {
                file = &loc_of_ones;
            } else {
                file = &loc_of_zeros;
            }

            ratio = threes / not_threes;

            file.write_all(format!("{ratio},{t_location},{tn_location}\n").as_bytes())
                .expect("write failed");

            // reset at end of run
            count = 1;
        }

        if t_location > MAX {
            break;
        }

        last = x;
    }

    print!("\x1b[1A\x1b[2K");
    println!("{percents_done}%");
}
