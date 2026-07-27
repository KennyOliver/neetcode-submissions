impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        // let mut prices = vec![10, 1, 5, 6, 7, 1];

        let mut target = 0;
        let mut desired_i = 0;
        let mut desired_j = 0;

        for i in 0..prices.len() {
            for j in 0..i {
                let diff = prices[i] - prices[j];
                target = if diff > target {
                        desired_i = i;
                        desired_j = j;
                        
                        diff
                    } else { target };
            }
        }

        target
    }
}
