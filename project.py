import mysql.connector
from tabulate import tabulate
from datetime import datetime
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Yamini@7',
    database='Restaurant'
)
connect = con.cursor()

user_orders = {}
def inserting(num):
    connect.execute("select count(*) from Menu where LOWER(item_name) = LOWER(%s)", (num[0],))
    exists = connect.fetchone()[0]

    if exists > 0:
        print(f" Item '{num[0]}' already exists in Menu")
        return
    connect.execute("select coalesce(max(id), 0) from Menu")
    store = connect.fetchone()[0] + 1

    connect.execute(
        "insert into Menu (id, item_name, item_price, item_price_in, category) VALUES (%s, %s, %s, %s, %s)",
        (store, num[0], num[1], num[2], num[3])
    )
    con.commit()
    print(f" Successfully added new item '{num[0]}'")
def removing(itemname):
    connect.execute("delete from menu where item_name = %s", (itemname,))
    if connect.rowcount > 0:
        con.commit()
        print(" Successfully removed item")
    else:
        print(f" Item '{itemname}' not found in Menu")

def updating(itemname, field, new_value):
    valid_fields = ["item_name", "item_price", "item_price_in", "category"]
    if field not in valid_fields:
        print(" Invalid field!")
        return
    if field == "item_name":
        connect.execute("select count(*) from Menu where LOWER(item_name) = LOWER(%s)", (new_value,))
        exists = connect.fetchone()[0]
        if exists > 0:
            print(f" Item name '{new_value}' already exists. Choose another name.")
            return

    query = f"update Menu SET {field} = %s where item_name = %s"
    connect.execute(query, (new_value, itemname))
    if connect.rowcount > 0:
        con.commit()
        print(f" Successfully updated {field} of '{itemname}'")
    else:
        print(f" Item '{itemname}' not found")

def show_items():
    connect.execute("select id, item_name, item_price, item_price_in, category FROM Menu")
    rows = connect.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Price", "Investment", "Category"], tablefmt="fancy_grid"))

def show_orders():
    connect.execute("select * from Orders")
    rows = connect.fetchall()
    print(tabulate(rows, headers=[i[0] for i in connect.description], tablefmt="fancy_grid"))

def day_wise_profit():
    connect.execute("""
        SELECT 
            DATE(o.order_date) as day,
            SUM(o.quantity * (m.item_price - m.item_price_in)) as total_profit
        FROM Orders o
        JOIN Menu m ON o.item_name = m.item_name
        GROUP BY day
        ORDER BY day;
    """)
    result = connect.fetchall()

    print("\n Day Wise Profit Report")
    print(tabulate(result, headers=["Date", "Total Profit"], tablefmt="fancy_grid"))

def place_order(item_id, quantity, mobile):
    connect.execute("SELECT item_name, item_price FROM Menu WHERE id = %s", (item_id,))
    result = connect.fetchone()
    if result:
        itemname, price = result
        total = price * quantity
        connect.execute(
            "INSERT INTO Orders (mobile, item_name, quantity, total_price, order_datetime) "
            "VALUES (%s, %s, %s, %s, NOW())",

            (mobile, itemname, quantity, total)
        )
        con.commit()
        connect.execute("SELECT LAST_INSERT_ID()")
        oid = connect.fetchone()[0]

        user_orders.setdefault(mobile, []).append(oid)

        print(f" Order Placed: {itemname} × {quantity} = ₹{total} (Order ID {oid})")
    else:
        print(" Item not found")

def total_bill(mobile):
    query = "SELECT order_id, item_name, quantity, total_price, order_datetime FROM Orders WHERE mobile = %s"
    connect.execute(query, (mobile,))
    orders = connect.fetchall()
    
    if not orders:
        print("\n No order has been placed yet.\n")
        return
    
    print("\n=====  Your Bill =====")
    grand_total = 0
    for order in orders:
        order_id, item_name, quantity, total_price, order_datetime = order
        print(f"{order_id} | {item_name} | Qty: {quantity} | ₹{total_price} | {order_datetime}")
        grand_total += total_price
    
    print(f"\n Grand Total: ₹{grand_total}\n")
    print("=======================")

def cancel_order(order_id, mobile):
    query = "SELECT * FROM Orders WHERE order_id = %s AND mobile = %s"
    connect.execute(query, (order_id, mobile))
    result = connect.fetchone()

    if result:
        delete_query = "DELETE FROM Orders WHERE order_id = %s AND mobile = %s"
        connect.execute(delete_query, (order_id, mobile))
        con.commit()

        if mobile in user_orders and order_id in user_orders[mobile]:
            user_orders[mobile].remove(order_id)

        print(f" Order {order_id} cancelled successfully!")
    else:
        print(f" No such order found with Order ID {order_id} for your account.")


def admin_login():
    password = input("Enter admin password: ")
    if password == 'Yamini@123':
        print(" Admin Login successful\n")
        return True
    else:
        print(" Wrong Password! Access Denied\n")
        return False

def user_login():
    name = input("Enter your name: ")
    mobile = input("Enter your mobile number: ")
    if len(mobile) == 10 and mobile.isdigit() and mobile[0] in ['6','7','8','9']:
        print(f" Welcome {name}! Your mobile {mobile} is verified.")
        return name, mobile
    else:
        print(" Invalid mobile number. Must be 10 digits and start with 6/7/8/9.")
        return None, None

while True:
    print("\n------- LOGIN -----------")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    unknown = input("Choose one: ")

    if unknown == '1':  
        if not admin_login():
            continue
        while True:
            print("\n===== Admin Menu =====")
            print("1. Upload New Item") 
            print("2. Remove Item") 
            print("3. Update Item")
            print("4. View All Items")
            print("5. View All Orders")
            print("6. Day Wise Profit")
            print("7. Logout")
            admin = input("Choose option: ")

            if admin == '1':
                itemname = input("Enter item name: ")
                connect.execute("select count(*) from menu where LOWER(item_name)=LOWER(%s)",(itemname,))
                exists=connect.fetchone()[0]
                if exists>0:
                    print(f" Item '{itemname}' already exists in Menu")
                else:
                    sale = int(input("Enter sale price: "))
                    buy = int(input("Enter investment price: "))
                    category = input("Enter category: ")
                    inserting([itemname, sale, buy, category])

            elif admin == '2':
                itemname = input("Enter item name to remove: ")
                removing(itemname)

            elif admin == '3':
                itemname = input("Enter item name to update: ")
                print("1. Name\n2. Price\n3. Investment\n4. Category")
                choice = input("Choose: ")

                if choice == '1':
                    new_value = input("Enter new name: ")
                    updating(itemname, "item_name", new_value)
                elif choice == '2':
                    new_value = int(input("Enter new price: "))
                    updating(itemname, "item_price", new_value)
                elif choice == '3':
                    new_value = int(input("Enter new investment: "))
                    updating(itemname, "item_price_in", new_value)
                elif choice == '4':
                    new_value = input("Enter new category: ")
                    updating(itemname, "category", new_value)

            elif admin == '4':
                show_items()
            elif admin == '5':
                show_orders()
            elif admin == '6':
                day_wise_profit()
            elif admin == '7':
                break
            else:
                print(" Invalid choice")

    elif unknown == '2':
        name, mobile = user_login()
        if not name:
            continue
        while True:
            print("\n===== Restaurant System =====")
            print("1. View Menu")
            print("2. Place Order")
            print("3. View Total Bill")
            print("4. Cancel Order")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                show_items()

            elif choice == '2':
                item_id = int(input("Enter Item ID: "))
                qty = int(input("Enter quantity: "))
                place_order(item_id, qty, mobile)

                while True:
                    print("\nDo you want to order more?")
                    print("1. Yes")
                    print("2. No, go back to main menu")
                    next_action = input("Choose: ")
                    if next_action == '1':
                        item_id = int(input("Enter Item ID: "))
                        qty = int(input("Enter quantity: "))
                        place_order(item_id, qty, mobile)
                    elif next_action == '2':
                        break
                    else:
                        print(" Invalid choice")

            elif choice == '3':
                total_bill(mobile)
            elif choice == '4':
               oid=int(input("Enter Order ID to cancel: "))
               cancel_order(oid,mobile)
            elif choice == '5':
                print("Exiting... Thank you!")
                break
            else:
                print("Invalid choice")

    elif unknown == '3':
        print(" Goodbye!")
        break
    else:
        print(" Invalid choice")
