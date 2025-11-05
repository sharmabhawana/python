# Case-Insensitive Palindrome Check
# Input a string from the user.
# Ignore spaces, punctuation, and case.
# Check if it's a palindrome.
import string
st=input("Enter a string: ").lower()
for p in string.punctuation:
    st=st.replace(p,"")
    st=st.replace(" ","")
if st==st[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")