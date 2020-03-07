#![allow(non_snake_case)]

fn main() {
    let mut inbuf = String::new();
    std::io::stdin().read_line(&mut inbuf).unwrap();
    let S = inbuf.trim_right().to_owned();

    let date: Vec<&str> = S.split('/').collect();
    let year: i32 = date[0].parse().unwrap();
    let month: i32 = date[1].parse().unwrap();
    let day: i32 = date[2].parse().unwrap();

    let mut ans = "Heisei";
    if year > 2019 || year == 2019 && month >= 5 {
        ans = "TBD"
    }

    println!("{}", ans);
}
