import streamlit as st

st.title("My Student Task Manager")

task = st.text_input("Enter your task")

subject = st.selectbox(
    "Select subject",
    ["Python", "DBMS", "Image Processing", "AIML"]
)

priority = st.selectbox(
    "Select priority",
    ["High", "Medium", "Low"]
)

if st.button("Add Task"):
    if task:
        st.success("Task added successfully!")
        st.write("Task:", task)
        st.write("Subject:", subject)
        st.write("Priority:", priority)
    else:
        st.warning("Please enter a task.")
