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
r"a?c
der
cod
" => r"7",

r"atcoder
atcoder
???????
" => r"7"
}

use std::cmp::max;
use std::cmp::min;

fn main() {
    println!("{}", solve(&stdin!()));
}

fn solve(src: &str) -> String {
    input! {
        source = src,
        a: chars,
        b: chars,
        c: chars,
    }

    // Get whether two substrings match by each gap
    let ab_match_vec: Vec<bool> = get_match_vec(&a, &b);
    let ac_match_vec: Vec<bool> = get_match_vec(&a, &c);
    let bc_match_vec: Vec<bool> = get_match_vec(&b, &c);

    let mut min_len: usize = a.len()+b.len()+c.len();
    //        af
    //        |
    // 0123456789ABCDEF
    // *******aa*******
    // ****bbb**bbb****
    // cccc********cccc

    // Check prior whether a and b match
    let af: usize = b.len()+c.len();
    for bf in 0..af+a.len()+c.len()+1 {
        if ! is_relative_matched_strings(&ab_match_vec, a.len(), b.len(), af, bf) {
            continue;
        }
        // a and b matched
        for cf in 0..af+a.len()+b.len()+1 {
            if ! is_relative_matched_strings(&ac_match_vec, a.len(), c.len(), af, cf) || ! is_relative_matched_strings(&bc_match_vec, b.len(), c.len(), bf, cf) {
                continue;
            }
            // a, b, and c Matched
            min_len = min(min_len, calc_len(a.len(), b.len(), c.len(), af, bf, cf));
        }
    }

    let ans: String = min_len.to_string();
    return ans;
}

fn get_match_vec(stra: &Vec<char>, strb: &Vec<char>) -> Vec<bool> {
    //    af
    //    |
    // 012345
    // ***aa***
    // bbb**bbb
    let mut match_vec: Vec<bool> = vec![false; stra.len()+strb.len()+1];
    let af: usize = strb.len();
    for bf in 0..match_vec.len() {
        // Calc whether string match
        let mut is_matched: bool = true;
        for i in bf..match_vec.len() {
            let mut cha: char = '?';
            let mut chb: char = '?';
            if af <= i && i < af+stra.len() {
                cha = stra[i-af];
            }
            if bf <= i && i < bf+strb.len() {
                chb = strb[i-bf];
            }
            if ! is_matched_chars(cha, chb) {
                is_matched = false;
                break;
            }
        }
        match_vec[bf] = is_matched;
    }
    return match_vec;
}

fn is_matched_chars(cha: char, chb: char) -> bool {
    if cha == '?' || chb == '?' {
        return true;
    }
    return cha == chb;
}

fn is_relative_matched_strings(relative_match_vec: &Vec<bool>, alen: usize, blen: usize, af: usize, bf: usize) -> bool {
    if bf+blen < af {
        return true;
    }
    if af+alen < bf {
        return true;
    }
    /*
    println!("af: {}", af);
    println!("alen: {}", alen);
    println!("bf: {}", bf);
    println!("blen: {}", blen);
    println!("relative_match_vec.len(): {}", relative_match_vec.len());
    println!("bf+blen-af: {}", bf+blen-af);
    println!("");
    */
    return relative_match_vec[bf+blen-af];
}

fn calc_len(alen: usize, blen: usize, clen: usize, af: usize, bf: usize, cf: usize) -> usize {
    let end = max(max(af+alen, bf+blen), cf+clen);
    let begin = min(min(af, bf), cf);
    return end-begin;
}
