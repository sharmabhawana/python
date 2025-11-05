# Name Formatting
# Input: Full name (e.g., "kuldeep gusain").    
# Output: "Gusain, Kuldeep" in title case.
name=input("Enter your full name: ").title().split()
formatted_name=f"{name[1]},{name[0]}"
print(formatted_name)