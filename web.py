import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To Do App")
st.subheader("This is my ToDo list application.")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo:", placeholder="A new todo...",
              on_change=add_todo, key="new_todo")

