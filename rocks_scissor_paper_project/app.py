import streamlit as st
import random

# Set page title
st.title("Rock Paper Scissors Game")

# Create a list of possible choices
choices = ["Rock", "Paper", "Scissors"]

# Create buttons for user choice
user_choice = st.radio("Make your choice:", choices)

# Add a play button
if st.button("Play"):
    # Computer makes a random choice
    computer_choice = random.choice(choices)
    
    # Display choices
    st.write(f"Your choice: {user_choice}")
    st.write(f"Computer's choice: {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        st.write("It's a tie! 🤝")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.write("You win! 🎉")
    else:
        st.write("Computer wins! 💻")
    
# Add game instructions
st.sidebar.header("Game Rules:")
st.sidebar.write("""
- Rock crushes Scissors
- Scissors cuts Paper
- Paper covers Rock
""") 