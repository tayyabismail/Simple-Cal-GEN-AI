import streamlit as st

# Title of the app
st.title("Simple Calculator")

# User input for numbers
num1 = st.number_input("Enter first number:", format="%.2f")
num2 = st.number_input("Enter second number:", format="%.2f")

# Choose an operation
operation = st.selectbox("Choose an operation:", ("Addition", "Subtraction", "Multiplication", "Division"))

# Perform the calculation
result = None
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of {num1} + {num2} is {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of {num1} - {num2} is {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of {num1} * {num2} is {result}")
    elif operation == "Division":
        if num2 == 0:
            st.error("Division by zero is not allowed.")
        else:
            result = num1 / num2
            st.success(f"The result of {num1} / {num2} is {result}")

# Display the result
if result is not None:
    st.write("Result:", result)
