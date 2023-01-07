import streamlit as st 
import base64
import streamlit as st


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("img1.jpeg,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('img1.jpeg')


st.title("C++ CODES FOR ALL QUESTIONS: ")
st.write("In here we are going to see all the codes for the question gave by kalai selvi mam.")
st.markdown("**WRITE A SIMPLE C++ PROGRAM**")
st.caption("An simple c++ program,printing welcome:")
st.code("""
 #include <iostream>
using namespace std;

int main() {
  cout << "Welcome to C++ programming language" << endl;
  return 0;
}
""")

st.markdown("**2. write a c++ program to print the age and name given by the user.**")

st.caption("Here is a simple C++ program that prompts the user to enter their name and age, and then prints a message with the user's name and age:")

st.code("""
#include <iostream>
#include <string>
using namespace std;

int main() {
  string name;
  int age;
  cout << "Enter your name: ";
  getline(cin, name);
  cout << "Enter your age: ";
  cin >> age;
  cout << "Your name is " << name << " and you are " << age << " years old." << endl;
  return 0;
}
""")
st.caption("This program uses the getline() function to read the user's name from the standard input, and it uses the cin stream to read the user's age. It then prints a message using the cout stream, combining the user's name and age into the message.")

st.caption("For example, if the user enters John for their name and 30 for their age, the program will output 'Your name is John and you are 30 years old.'")

st.markdown("**3. write a c++ program to print the word given by the user**")

st.code("""
#include <iostream>
#include <string>
using namespace std;

int main() {
  string word;
  cout << "Enter a word: ";
  cin >> word;
  cout << "You entered: " << word << endl;
  return 0;
}
""")

st.markdown("**4.Write a c++ program to add two numbers.**")

st.caption("Here is a simple C++ program that prompts the user to enter two numbers, and then calculates their sum:")

st.code("""
#include <iostream>
using namespace std;

int main() {
  int a, b;
  cout << "Enter the first number: ";
  cin >> a;
  cout << "Enter the second number: ";
  cin >> b;
  int sum = a + b;
  cout << "The sum is: " << sum << endl;
  return 0;
}
""")
st.caption("This program uses the cin stream to read the user's input, and it stores the input in variables a and b. It then calculates the sum of a and b and stores it in the variable sum. Finally, it uses the cout stream to print the sum to the standard output.")

st.markdown("**5.write a c++ program to swap two numbners**")

st.caption("Here is a simple C++ program that prompts the user to enter two numbers, and then swaps their values:")

st.code("""
#include <iostream>
using namespace std;

int main() {
  int a, b;
  cout << "Enter the first number: ";
  cin >> a;
  cout << "Enter the second number: ";
  cin >> b;
  cout << "Before swapping: " << a << " " << b << endl;
  int temp = a;
  a = b;
  b = temp;
  cout << "After swapping: " << a << " " << b << endl;
  return 0;
}
""")
st.caption("This program uses the cin stream to read the user's input, and it stores the input in variables a and b. It then prints the values of a and b before swapping them, using the cout stream. To swap the values, it creates a temporary variable called temp and assigns the value of a to it. It then assigns the value of b to a, and the value of temp (which is the original value of a) to b. Finally, it prints the values of a and b after swapping them.")
