import streamlit as st
import sqlite3
import pandas as pd

def get_connection():
    return sqlite3.connect("tickets.db")

st.title("Industrial Maintenance Ticketing System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Create Ticket", "View Tickets", "Update Ticket"]
)

if menu == "Create Ticket":

    st.header("Create Maintenance Ticket")

    machine_id = st.text_input("Machine ID")
    issue = st.text_input("Issue Description")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])

    if st.button("Submit Ticket"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tickets (machine_id, issue, priority, status) VALUES (?, ?, ?, ?)",
            (machine_id, issue, priority, "Open")
        )

        conn.commit()
        conn.close()

        st.success("Ticket created successfully!")

elif menu == "View Tickets":

    st.header("All Maintenance Tickets")

    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM tickets", conn)

    total = len(df)
    open_tickets = len(df[df["status"] == "Open"])
    progress = len(df[df["status"] == "In Progress"])
    resolved = len(df[df["status"] == "Resolved"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Tickets", total)
    col2.metric("Open", open_tickets)
    col3.metric("In Progress", progress)
    col4.metric("Resolved", resolved)

    st.subheader("Ticket Table")
    st.dataframe(df)
    high_priority = df[df["priority"] == "High"]

if not high_priority.empty:
    st.warning("⚠ High Priority Issues Detected!")
    st.dataframe(high_priority)

    conn.close()

elif menu == "Update Ticket":

    st.header("Update Ticket Status")

    ticket_id = st.number_input("Ticket ID", step=1)
    status = st.selectbox("New Status", ["Open", "In Progress", "Resolved"])

    if st.button("Update Status"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE tickets SET status=? WHERE ticket_id=?",
            (status, ticket_id)
        )

        conn.commit()
        conn.close()

        st.success("Ticket updated successfully!")