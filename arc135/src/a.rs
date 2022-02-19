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
    r"15
    " => r"192",

    r"3
    " => r"3",

    r"100
    " => r"824552442"
}

use std::collections::HashMap;
const MOD: u64 = 998244353;

fn main() {
    println!("{}", solve(&stdin!()));
}

fn solve(src: &str) -> String {
    input! {
        source = src,
        S: u64
    }

    let memo = make_memo(S);
    let ans = memo.get(&S).unwrap();

    ans.to_string()
}

fn make_memo(root_val: u64) -> HashMap<u64, u64> {
    let mut vec: Vec<u64> = vec![root_val];
    let mut memo: HashMap<u64, u64> = HashMap::new();

    while !vec.is_empty() {
        let val: u64 = vec.pop().unwrap();
        if memo.contains_key(&val) {
            continue;
        }

        if val <= 4 {
            memo.insert(val, val % MOD);
            continue;
        }

        let low_child = val / 2;
        let high_child = if val % 2 == 0 { val / 2 } else { val / 2 + 1 };

        if memo.contains_key(&low_child) && memo.contains_key(&high_child) {
            memo.insert(
                val,
                memo.get(&low_child).unwrap() * memo.get(&high_child).unwrap() % MOD,
            );
        } else {
            vec.push(val);
            vec.push(low_child);
            vec.push(high_child);
        }
    }

    memo
}
