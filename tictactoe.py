import streamlit as st
import numpy as np
import pandas as pd

st.title("Tic Tac Toe")

# Initialize board
if "board" not in st.session_state:
    st.session_state.board = np.array([" ", " ", " ",
                                        " ", " ", " ",
                                        " ", " ", " "])
    st.session_state.turn = "X"

# Display board using pandas
df = pd.DataFrame(st.session_state.board.reshape(3, 3))
st.table(df)

# Button grid
for i in range(9):
    if st.button(f"Position {i+1}"):
        if st.session_state.board[i] == " ":
            st.session_state.board[i] = st.session_state.turn
            st.session_state.turn = "O" if st.session_state.turn == "X" else "X"

# Reset button
if st.button("Reset Game"):
    st.session_state.board = np.array([" ", " ", " ",
                                        " ", " ", " ",
                                        " ", " ", " "])
    st.session_state.turn = "X"
