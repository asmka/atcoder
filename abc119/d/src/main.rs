#![allow(non_snake_case)]

macro_rules! input {
    (source = $s:expr, $($r:tt)*) => {
        let mut iter = $s.split_whitespace();
        input_inner!{iter, $($r)*}
    };
    ($($r:tt)*) => {
        let s = {
            use std::io::Read;
            let mut s = String::new();
            std::io::stdin().read_to_string(&mut s).unwrap();
            s
        };
        let mut iter = s.split_whitespace();
        input_inner!{iter, $($r)*}
    };
}

macro_rules! input_inner {
    ($iter:expr) => {};
    ($iter:expr, ) => {};

    ($iter:expr, $var:ident : $t:tt $($r:tt)*) => {
        let $var = read_value!($iter, $t);
        input_inner!{$iter $($r)*}
    };
}

macro_rules! read_value {
    ($iter:expr, ( $($t:tt),* )) => {
        ( $(read_value!($iter, $t)),* )
    };

    ($iter:expr, [ $t:tt ; $len:expr ]) => {
        (0..$len).map(|_| read_value!($iter, $t)).collect::<Vec<_>>()
    };

    ($iter:expr, chars) => {
        read_value!($iter, String).chars().collect::<Vec<char>>()
    };

    ($iter:expr, usize1) => {
        read_value!($iter, usize) - 1
    };

    ($iter:expr, $t:ty) => {
        $iter.next().unwrap().parse::<$t>().expect("Parse error")
    };
}

macro_rules! stdin {
    () => {{
        use std::io::Read;
        let mut s = String::new();
        std::io::stdin().read_to_string(&mut s).unwrap();
        s
    }};
}

macro_rules! test {
    ($($input:expr => $expected_output:expr),*) => {
        #[test]
        fn solve_test() {
            let mut i = 0;
            println!("");
            $(
                i += 1;
                println!("Case {}:", i);
                println!("[in]\n{}", $input);
                println!("[out]\n{}", solve($input));
                println!("[expected out]\n{}", $expected_output);
                println!("");
                assert_eq!(solve($input), $expected_output);
             )*
        }
    }
}

test! {
r"2 3 4
100
600
400
900
1000
150
2000
899
799
" => r"350
1400
301
399",

r"1 1 3
1
10000000000
2
9999999999
5000000000
" => r"10000000000
10000000000
14999999998"
}

use std::cmp::max;
use std::cmp::min;

fn main() {
    println!("{}", solve(&stdin!()));
}

fn solve(src: &str) -> String {
    input! {
        source = src,
        A: i32, B: i32, Q: i32,
        s: [i64; A],
        t: [i64; B],
        x: [i64; Q]
    }
    
    let mut ans: String = String::new();
    for ix in x {
        if ! ans.is_empty() {
            ans += "\n";
        }
        let min_d: i64 = min(calc_min_d(&s, &t, ix), calc_min_d(&t, &s, ix));
        ans += &min_d.to_string();
    }

    return ans;
}

fn calc_min_d(l1: &Vec<i64>, l2: &Vec<i64>, p0: i64) -> i64 {
    let mut min_d: i64 = std::i64::MAX;
    let lrp1: Vec<i64> = nearest_lr(l1, p0);
    for p1 in lrp1 {
        let lrp2: Vec<i64> = nearest_lr(l2, p1);
        for p2 in lrp2 {
            let d: i64 = (p1-p0).abs() + (p2-p1).abs();
            min_d = min(min_d, d);
        }
    }
    return min_d;
}

fn nearest_lr(v: &Vec<i64>, p: i64) -> Vec<i64> {
    let np: i64 = b_search(v, p, 0, v.len() as i64);

    let mut lr: Vec<i64> = Vec::new();
    if p == v[np as usize] {
        lr.push(v[np as usize]);
    } else if p < v[np as usize] {
        if np-1 >= 0 {
            lr.push(v[(np-1) as usize]);
        }
        lr.push(v[np as usize]);
    } else {
        lr.push(v[np as usize]);
        if ((np+1) as usize) < v.len() {
            lr.push(v[(np+1) as usize]);
        }
    }
    return lr;
}

#[test]
fn nearest_lr_test() {
    let v: Vec<i64> = vec![2, 5];
    let e1: Vec<i64> = vec![2];
    let e2: Vec<i64> = vec![5];
    let e3: Vec<i64> = vec![2, 5];
    assert_eq!(nearest_lr(&v, 1), e1);
    assert_eq!(nearest_lr(&v, 6), e2);
    assert_eq!(nearest_lr(&v, 3), e3);
}

fn b_search(v: &Vec<i64>, p: i64, b: i64, e: i64) -> i64 {
    if e-b == 1 {
        return b;
    }
    let rb: i64 = b + (e-b)/2;
    if p < v[rb as usize] {
        return b_search(v, p, b, rb);
    } else {
        return b_search(v, p, rb, e);
    }
}
