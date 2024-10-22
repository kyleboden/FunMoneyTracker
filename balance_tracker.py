import streamlit as st
import os

# Define the filename to store the balance
BALANCE_FILE = "balance.txt"

# Function to read the balance from the file
def read_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as file:
            return float(file.read())
    return 0.0  # Default balance if file does not exist

# Function to write the balance to the file
def write_balance(balance):
    with open(BALANCE_FILE, "w") as file:
        file.write(f"{balance:.2f}")

# Function to update balance based on input
def update_balance(amount, operation):
    if operation == "add":
        st.session_state.balance += amount
    elif operation == "subtract":
        st.session_state.balance -= amount
    write_balance(st.session_state.balance)  # Save the updated balance
    st.success(f"Updated Balance: ${st.session_state.balance:.2f}")

    # Reset the input fields
    st.session_state.add = 0.0
    st.session_state.subtract = 0.0

# Set the title of the app
st.title("Balance Tracker")

# Initialize balance from the file
if 'balance' not in st.session_state:
    st.session_state.balance = read_balance()

# Display the current balance in a larger font
st.markdown(f"<h1 style='font-size: 48px;'>Current Balance: ${st.session_state.balance:.2f}</h1>", unsafe_allow_html=True)

# Create input fields for adding and subtracting
add_amount = st.number_input("Add Amount:", min_value=0.0, step=0.01, key="add", on_change=lambda: update_balance(st.session_state.add, "add"))
subtract_amount = st.number_input("Subtract Amount:", min_value=0.0, step=0.01, key="subtract", on_change=lambda: update_balance(st.session_state.subtract, "subtract"))

# Show a note for the user
st.info("Enter an amount and press Enter to update your balance.")
