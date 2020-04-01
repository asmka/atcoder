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
r"3
2 3 5
" => "7",

r"10
1 1 1 1 1 1 1 1 1 1
" => "11"
}

use std::cmp::max;
use std::cmp::min;

fn main() {
    println!("{}", solve(&stdin!()));
}

fn solve(src: &str) -> String {
    input! {
        source = src,
        N: i32,
        p: [i32; N]
    }
    let sum_max: i32 = p.iter().sum();
    let mut dp: Vec<Vec<bool>> = vec![vec![false; (sum_max+1) as usize]; N as usize];
    for i in 0..dp.len() {
        for sc in 0..(sum_max+1) as usize {
            if i == 0 {
                dp[i][sc] = sc == 0 || sc as i32 == p[i];
                continue;
            }
            if sc as i32 - p[i] >= 0 {
                dp[i][sc] = dp[i-1][sc] | dp[i-1][sc-(p[i] as usize)];
            } else {
                dp[i][sc] = dp[i-1][sc];
            }
        }
    }
    let mut cnt: i32 = 0;
    for sc in 0..(sum_max+1) as usize {
        if dp[N as usize - 1][sc] == true {
            cnt += 1;
        }
    }

    let ans: String = cnt.to_string();
    return ans;
}
