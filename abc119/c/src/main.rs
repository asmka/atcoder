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
r"5 100 90 80
98
40
30
21
80
" => r"23",

r"8 100 90 80
100
100
90
90
90
80
80
80
" => r"0",

r"8 1000 800 100
300
333
400
444
500
555
600
666
" => r"243"
}

//use std::cmp::max;
use std::cmp::min;

fn main() {
    println!("{}", solve(&stdin!()));
}

fn solve(src: &str) -> String {
    input! {
        source = src,
        N: i32, A: i32, B: i32, C: i32,
        l: [i32; N]
    }
    let ans: String = calc_min_mp(0, &l, &vec![A, B, C]).to_string();
    return ans;
}

fn calc_min_mp(sum_mp: i32, from_bamboov: &Vec<i32>, to_bamboov: &Vec<i32>) -> i32 {
    // Has Made all bamboos
    if to_bamboov.len() == 0 {
        return sum_mp;
    }

    let mut sum_min_mp: i32 = std::i32::MAX;
    for bits in 1..2i32.pow(from_bamboov.len() as u32) {
        let src_bamboov: Vec<i32> = ext_vec(&from_bamboov, bits);
        let rest_bamboov: Vec<i32> = ext_restvec(&from_bamboov, bits);

        let dst_bamboo: i32 = to_bamboov[0];
        let next_to_bamboov: Vec<i32> = to_bamboov[1..].to_vec();

        // Overuse bamboos
        if rest_bamboov.len() < next_to_bamboov.len() {
            continue;
        }

        // Make a bamboo
        let used_mp: i32 = calc_mp(&src_bamboov, dst_bamboo);

        // Make the rest bamboos
        let min_mp: i32 = calc_min_mp(sum_mp+used_mp, &rest_bamboov, &next_to_bamboov);

        sum_min_mp = min(sum_min_mp, min_mp);
    }
    return sum_min_mp;
}

fn ext_vec(bamboov: &Vec<i32>, bits: i32) -> Vec<i32> {
    let digit: i32 = bamboov.len() as i32;

    // digit:     4321
    // index:     0123
    // bits:      0110
    let mut ext_bamboov: Vec<i32> = Vec::new();
    let mut d: i32 = digit;
    while d > 0 {
        let i: usize = (digit - d) as usize;
        let b: i32 = (bits >> d-1) & 0b1;
        if b == 0b1 {
            ext_bamboov.push(bamboov[i]);
        }
        d -= 1;
    }
    return ext_bamboov;
}

#[test]
fn ext_vec_test() {
    assert_eq!(ext_vec(&vec![1, 2, 3], 0b10), vec![2]);
}

fn ext_restvec(bamboov: &Vec<i32>, bits: i32) -> Vec<i32> {
    let digit: i32 = bamboov.len() as i32;
    let rest_bits: i32 = 0b10i32.pow(digit as u32)-1 ^ bits;

    // bits:      0110
    // rest_bits: 1001
    return ext_vec(bamboov, rest_bits);
}

#[test]
fn ext_restvec_test() {
    assert_eq!(ext_restvec(&vec![1, 2, 3], 0b10), vec![1,3]);
}

fn calc_mp(use_bamboov: &Vec<i32>, dest_bamboo: i32) -> i32 {
    let sum_len: i32 = use_bamboov.iter().fold(0, |sum, x| sum + x);
    let mp: i32 = 10*(use_bamboov.len() as i32 - 1) + (dest_bamboo - sum_len).abs();
    return mp;
}

#[test]
fn calc_mp_test() {
    assert_eq!(calc_mp(&vec![1], 10), 9);
    assert_eq!(calc_mp(&vec![1, 2, 3], 4), 22);
    assert_eq!(calc_mp(&vec![1, 2, 3], 10), 24);
}
