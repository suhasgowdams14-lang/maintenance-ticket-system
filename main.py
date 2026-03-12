import sqlite3

def create_ticket():
    machine_id = input("Enter Machine ID: ")
    issue = input("Enter Issue Description: ")
    priority = input("Enter Priority (Low/Medium/High): ")

    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tickets (machine_id, issue, priority, status) VALUES (?, ?, ?, ?)",
        (machine_id, issue, priority, "Open")
    )

    conn.commit()
    conn.close()

    print("Ticket created successfully!")

def view_tickets():
    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets")
    tickets = cursor.fetchall()

    for ticket in tickets:
        print(ticket)

    conn.close()

def update_ticket():
    ticket_id = input("Enter Ticket ID: ")
    status = input("Enter New Status (In Progress/Resolved): ")

    conn = sqlite3.connect("tickets.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tickets SET status=? WHERE ticket_id=?",
        (status, ticket_id)
    )

    conn.commit()
    conn.close()

    print("Ticket updated successfully!")

def menu():
    while True:
        print("\nMaintenance Ticket System")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Update Ticket")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            update_ticket()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

menu()