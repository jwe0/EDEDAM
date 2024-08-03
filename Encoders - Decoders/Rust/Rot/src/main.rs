use std::io::{self, Write};

fn main() {
    let nums: Vec<char> = (b'a'..=b'z').map(|c| c as char).collect();

    print!("[WORD]   > ");
    io::stdout().flush().unwrap();
    let mut word = String::new();
    io::stdin().read_line(&mut word).expect("Failed to read word");

    print!("[SHIFT]  > ");
    io::stdout().flush().unwrap();
    let mut shift = String::new();
    io::stdin().read_line(&mut shift).expect("Failed to read shift");

    let word = word.trim();
    let num: usize = shift.trim().parse().expect("Failed to parse shift");

    print!("[STRING] > ");

    for letter in word.chars() {
        if letter.is_ascii_alphabetic() {
            if let Some(index) = nums.iter().position(|&x| x == letter.to_ascii_lowercase()) {
                let new_index = (index + num) % 26; // Ensure the index wraps around
                print!("{}", nums[new_index]);
            }
        } else {
            // If the character is not alphabetic, print it as is
            println!("{}", letter);
        }
    }
    println!("");
}

