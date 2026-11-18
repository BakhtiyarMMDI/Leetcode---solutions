class Solution {
public:
    int evalRPN(vector<string>& tokens) {

        stack<int> st;

        for (string op : tokens){

            if (op != "+" && op != "-" && op != "*" && op != "/"){
                st.push(stoi(op));
            }
            else {
                int first = st.top();
                st.pop();
                int second = st.top();
                st.pop();

                if (op == "+"){
                    st.push(second + first);
                }
                else if (op == "-"){
                    st.push(second - first);
                }
                else if (op == "*"){
                    st.push(second * first);
                }
                else if (op == "/"){
                    st.push(second / first);
                }

            }

        }
        return st.top();
        
    }
};