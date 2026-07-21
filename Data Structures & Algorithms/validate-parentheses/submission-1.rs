#[derive(Debug)]
pub struct Stack<T> {
    elements: Vec<T>,
}

impl<T> Stack<T> {
    pub fn new() -> Self {
        Self {
            elements: Vec::new()
        }
    }

    pub fn push(&mut self, item: T) {
        self.elements.push(item);
    }

    pub fn pop(&mut self) -> Option<T> {
        self.elements.pop()
    }

    pub fn peek(&self) -> Option<&T> {
        self.elements.last()
    }

    pub fn len(&self) -> usize {
        self.elements.len()
    }

    pub fn is_empty(&self) -> bool {
        self.elements.is_empty()
    }
}

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let length = s.len();
        let mut p_stack = Stack::new();

        for ch in s.chars() {
            match ch {
                '(' | '{' | '[' => p_stack.push(ch),
                ')' => if p_stack.pop() != Some('(') { return false },
                '}' => if p_stack.pop() != Some('{') { return false },
                ']' => if p_stack.pop() != Some('[') { return false },
                _ => {}
            }
        }
        
        p_stack.is_empty()
    }
}
