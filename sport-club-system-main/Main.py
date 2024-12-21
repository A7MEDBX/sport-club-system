from flask import Flask, request, jsonify,session
from flask_mail import Mail, Message
from flask_cors import CORS
import random
import datetime
import sqlite3
import hashlib
import hmac
import os
STATIC_SALT = "NO_-@#000"
app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:5173"])
app.secret_key="User0-A-B-X"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'elkhazaansc.customerservices@gmail.com'  
app.config['MAIL_PASSWORD'] = 'xyyu hpoz egsv vygl'  

mail = Mail(app) 
app.config['SESSION_TYPE'] = 'filesystem'


def signup_check(email):

    conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM Member WHERE Member_Email = ?", (email,))
    user = cursor.fetchone()
    if user :
        return True
    conn.close() 


def login_check(email, password):
    conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM Member WHERE Member_Email = ?", (email,))
        user = cursor.fetchone()

        if user:
            stored_hashed_password = user[3]  
             
            hashed_password = password
            if hashed_password == stored_hashed_password:
                return True
        return False
    except Exception as e:
        
        return False
    finally:
        conn.close()


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
    resetpassstatus = data.get('resetpass',False)
    if resetpassstatus and not  signup_check(email):
       return jsonify({"status": "Error", "message": "Email not found. Cannot reset password."}), 404
    else:
        if not resetpassstatus and signup_check(email):
           return jsonify({"status": "Error", "message": "Email already registered."}), 400
        
    
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
        hashed_password = hashing(password)
        if signup_check(email):
          return jsonify({"status": "Error", "message": "Email is already exist."}), 500
            
            
        conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Member (
            Member_Name,
            Member_Email,
            Member_Password,
            Member_phone,
            Member_BirthDate,
            Member_Role)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
        (user_name, email, hashed_password, number, birth_date, "Member"))
        conn.commit()
        conn.close()

        if email in otp_storage:
            del otp_storage[email]

        return jsonify({'status': 'Success', 'message': 'Registration Successful'}), 201

    except Exception as e:
        print("Error occurred during sign-up:", e)
        return jsonify({'status': 'Failed', 'message': 'An error occurred. Please try again.'}), 500



@app.route("/api/add_match", methods=["POST"])
def add_match():
 data=request.get_json()
 try:
     match_date=data.get('match_date')
     match_start_time=data.get('match_time')
     match_stadium=data.get('match_location')
     match_FTeam=data.get('match_team1')
     match_STeam=data.get('match_team2')
     match_champoin=data.get('match_champoin')
     conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
     cursor=conn.cursor()
     cursor.execute("""INSERT INTO Match (Match_Date,Match_Start_Time,Match_Stadium,Match_FTeam,Match_STeam,Match_champion) VALUES (?,?,?,?,?,?)""",(match_date,match_start_time,match_stadium,match_FTeam,match_STeam,match_champoin))
     conn.commit()
     conn.close() 
     return jsonify({'status': 'Success','message': 'Match added successfully'}),201
 except Exception as e:
     print('Error occurred:', e)
     return jsonify({'status': 'Failed','message': 'An error occurred. Please try again.'}), 500
    
    
@app.route('api/add_team',methods=['POST'])
def add_team():
    data=request.get_json()
    try:
        
        Team_name=data('Team_name')
        Team_type=data('Team_type')
    
        conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor=conn.cursor()
        cursor.execute("""INSERT INTO Team (Team_Name,Team_Type) VALUES (?,?)""",(Team_name,Team_type))
        conn.commit()
        conn.close()
        return jsonify({'status': 'Success','message': 'Match added successfully'}),201
    except Exception as e:
        print('Error occurred:', e)
        return jsonify({'status': 'Failed','message': 'An error occurred. Please try again.'}), 500
    
    
    

@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.get_json()  
    try:
       
        item_name = data.get('item_name')
        item_description = data.get('item_description')
        item_type = data.get('item_type')
        item_size = data.get('item_size')
        item_price = data['item_price']
        item_offer = data.get('item_offer')
        item_colour = data.get('item_colour')

        conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Item (item_name, Item_description, Item_type, Item_size, Item_price, Item_offer, Item_colour)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (item_name, item_description, item_type, item_size, item_price, item_offer, item_colour))

        conn.commit()
        conn.close()

        return jsonify({'message': 'Item added successfully!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    
    
@app.route('api/add_news',methods=['POST'])
def add_news():
    data = request.get_json()  
    try:
       
       news_title=data.get('title')
       news_description=data.get('description')
       news_image=data.get('image_url')
                           

       conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
       cursor = conn.cursor()
       cursor.execute("""INSERT INTO News (News_title, News_description, News_imagelink) VALUES (?,?,?)""",(news_title,news_description,news_image))

 

       conn.commit()
       conn.close()

       return jsonify({'message': 'Event added successfully!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400



@app.route('/api/add_sponser',methods=['POST'])
def add_sponser():
    data = request.get_json()  
    try:
       
       Sponsors_name=data.get('Sponsors_name')
       Sponsorship_Amount=data.get('Sponsorship_Amount')
       Sponsors_expired_date=data.get('Sponsors_expired_date')
                           

       conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
       cursor = conn.cursor()
       cursor.execute("""INSERT INTO Sponsors (Sponsors_name, Sponsorship_Amount, Sponsors_expired_date) VALUES (?,?,?)""",(Sponsors_name,Sponsorship_Amount,Sponsors_expired_date))
 

       conn.commit()
       conn.close()

       return jsonify({'message': 'Event added successfully!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.rourte('/api/add_subscription_plane',methods=['POST'])
def add_subscription_plane():
    data = request.get_json()  
    try:
       
       Subscription_Plan_type=data.get('Subscription_Plan_type')
       Subscription_Amount=data.get('Subscription_Amount')
       Subscription_Name=data.get('Subscription_Name')
                           

       conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
       cursor = conn.cursor()
       cursor.execute("""INSERT INTO Subscription_Plan (Subscription_Plan_type, Subscription_Amount, Subscription_Name) VALUES (?,?,?)""",(Subscription_Plan_type,Subscription_Amount,Subscription_Name))

       conn.commit()
       conn.close()

       return jsonify({'message': 'Event added successfully!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/api/add_copon', methods=['POST'])
def add_copon():
    data = request.get_json()  
    try:
       
       Copon_Disscount=data.get('Copon_Disscount')
       Copon_timeofuses=data.get('Copon_timeofuses')
       
                           

       conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
       cursor = conn.cursor()
       cursor.execute("""INSERT INTO Copon (Copon_Disscount, Copon_timeofuses) VALUES (?,?)""",(Copon_Disscount,Copon_timeofuses))

       conn.commit()
       conn.close()

       return jsonify({'message': 'Event added successfully!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
    
@app.route('/api/UserData', methods=['POST'])
def get_user_data():
    data = request.get_json()
    id = data.get('id')
    if not id:
        return jsonify({'status': 'Failed', 'message': 'Error sending Data'}), 400
    conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Member WHERE Member_id = ?", (id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({
            'status': 'Success',
            'data': {
                'Member_ID': user[0],
                'Member_Name': user[1],
                'Member_Email': user[2],
                'Member_phoneNumber': user[4],  # Adjust indices based on schema
                'Member_BirthDate': user[5],
                'Member_subscription_status': user[6],
                'Member_Role': user[7]
            }
        })
    else:
        return jsonify({'status': 'Failed', 'message': 'User not found'}), 404


@app.route('/api/EditUserData', methods=['POST'])
def edit_user_data():
    data=request.get_json()
    user_id = data.get('id')
    user_name = data.get('userName')
    number = data.get('number')
    address=data.get('address')
    conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
    cursor=conn.cursor()
    cursor.execute("UPDATE Member SET Member_Name =?, Member_phoneNumber =?,member_Address =? WHERE Member_ID =?", (user_name, number,address, user_id))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Success', 'message': 'Data Updated Successfully'})
   




@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('username')
        password = data.get('Password')

        if not email or not password:
            return jsonify({'status': 'Failed', 'message': 'Email and password are required'}), 400

        hashed_password = hashing(password)
        if login_check(email, hashed_password):
            conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
            cursor = conn.cursor()
            cursor.execute("""
                SELECT Member_ID, Member_Name, Member_Role 
                FROM Member WHERE Member_Email = ?
            """, (email,))
            user = cursor.fetchone()
            conn.close()

            if user:
                member_id, member_name, member_role = user
                session['user_id'] = member_id
                session['user_name'] = member_name
                session['user_role'] = member_role
                return jsonify({
                    'status': 'Success',
                    'message': 'Login Successful',
                    'data': {
                        'Member_ID': member_id,
                        'Member_Name': member_name,
                        'Member_Role': member_role
                    }
                }), 200
            else:
                return jsonify({'status': 'Failed', 'message': 'User data retrieval failed'}), 500

        return jsonify({'status': 'Failed', 'message': 'Invalid Email or Password'}), 401

    except Exception as e:
        print("Error occurred during login:", e)
        return jsonify({'status': 'Failed', 'message': 'An error occurred. Please try again.'}), 500



@app.route('/api/logout', methods=['POST'])
def logout():
    try:
        session.pop('user_id', None)
        session.pop('user_name', None)
        session.pop('user_role', None)
        return jsonify({'status': 'Success', 'message': 'Logged out successfully.'}), 200
    except Exception as e:
        print("Error during logout:", e)
        return jsonify({'status': 'Failed', 'message': 'An error occurred during logout.'}), 500



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

    conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
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
