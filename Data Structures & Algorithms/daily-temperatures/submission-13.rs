impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut counts = vec![0; temperatures.len()];
        let mut temps_idx: Vec<usize> = Vec::new(); // monotonic decreasing stack

        for (i, &t) in temperatures.iter().enumerate() {
            while let Some(&top) = temps_idx.last() {
                if t > temperatures[top] {
                    temps_idx.pop();
                    counts[top] = (i - top) as i32;
                }
            }

            temps_idx.push(i);
        }

        counts
    }
}
