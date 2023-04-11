import streamlit as st
from modules import functions as fn

todos = fn.get_todos()


def add_todo():
    todo_loc = st.session_state["new_todo"]
    todos.append(todo_loc + '\n')
    fn.write_todos(todos)


st.title("My Todo App")
st.subheader("This is a subheader.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")

st.session_state