#include <iostream>
#include <iomanip>
#include <stack>
using namespace std;

// Function to determine the precedence of operators
int prec(char c) {
  if (c == '/' || c == '*')
    return 2;
  else if (c == '+' || c == '-')
    return 1;
  else
    return 0;
}

// Function to convert infix expression to postfix
string getPostfix(string s) {
  stack<char> st;
  string postfix;

  for (int i=0; i<s.length(); i++) {
    if (s[i] >= '0' && s[i] <= '9')
      postfix += s[i];  // Operand, add to postfix expression
    else if (s[i] == '(')
      st.push('(');     // Left parenthesis, push onto the stack
    else if (s[i] == ')') {
      while (st.top() != '(') {
        postfix += st.top();  // Pop operators from stack until matching '(' is found
        st.pop();
      }
      st.pop();  // Pop the '(' from the stack
    }
    else {
      while (!st.empty() && prec(s[i]) <= prec(st.top())) {
        postfix += st.top();  // Pop operators with higher or equal precedence
        st.pop();
      }
      st.push(s[i]);  // Push the current operator onto the stack
    }
  }

  while (!st.empty()) {
    postfix += st.top();  // Pop any remaining operators from the stack
    st.pop();
  }

  return postfix;
}

// Function to evaluate postfix expression
int evaluatePostfix(string s) {
  stack<int> st;

  for (int i=0; i<s.length(); i++) {
    if (s[i] >= '0' && s[i] <= '9')
      st.push(s[i] - '0');  // Operand, push onto the stack as an integer
    else {
      // Operator, pop two operands, perform the operation, and push the result back
      int val1 = st.top(); st.pop();
      int val2 = st.top(); st.pop();
      switch (s[i]) {
        case '+': st.push(val2 + val1); break;
        case '-': st.push(val2 - val1); break;
        case '*': st.push(val2 * val1); break;
        case '/': st.push(val2 / val1); break;
      }
    }
  }
  return st.top();  // The final result is at the top of the stack
}

int main() {
  // Example infix expression
  string exp = "(8*9-(0+(9/3*2)*2*3)*2+9)";
  char opr = '/';  // Operator
  int temp = 4;    // Temporary value
  double x = 0;    // Final result
  bool front = false;  // Determines the order of subtraction or division

  // Get postfix expression and print it
  string postfix = getPostfix(exp);
  cout << postfix << endl;

  // Evaluate postfix expression and print the result
  int result = evaluatePostfix(postfix);
  cout << result << endl;

  // Calculate the final result based on the operator and temporary value
  if (opr == '+')
    x = (double)temp - (double)result;
  else if (opr == '-') {
    if (front)
      x = (double)temp + (double)result;
    else
      x = (double)result - (double)temp;
  }
  else if (opr == '*')
    x = (double)temp / (double)result;
  else {
    if (front)
      x = (double)temp * (double)result;
    else
      x = (double)result / (double)temp;
  }

  // Print the final result with three decimal places
  cout << setprecision(3) << x << endl;

  return 0;
}
