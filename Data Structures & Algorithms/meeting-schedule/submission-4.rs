/**
 * Definition of Interval:
 * #[derive(Debug, Clone)]
 * pub struct Interval {
 *     pub start: i32,
 *     pub end: i32,
 * }
 *
 * impl Interval {
 *     pub fn new(start: i32, end: i32) -> Self {
 *         Interval { start, end }
 *     }
 * }
 */

impl Interval {
    pub fn sort(mut intervals: Vec<Interval>) -> Vec<Interval> {
        intervals.sort_unstable_by_key(|i| i.start);
        intervals
    }
}

impl Solution {
    pub fn can_attend_meetings(intervals: Vec<Interval>) -> bool {
        let mut prev_end = i32::MIN;

        for interval in &Interval::sort(intervals) {
            if interval.start < prev_end {
                return false;
            }

            prev_end = interval.end;
        }

        true
    }
}
