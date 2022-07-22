use std::io::Write;

const TN: i64 = 3;
const MAX: i64 = 10_000_000_00;

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

    let mut loc_of_anoms =
        std::fs::File::create("data_locations_of_anomalies.csv").expect("create failed");

    let mut last_count: i64 = -1;

    loc_of_ones
        .write_all(format!("count,loc_in_t\n").as_bytes())
        .expect("write failed");

    loc_of_zeros
        .write_all(format!("count,loc_in_t\n").as_bytes())
        .expect("write failed");

    loc_of_anoms
        .write_all(format!("anom_percent,loc_in_t\n").as_bytes())
        .expect("write failed");

    let mut file: &std::fs::File;

    let one_percent = MAX / 100;
    let mut percents_done = 0;
    let mut anom_count = 0;

    loop {
        if t_location > one_percent * percents_done {
            percents_done += 1;
            // remove last lines
            print!("\x1b[1A\x1b[2K");
            print!("\x1b[1A\x1b[2K");
            print!("\x1b[1A\x1b[2K");
            print!("\x1b[1A\x1b[2K");
            println!("{percents_done}%");
            println!("Iterated {tn_location} times over T{TN}");
            println!("First {t_location} of T");
            println!(
                "6,8 anomaly percent {} ",
                anom_count as f64 / tn_location as f64
            );

            loc_of_anoms
                .write_all(
                    format!("{},{t_location}\n", anom_count as f64 / tn_location as f64).as_bytes(),
                )
                .expect("write failed");
        }

        x = nth(t_location);
        t_location += TN;
        tn_location += 1;

        // continue run
        if last == x {
            count += 1;
        // end of run
        } else {
            if count > 1 {
                if x == 1 {
                    file = &loc_of_ones;
                } else {
                    file = &loc_of_zeros;
                }

                // 6, 8 synchronization conjecture
                if x == 1 {
                    if count == 6 {
                        if last_count != 8 {
                            // println!("{t_location} {count} {last_count}")
                            anom_count += 1;
                        }
                    } else if count == 8 {
                        if last_count != 6 {
                            // println!("{t_location} {count} {last_count}")
                            anom_count += 1;
                        }
                    }

                    if count == 6 || count == 8 {
                        last_count = count;
                    }
                }

                file.write_all(format!("{count},{t_location}\n").as_bytes())
                    .expect("write failed");
            }
            count = 1;
        }

        if t_location > MAX {
            break;
        }

        last = x;
    }

    print!("\x1b[1A\x1b[2K");
    print!("\x1b[1A\x1b[2K");
    print!("\x1b[1A\x1b[2K");
    println!("Iterated {tn_location} times over T{TN}");
    println!("First {t_location} of T");
    println!(
        "6,8 anomaly percent {} ",
        anom_count as f64 / tn_location as f64
    );
}
