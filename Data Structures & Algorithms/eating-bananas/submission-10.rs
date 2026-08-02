impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let mut low = 1;
        let mut high = *piles.iter().max().unwrap_or(&1);

        while low < high {
            let mid = low + (high - low) / 2;
            let mut hours_spent = 0;

            for &pile in &piles {
                hours_spent += (pile as i64 + mid as i64 - 1) / mid as i64;
            }

            if hours_spent <= h as i64 {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        low
    }
}
