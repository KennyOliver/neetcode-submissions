impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut temperatures_copy = temperatures.clone();
        let mut counts = vec![0; temperatures.len()];
        let mds = Vec::new(); // monotonic decreasing stack
        
        for i in 0..temperatures.len() {
            // if t > mds.last() {
            //     ...
            // }
            let t = temperatures[i];
            while let Some(&top) = mds.last() {
                if top < t {
                    mds.pop();
                    counts[i] = counts[i] + 1;
                } else {
                    break;
                }
            }
            mds.push(t);
        }

        counts
    }
}
