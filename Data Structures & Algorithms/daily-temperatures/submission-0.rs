impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut temperatures_copy = temperatures.copy();
        let mut counts = vec![0; temperatures.len()];
        let mds = Vec::new(); // monotonic decreasing stack
        
        for (let i = 0; i < temperatures.len(); i++) {
            // if t > mds.last() {
            //     ...
            // }
            let t = temperatures[i];
            while let Some(&top) = mds.last() {
                if top < t {
                    stack.pop();
                    counts[i] = counts[i] + 1;
                } else {
                    break;
                }
            }
            stack.push(t);
        }

        counts
    }
}
