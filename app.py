from flask import Flask, render_template, request, redirect, url_for, session, flash
import pymysql

app = Flask(__name__)
app.secret_key = 'your_secret_key'

db = pymysql.connect(
    host="localhost",
    user="root",
    password="Chintu@2238",
    database="pharmacy_hubs"
)
cursor = db.cursor()

# Function to get DB connection with dict cursor
def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Chintu@2238",
        database="pharmacy_hubs",
        cursorclass=pymysql.cursors.DictCursor
    )

# Index Route
@app.route('/')
def index():
    return render_template('index.html')

# Get medicine by ID
def get_medicine_by_id(medicine_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM medicines WHERE medicine_id = %s", (medicine_id,))
    medicine = cur.fetchone()
    conn.close()
    return medicine

# Medicines Route
@app.route('/medicines')
def medicines():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT medicines.*, categories.category_name FROM medicines
        JOIN categories ON medicines.category_id = categories.category_id
    """)
    medicines = cursor.fetchall()
    conn.close()
    
    meds = []
    for med in medicines:
        meds.append({
            'medicine_id': med['medicine_id'],
            'name': med['name'],
            'description': med['description'],
            'price': med['price'] if med['price'] else 0.0,
            'stock': med['stock'],
            'category': med['category_name'],
            'image_url': med['image_url']
        })

    return render_template('medicines.html', medicines=meds)
# Add to Cart
@app.route('/add_to_cart/<int:medicine_id>', methods=['POST'])
def add_to_cart(medicine_id):
    if 'user_id' not in session:
        flash('You must be logged in to add items to your cart.', 'danger')
        return redirect(url_for('signin'))

    medicine = get_medicine_by_id(medicine_id)
    if not medicine:
        flash('Medicine not found.', 'danger')
        return redirect(url_for('medicines'))

    price = float(medicine['price']) if medicine['price'] else 0.0
    cart_items = session.get('cart_items', [])

    for item in cart_items:
        if item['medicine_id'] == medicine['medicine_id']:
            item['quantity'] += 1
            break
    else:
        cart_items.append({
            'medicine_id': medicine['medicine_id'],
            'name': medicine['name'],
            'price': price,
            'quantity': 1
        })

    session['cart_items'] = cart_items
    flash(f'{medicine["name"]} added to your cart!', 'success')
    return redirect(url_for('cart'))

# Cart Route
@app.route('/cart')
def cart():
    if 'user_id' not in session:
        flash('You must be logged in to view your cart.', 'danger')
        return redirect(url_for('signin'))

    cart_items = session.get('cart_items', [])
    if not cart_items:
        flash('Your cart is empty.', 'info')
        return render_template('cart.html', cart_items=[], grand_total=0)

    grand_total = 0
    for item in cart_items:
        price = float(item['price'])
        quantity = int(item['quantity'])
        total_item = price * quantity
        grand_total += total_item

    return render_template('cart.html', cart_items=cart_items, grand_total=grand_total)

# Remove from Cart
@app.route('/remove_from_cart/<int:medicine_id>', methods=['POST'])
def remove_from_cart(medicine_id):
    if 'user_id' not in session:
        flash('You must be logged in to modify your cart.', 'danger')
        return redirect(url_for('signin'))

    cart_items = session.get('cart_items', [])
    cart_items = [item for item in cart_items if item['medicine_id'] != medicine_id]
    session['cart_items'] = cart_items

    flash('Item removed from your cart.', 'success')
    return redirect(url_for('cart'))

# Checkout Route
@app.route('/checkout')
def checkout():
    if 'user_id' not in session:
        flash('You must be logged in to proceed to checkout.', 'danger')
        return redirect(url_for('signin'))
    return render_template('checkout.html')

# Process Payment Route
@app.route('/process_payment', methods=['POST'])
def process_payment():
    if 'user_id' not in session:
        flash("Login required to process payment", "danger")
        return redirect(url_for('signin'))

    # Dummy card validation (for demonstration only)
    flash("Payment processed successfully! Your order has been placed.", "success")

    # Clear the cart after payment
    session.pop('cart_items', None)

    return redirect(url_for('orderhistory'))  # Make sure 'orderhistory' is the correct endpoint name

# Order History Route (use 'orderhistory' to match your filename)
@app.route('/orderhistory')
def orderhistory():
    if 'user_id' not in session:
        flash('You must be logged in to view your order history.', 'danger')
        return redirect(url_for('signin'))

    orders = []  # You can implement actual DB fetch logic here
    return render_template('orderhistory.html', orders=orders)

# Feedback Route
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if 'user_id' not in session:
        return redirect(url_for('signin'))

    if request.method == 'POST':
        message = request.form.get('message').strip()  # Strip whitespace
        user_id = session.get('user_id')

        if message:  # If the message is not empty after trimming
            cursor = db.cursor()
            try:
                cursor.execute("INSERT INTO Feedback (user_id, message) VALUES (%s, %s)", (user_id, message))
                db.commit()
                flash('Feedback submitted successfully!', 'success')
            except Exception as e:
                db.rollback()
                print(f"Error inserting feedback: {e}")
                flash('Error submitting feedback.', 'danger')
            finally:
                cursor.close()
            return redirect(url_for('feedback'))
        else:
            flash('Please enter your feedback before submitting.', 'warning')

    return render_template('feedback.html')

# Sign-in Route
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        name = request.form.get('username')  # Use .get() to avoid KeyError
        password = request.form.get('password')

        if not name or not password:
            flash("Username and password are required.", "danger")
            return redirect(url_for('signin'))

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT user_id, password FROM Users WHERE name = %s", (name,))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user and user['password'] == password:
            session['user_id'] = user['user_id']
            flash("Signed in successfully!", "success")
            return redirect(url_for('index'))
        else:
            flash("Invalid username or password.", "danger")
            return redirect(url_for('signin'))

    return render_template('signin.html')

# Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')

        if not name or not password:
            flash('Username and password are required.', 'danger')
            return redirect(url_for('signup'))

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT * FROM Users WHERE name = %s", (name,))
        existing_user = cur.fetchone()
        if existing_user:
            flash('Username already exists. Please choose another one.', 'danger')
            cur.close()
            conn.close()
            return redirect(url_for('signup'))

        cur.execute("INSERT INTO Users (name, password) VALUES (%s, %s)", (name, password))
        conn.commit()
        cur.close()
        conn.close()

        flash('Account created successfully! Please sign in.', 'success')
        return redirect(url_for('signin'))

    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('signin'))



if __name__ == "__main__":
    app.run(debug=True)
