class MinStack {
    stack <int> st;
    stack<int> minSt;
public:
    MinStack() {
        
    }
    
    void push(int value) {
        st.push(value);
        if (minSt.empty() || value <= minSt.top()){
            minSt.push(value);
        }
        
    }
    
    void pop() {
        int popValue = st.top();
        st.pop();

        if (popValue == minSt.top()){
            minSt.pop();
        }

        
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return minSt.top();
        
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(value);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */