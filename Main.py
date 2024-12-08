from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
import random
import datetime
import sqlite3
import hashlib
import hmac
STATIC_SALT = "NO_-@#000"
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'elkhazaansc.customerservices@gmail.com'  
app.config['MAIL_PASSWORD'] = 'xyyu hpoz egsv vygl'  

mail = Mail(app) 
CORS(app)


def signup_check(email):

    conn = sqlite3.connect(r'C:\YD.Project\Data base\SYS.db')
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM Member WHERE Member_Email = ?", (email,))
    user = cursor.fetchone()
    if user :
        return True
    conn.close() 


def login_check(email, password):

    conn = sqlite3.connect(r'C:\YD.Project\Data base\SYS.db')
    cursor = conn.cursor()

    # Retrieve the hashed password from the database
    cursor.execute("SELECT * FROM Member WHERE Member_Email = ?", (email,))
    user = cursor.fetchone()
    conn.close()

    if user:
        stored_hashed_password = user[3]  
       
        hashed_password = password

       
        if hashed_password == stored_hashed_password:
            return True

    return False


def hashing(password):
    salt=STATIC_SALT
    salt_bytes = salt.encode('utf-8')
    password_bytes = password.encode('utf-8')
    hashed_password = hmac.new(salt_bytes, password_bytes, hashlib.sha256).hexdigest()
    return hashed_password


def send_otp(email, otp_code):       
    try:
        msg = Message(
            "Your OTP Code",
            sender=app.config['MAIL_USERNAME'],
            recipients=[email]
        )
        msg.body = f"Your OTP code is: {otp_code}. It is valid for 2 minutes."
        mail.send(msg)
        return True
    except Exception as e:
        print("Failed to send email:")
        print(e)  
        return False   


otp_storage = {}



@app.route('/api/request-otp', methods=['POST'])
def request_otp():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"status": "Error", "message": "Email is required."}), 400
    if not signup_check(email):
         return jsonify({"status": "Error", "message": "Email is not registered."}), 400
        
    
    otp_code = f"{random.randint(100000, 999999)}"
    otp_storage[email] = {
        "otp_code": otp_code,
        "timestamp": datetime.datetime.now(datetime.timezone.utc)
    }

    if send_otp(email, otp_code):
        return jsonify({"status": "Success", "message": "OTP sent successfully."})
    else:
        return jsonify({"status": "Error", "message": "Failed to send OTP. Try again."}), 500


@app.route('/api/verify-otp', methods=['POST'])
def verify_otp():
    data = request.get_json()
    email = data.get('email')
    otp_code = data.get('otpCode')

    if not email or not otp_code:
        return jsonify({"status": "Error", "message": "Email and OTP code are required."}), 400

    if email in otp_storage:
        stored_otp = otp_storage[email]
      
        if (datetime.datetime.now(datetime.timezone.utc) - stored_otp['timestamp']).total_seconds() > 120:
            otp_storage.pop(email)
            return jsonify({"status": "Error", "message": "OTP has expired. Please request a new one."}), 400

        if stored_otp['otp_code'] == otp_code:
            otp_storage.pop(email)
            return jsonify({"status": "Success", "message": "OTP verified successfully."})
        else:
            return jsonify({"status": "Error", "message": "Invalid OTP."}), 400

    return jsonify({"status": "Error", "message": "No OTP found for this email."}), 400



@app.route("/api/signup", methods=["POST"])
def sign_up():
    
    try:
        data = request.get_json()
        user_name = data.get('userName')
        number = data.get('number')
        birth_date = data.get('birthDate')
        email = data.get('email')
        password = data.get('password')
        plan = data.get('plan')
        plan= "NONE"
        hashed_password = hashing(password)
        if signup_check(email):
          return jsonify({"status": "Error", "message": "Email is already exist."}), 500
            
            
        conn = sqlite3.connect(r'C:\YD.Project\Data base\SYS.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Member (
            Member_Name,
            Member_Email,
            Member_Password,
            Member_phoneNumber,
            Member_BirthDate,
            Member_subscription_status,
            Member_Role)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (user_name, email, hashed_password, number, birth_date,plan, "Member"))
        conn.commit()
        conn.close()

        if email in otp_storage:
            del otp_storage[email]

        return jsonify({'status': 'Success', 'message': 'Registration Successful'}), 201

    except Exception as e:
        print("Error occurred during sign-up:", e)
        return jsonify({'status': 'Failed', 'message': 'An error occurred. Please try again.'}), 500



@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json() 
        email = data.get('username')
        password = data.get('Password')

        if not email or not password:
            return jsonify({'status': 'Failed', 'message': 'Email and password are required'}), 400

   
        status = login_check(email, hashing(password))

        if status:
            return jsonify({'status': 'Success', 'message': 'Login Successful'}), 200
        else:
            return jsonify({'status': 'Failed', 'message': 'Invalid Email or Password'}), 401

    except Exception as e:
        import traceback
        print("Error occurred:")
        print(traceback.format_exc())  
        return jsonify({'status': 'Failed', 'message': 'An error occurred. Please try again.'}), 500
@app.route('/api/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    email = data.get('email')
    otp_code = data.get('otpCode')
    new_password = data.get('password')

    if not email or not otp_code or not new_password:
        return jsonify({"status": "Error", "message": "All fields are required."}), 400

    if email not in otp_storage:
        return jsonify({"status": "Error", "message": "No OTP found for this email."}), 400

    stored_otp = otp_storage[email]
    if (datetime.datetime.now(datetime.timezone.utc) - stored_otp['timestamp']).total_seconds() > 120:
        otp_storage.pop(email)
        return jsonify({"status": "Error", "message": "OTP has expired. Please request a new one."}), 400

    if stored_otp['otp_code'] != otp_code:
        return jsonify({"status": "Error", "message": "Invalid OTP."}), 400

    conn = sqlite3.connect(r'C:\YD.Project\Data base\SYS.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Member SET Member_Password = ? WHERE Member_Email = ?", (hashing(new_password), email))
    conn.commit()
    conn.close()

    otp_storage.pop(email)
    return jsonify({"status": "Success", "message": "Password reset successfully."})



@app.route('/')
def home():
    return "API is working"


if __name__ == '__main__':
    app.run(debug=True)
