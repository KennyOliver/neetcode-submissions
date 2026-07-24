impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut counts = vec![0; temperatures.len()];
        let mut mds = Vec::new(); // monotonic decreasing stack
        
        for i in 0..temperatures.len() {
            // if t > mds.last() {
            //     ...
            // }
            let t = temperatures[i];
            while let Some(&top) = mds.last() {
                counts[i] = counts[i] + 1;
                if top < t {
                    mds.pop();
                } else {
                    break;
                }
            }
            mds.push(t);
        }

        counts
    }
}
