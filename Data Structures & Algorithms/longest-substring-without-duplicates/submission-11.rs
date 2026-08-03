use std::collections::HashSet;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let mut set = HashSet::new();
        let mut max_len = 0;
        let mut l = 0;

        for r in 0..chars.len() {
            while set.contains(&chars[r]) {
                set.remove(&chars[l]);
                l += 1;
            }

            set.insert(chars[r]);
            max_len = max(max_len, r - l + 1);
        }

        max_len as i32
    }
}
