from flask import Flask, request, jsonify,session
from flask_mail import Mail, Message
from flask_cors import CORS
import random
import datetime
import sqlite3
import hashlib
import hmac
import os
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
import cloudinary
import cloudinary.api
import cloudinary.uploader
STATIC_SALT = "NO_-@#000"
app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:5173"])
app.secret_key="User0-A-B-X"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'elkhazaansc.customerservices@gmail.com'  
app.config['MAIL_PASSWORD'] = 'xyyu hpoz egsv vygl'  
cloudinary.config( 
    cloud_name = "dmiusn95l", 
    api_key = "786173112484423", 
    api_secret = "twowfhiUAIKvQTJFRKEyKVuVv4Y", 
    secure=True
)
mail = Mail(app) 
app.config['SESSION_TYPE'] = 'filesystem'


def edit_coach(member_id,team_id):
    try:
         conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
         cursor = conn.cursor()
         cursor.execute("""UPDATE Coach SET Member_ID=? WHERE  Team_ID=?  """,(member_id,team_id))
         conn.commit()
         conn.close()
         return True

    except Exception as e:
        print('Error occurred:', e)
        return False

def add_expinses(match_id=None,Traning_id=None,Tprice=0):
    try:
        conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor = conn.cursor()
        if match_id != None :
         cursor.execute("""INSERT INTO Expenses (Match_ID,Tprice) VALUES(?,?)""",(match_id,Tprice))
        elif Traning_id != None:
         cursor.execute("""INSERT INTO Expenses (Traning_ID,Tprice) VALUES(?,?)""",(Traning_id,Tprice))

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print('Error occurred:', e)
        return False
        


def edit_expenses(match_id=None, training_id=None, tprice=0):
    try:
        conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor = conn.cursor()

        if match_id is not None:
            cursor.execute("""UPDATE Expenses SET Tprice = ? WHERE Match_ID = ?""", (tprice, match_id))
        elif training_id is not None:
            cursor.execute("""UPDATE Expenses SET Tprice = ? WHERE Training_ID = ?""", (tprice, training_id))

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print('Error occurred:', e)
        return False

 
def add_coach(member_id,team_id):
    try:
         conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
         cursor = conn.cursor()
         cursor.execute("""INSERT INTO Coach (Member_ID,Team_ID) VALUES(?,?)""",(member_id,team_id))
         conn.commit()
         conn.close()
         return True

    except Exception as e:
        print('Error occurred:', e)
        return False

def edit_player(member_id,Team_id,Teammember_postion,Teammember_status):
    try:
         conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
         cursor = conn.cursor()
         cursor.execute("""UPDATE Teammember SET Team_id=?,Teammember_postion=?,Teammember_status=? WHERE member_ID=?""",(Team_id,Teammember_postion,Teammember_status,member_id))
         conn.commit()
         conn.close()
         return True

    except Exception as e:
        print('Error occurred:', e)
        return False

def add_player(member_id,Team_id,Teammember_postion,Teammember_status):
    try:
         conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
         cursor = conn.cursor()
         cursor.execute("""INSERT INTO Teammember (member_ID,Team_id,Teammember_postion,Teammember_status) VALUES(?,?,?,?)""",(member_id,Team_id,Teammember_postion,Teammember_status))
         conn.commit()
         conn.close()
         return True

    except Exception as e:
        print('Error occurred:', e)
        return False


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

def add_ticket(Match_ID):
    try:
        categories = [
            {"price": 100, "type": "Standard", "start_chairnum": 1, "count": 8500},
            {"price": 300, "type": "VIP", "start_chairnum": 8501, "count": 1000},
            {"price": 700, "type": "Special", "start_chairnum": 9501, "count": 500}
        ]
        Ticket_favteam = 'ElkhazaanSC'
        
        conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor = conn.cursor()
         
        for category in categories:
            Ticket_price = category["price"]
            Ticket_Type = category["type"]
            Ticket_chairnum = category["start_chairnum"]
            print("forloop")
            for _ in range(category["count"]):
                cursor.execute("""
                    INSERT INTO Tickets (Match_ID, Tickets_price, Tickets_type, Tickets_chair_num, Tickets_favTeam)
                    VALUES (?, ?, ?, ?, ?)
                """, (Match_ID, Ticket_price, Ticket_Type, Ticket_chairnum, Ticket_favteam))
                Ticket_chairnum += 1  


        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
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


def subscribe(member_ID,subscribe_id,Subscription_Start_Date,Subscription_END_Date):
    try:
        conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Subscribe (member_ID, subscribe_id, Subscription_Start_Date, Subscription_END_Date)
            VALUES (?, ?, ?, ?)
        """, (member_ID, subscribe_id, Subscription_Start_Date, Subscription_END_Date))

        conn.commit()
        conn.close()
        
        return True

    except Exception as e:
        print('Error occurred:', e)
        return False

otp_storage = {}

def add_purch(payment_id,purch_Date,copon_id,purch_type,purch_Amount,purch_Tprice,serve_id):
    conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
    cursor = conn.cursor()
    if purch_type == 'item':
        cursor.execute("INSERT INTO Purch (Payment_ID, Purch_Date, copon_id, Purch_Type, Purch_Amount, Purch_TPrice, item_ID) VALUES (?,?,?,?,?,?,?)", (payment_id, purch_Date, copon_id, purch_type, purch_Amount, purch_Tprice, serve_id))
        conn.commit()
    elif purch_type == 'Ticket':
        cursor.execute("INSERT INTO Purch (Payment_ID, Purch_Date, copon_id, Purch_Type, Purch_Amount, Purch_TPrice, Ticket_Id) VALUES (?,?,?,?,?,?,?)", (payment_id, purch_Date, copon_id, purch_type, purch_Amount, purch_Tprice, serve_id))
        conn.commit()
    elif purch_type=='Subscription':
        cursor.execute("INSERT INTO Purch (Payment_ID, Purch_Date, copon_id, Purch_Type, Purch_Amount, Purch_TPrice, subscribe_id) VALUES (?,?,?,?,?,?,?)", (payment_id, purch_Date, copon_id, purch_type, purch_Amount, purch_Tprice, serve_id))
        conn.commit()
    conn.close()
    return True
    
def edit_purch(payment_id,purch_Date,copon_id,purch_type,purch_Amount,purch_Tprice,serve_id):
    conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
    cursor = conn.cursor()

    if purch_type == 'item':
        cursor.execute("""
            UPDATE Purch
            SET Purch_Date = ?, copon_id = ?, Purch_Type = ?, Purch_Amount = ?, Purch_TPrice = ?, item_ID = ?
            WHERE Payment_ID = ?
        """, (purch_Date, copon_id, purch_type, purch_Amount, purch_Tprice, serve_id, payment_id))
        conn.commit()
        
    elif purch_type == 'Ticket':
        cursor.execute("""
            UPDATE Purch
            SET Purch_Date = ?, copon_id = ?, Purch_Type = ?, Purch_Amount = ?, Purch_TPrice = ?, Ticket_Id = ?
            WHERE Payment_ID = ?
        """, (purch_Date, copon_id, purch_type, purch_Amount, purch_Tprice, serve_id, payment_id))
        conn.commit()
        
    elif purch_type == 'Subscription':
        cursor.execute("""
            UPDATE Purch
            SET Purch_Date = ?, copon_id = ?, Purch_Type = ?, Purch_Amount = ?, Purch_TPrice = ?, subscribe_id = ?
            WHERE Payment_ID = ?
        """, (purch_Date, copon_id, purch_type, purch_Amount, purch_Tprice, serve_id, payment_id))
        conn.commit()

    conn.close()
    return True

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
            Member_Role,
            Member_status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (user_name, email, hashed_password, number, birth_date, "Member","Active"))
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
        
        match_id=cursor.lastrowid 
        if add_ticket(match_id):
            cursor.execute("""INSERT INTO Match (Match_Date,Match_Start_Time,Match_Stadium,Match_FTeam,Match_STeam,Match_champion) VALUES (?,?,?,?,?,?)""",(match_date,match_start_time,match_stadium,match_FTeam,match_STeam,match_champoin))
            conn.commit()
            conn.close()
            if match_FTeam=='Elkhazzan':
                training_cost = random.randint(1000, 2000)
                equipment_cost = random.randint(500, 1000)
                total_cost = training_cost + equipment_cost
                add_expinses(match_id, total_cost)
            else :
                training_cost = random.randint(2000, 5000)
                equipment_cost = random.randint(500, 1000)
                travel_cost = random.randint(1000, 10000) 
                Tprice = training_cost + equipment_cost + travel_cost
                add_expinses(match_id, Tprice)




            return jsonify({'status': 'Success','message': 'Match added successfully'}),201
        else :
            return jsonify({'status': 'Failed','message': 'Error while adding ticket'}),500
 except Exception as e:
        print('Error occurred:', e)
        return jsonify({'status': 'Failed','message': 'An error occurred. Please try again.'}), 500

@app.route("/api/edit_match", methods=["POST"])
def edit_match():
    data=request.get_json()
    try:
            match_id=data.get('member_id')
            match_date=data.get('match_date')
            match_start_time=data.get('match_time')
            match_stadium=data.get('match_location')
            match_FTeam=data.get('match_team1')
            match_STeam=data.get('match_team2')
            match_champoin=data.get('match_champoin')
            conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
            cursor=conn.cursor()
            
             
            if add_ticket(match_id):
                cursor.execute("""INSERT INTO Match (Match_Date,Match_Start_Time,Match_Stadium,Match_FTeam,Match_STeam,Match_champion) VALUES (?,?,?,?,?,?)""",(match_date,match_start_time,match_stadium,match_FTeam,match_STeam,match_champoin))
                conn.commit()
                conn.close()
                if match_FTeam=='Elkhazzan':
                    training_cost = random.randint(1000, 2000)
                    equipment_cost = random.randint(500, 1000)
                    total_cost = training_cost + equipment_cost
                    edit_expenses(match_id, total_cost)
                else :
                    training_cost = random.randint(2000, 5000)
                    equipment_cost = random.randint(500, 1000)
                    travel_cost = random.randint(1000, 10000) 
                    Tprice = training_cost + equipment_cost + travel_cost
                    edit_expenses(match_id, Tprice)




                return jsonify({'status': 'Success','message': 'Match added successfully'}),201
            else :
                return jsonify({'status': 'Failed','message': 'Error while adding ticket'}),500
    except Exception as e:
            print('Error occurred:', e)
            return jsonify({'status': 'Failed','message': 'An error occurred. Please try again.'}), 500
    
@app.route("/api/Get_match", methods=["GET"])
def get_match():
    data = request.get_json()
    id_ = data.get('id')
    if not id:
        return jsonify({'status': 'Failed', 'message': 'Error sending Data'}), 400
    conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Match WHERE Member_id = ?", (id_,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({
            'status': 'Success',
            'data': {
                'Match_ID': user[0],
                'Match_FTeam': user[1],
                'Match_STeam': user[2],
                'Match_Date': user[3],  
                'Match_champion': user[4],
                'Match_start_time': user[5],
                'Match_stadium': user[6]
            }
        })
    else:
        return jsonify({'status': 'Failed', 'message': 'User not found'}), 404

    
    
@app.route("/api/add_team",methods=['POST'])
def add_team():
    data=request.get_json()
    try:
        
        Team_name=data.get('Team_name')
        Team_type=data.get('Team_type')
    
        conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor=conn.cursor()
        cursor.execute("""INSERT INTO Team (Team_Name,Team_Type) VALUES (?,?)""",(Team_name,Team_type))
        conn.commit()
        conn.close()
        return jsonify({'status': 'Success','message': 'Match added successfully'}),201
    except Exception as e:
        print('Error occurred:', e)
        return jsonify({'status': 'Failed','message': 'An error occurred. Please try again.'}), 500


@app.route("/api/Edit_team",methods=['POST'])
def edit_team():
    data=request.get_json()
    try:
        Team_id=data.get("team_id")
        Team_name=data.get('Team_name')
        Team_type=data.get('Team_type')
    
        conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor=conn.cursor()
        cursor.execute("""
            UPDATE Team
            SET Team_Name = ?, Team_Type = ?
            WHERE Team_ID = ?
        """, (Team_id, Team_type, Team_name))      
        conn.commit()
        conn.close()
        return jsonify({'status': 'Success','message': 'Match added successfully'}),201
    except Exception as e:
        print('Error occurred:', e)
        return jsonify({'status': 'Failed','message': 'An error occurred. Please try again.'}), 500


@app.route("/api/Get_teams",methods=['GET'])
def get_team():
    data = request.get_json()
    id_ = data.get('id')
    if not id:
     return jsonify({'status': 'Failed', 'message': 'Error sending Data'}), 400
    conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Team WHERE Member_id = ?", (id_,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({
            'status': 'Success',
            'data': {
                'Team_ID': user[0],
                'Team_Name': user[1],
                'Team_Type': user[2],
            }
        })
    else:
        return jsonify({'status': 'Failed', 'message': 'User not found'}), 404
 
@app.route("/get_items", methods=['GET'])
def get_items():
    try:
        conn= sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db') 
        cursor = conn.cursor()
            
        cursor.execute('SELECT * FROM Item')
        items = cursor.fetchall()
            
        items_list = []
        for item in items:
            item_dict = {
                'item_id': item[0],
                'item_name': item[1],
                'item_image': item[2],  
                'item_description': item[3],
                'item_type': item[4],
                'item_size': item[5],
                'item_price': item[6],
                'item_offer': item[7],
                'item_colour': item[8]
            }
            items_list.append(item_dict)
        
        return jsonify({'items': items_list}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400
 
    

@app.route("/add_item", methods=['POST'])
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
        item_image = request.files.get('item_image')
        
        
        upload_result = cloudinary.uploader.upload(item_image)
        item_image_url = upload_result.get('secure_url')  
        
        
        if not item_image:
            return jsonify({'status': 'Failed', 'message': 'image are requierd'}), 400
        

        conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO Item (item_name,image_url, Item_description, Item_type, Item_size, Item_price, Item_offer, Item_colour)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (item_name,item_image_url, item_description, item_type, item_size, item_price, item_offer, item_colour))

        conn.commit()
        conn.close()

        return jsonify({'message': 'Item added successfully!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

@app.route("/edit_item", methods=['POST'])
def edit_item():
    data = request.get_json()  
    try:
        item_id=data.get('item_id')
        item_name = data.get('item_name')
        item_description = data.get('item_description')
        item_type = data.get('item_type')
        item_size = data.get('item_size')
        item_price = data['item_price']
        item_offer = data.get('item_offer')
        item_colour = data.get('item_colour')
        item_image = request.files.get('item_image')
        
        
        upload_result = cloudinary.uploader.upload(item_image)
        item_image_url = upload_result.get('secure_url')  
        
        
        if not item_image:
            return jsonify({'status': 'Failed', 'message': 'image are requierd'}), 400
        

        conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor = conn.cursor()

        if item_image:
            cursor.execute('''
                UPDATE Item
                SET item_name = ?, image_url = ?, item_description = ?, item_type = ?, item_size = ?, item_price = ?, item_offer = ?, item_colour = ?
                WHERE item_id = ?
            ''', (item_name, item_image_url, item_description, item_type, item_size, item_price, item_offer, item_colour, item_id))
        conn.commit()
        conn.close()

        return jsonify({'message': 'Item edited successfully!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400

    
@app.route("/api/add_news",methods=['POST'])
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

@app.route("/api/Get_news",methods=['GET'])
def get_news():
    data = request.get_json()
    id_ = data.get('id')
    if not id:
     return jsonify({'status': 'Failed', 'message': 'Error sending Data'}), 400
    conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM News Member_id = ?", (id_,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({
            'status': 'Success',
            'data': {
                'News_ID': user[0],
                'News_imagelink': user[1],
                'News_title': user[2],
                'News_description': user[3], 
            }
        })
    else:
        return jsonify({'status': 'Failed', 'message': 'User not found'}), 404




@app.route("/api/add_sponser",methods=['POST'])
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
    

    
@app.route("/api/Get_sponser",methods=['GET'])
def get_sponsers():
    data = request.get_json()
    id_ = data.get('id')
    if not id:
        return jsonify({'status': 'Failed', 'message': 'Error sending Data'}), 400
    conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Sponsors WHERE Member_id = ?", (id_,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({
            'status': 'Success',
            'data': {
                'Sponsors_ID': user[0],
                'Sponsors_Amount': user[1],
                'Sponsors_name': user[2],
                'Sponsors_expired_date': user[3],  
            }
        })
    else:
        return jsonify({'status': 'Failed', 'message': 'User not found'}), 404



@app.route("/api/add_subscription_plane",methods=['POST'])
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


@app.route("/api/edit_subscription_plane",methods=['POST'])
def edit_subscription_plane():
    data = request.get_json()  
    try:
       Subscription_id=data.get('Subscription_id')
       Subscription_Plan_type=data.get('Subscription_Plan_type')
       Subscription_Amount=data.get('Subscription_Amount')
       Subscription_Name=data.get('Subscription_Name')
                           

       conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
       cursor = conn.cursor()
       cursor.execute("""
            UPDATE Subscription_Plan
            SET Subscription_Plan_type = ?, Subscription_Amount = ?, Subscription_Name = ?
            WHERE Subscription_Plan_ID = ?
        """, (Subscription_Plan_type, Subscription_Amount, Subscription_Name, Subscription_id))

       conn.commit()
       conn.close()

       return jsonify({'message': 'Event added successfully!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/get_sucscription_plane' , methods=['GET'])
def get_subscription_plans():
    data = request.get_json()
    id_ = data.get('id')
    if not id:
        return jsonify({'status': 'Failed', 'message': 'Error sending Data'}), 400
    conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Subscription WHERE Member_id = ?", (id_,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({
            'status': 'Success',
            'data': {
                'Subscription_ID': user[0],
                'Subscription_Plan_type': user[1],
                'Subscription_Amount': user[2],
                'Subscription_Name': user[3],
            }
        })
    else:
        return jsonify({'status': 'Failed', 'message': 'User not found'}), 404





@app.route("/api/add_copon", methods=['POST'])
def add_copon():
    data = request.get_json()  
    try:
       Copon_Code=data.get('Copon_Disscount')
       Copon_Disscount=data.get('Copon_Disscount')
       Copon_timeofuses=data.get('Copon_timeofuses')
       
                           

       conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
       cursor = conn.cursor()
       cursor.execute("""INSERT INTO Copon (Copon_Code, Copon_Disscount, Copon_timeofuses) VALUES (?,?,?)""",(Copon_Code,Copon_Disscount,Copon_timeofuses))

       conn.commit()
       conn.close()

       return jsonify({'message': 'Event added successfully!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route("/api/Check_copon",methods=[ "POST"])
def check_copon():
    data=request.get_json()
    try:   
        copone_code=data['copone_code']
        conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM Copon WHERE Copon_Code =?", (copone_code,))
        result=cursor.fetchone()
        Nnumberofuses=result[2]-1
        if result and result[2]>0:
            cursor.execute("""UPDATE Copon SET Copon_timeofuses = ? WHERE Copon_ID = ?""",(Nnumberofuses,result[0]) )
            conn.commit()
            conn.close()
            return jsonify({'status': 'Success', 'data': {'discount' : result[1]}}), 200 
        
            
        else :
            conn.close()
            return jsonify({'status': 'Failed', 'data': 'Your copon dose not has Exist or Expierd '}), 404
        

    except Exception as e:
        return jsonify({'status': 'Failed', 'message': 'An error occurred. Please try again.'}), 500

@app.route("/api/add_payment",methods=['POST'])
def add_payment():
    data = request.get_json()  
    try:
       
       member_ID=data.get('member_ID')
       member_Address=data.get('member_Address')
       payment_type=data.get('payment_type')
       purch_Date=data.get('purch_Date')
       purch_type=data.get('purch_Type')
       copon_id=data.get('copon_id', None)
       purch_Amount=data.get('purch_Amount')
       purch_Tprice=data.get('purch_Tprice')
       item_ID=data.get('item_ID',None)
       Ticket_Id=data.get('ticket_Id',None)
       subscribe_id=data.get('subscribe_id',None)
       Subscription_Start_Date=data.get('Subscription_Start_Date')
       Subscription_END_Date=data.get('Subscription_END_Date')

       if not all([member_ID, member_Address, payment_type, purch_Date, purch_type, purch_Amount, purch_Tprice]):
            return jsonify({'status': 'Failed', 'message': 'Missing required fields'}), 400
       conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
       cursor = conn.cursor()
       cursor.execute("""INSERT INTO Payment (member_ID, member_Address, payment_type) VALUES (?,?,?)""",(member_ID,member_Address,payment_type))
       conn.commit()
       payment_id = cursor.lastrowid
       
       if item_ID or Ticket_Id or subscribe_id:
            serve_id = item_ID or Ticket_Id or subscribe_id  
            if subscribe_id:
                subscribe(member_ID,subscribe_id,Subscription_Start_Date,Subscription_END_Date)
            if add_purch(payment_id,purch_Date,copon_id,purch_type,purch_Amount,purch_Tprice,serve_id):
                conn.close()
                return jsonify({'status': 'Success', 'message': 'Purchase added successfully!'}), 200
            
       else:
            conn.close()
            return jsonify({'status': 'Failed', 'message': 'serv_id  required'}), 400
       
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route("/api/edit_payment",methods=['POST'])
def edit_payment():
   
    data = request.get_json()  
    try:
       payment_id=data.get('payment_id')
       member_ID=data.get('member_ID')
       member_Address=data.get('member_Address')
       payment_type=data.get('payment_type')
       purch_Date=data.get('purch_Date')
       purch_type=data.get('purch_Type')
       copon_id=data.get('copon_id', None)
       purch_Amount=data.get('purch_Amount')
       purch_Tprice=data.get('purch_Tprice')
       item_ID=data.get('item_ID',None)
       Ticket_Id=data.get('ticket_Id',None)
       subscribe_id=data.get('subscribe_id',None)
       Subscription_Start_Date=data.get('Subscription_Start_Date')
       Subscription_END_Date=data.get('Subscription_END_Date')

       if not all([member_ID, member_Address, payment_type, purch_Date, purch_type, purch_Amount, purch_Tprice]):
            return jsonify({'status': 'Failed', 'message': 'Missing required fields'}), 400
       conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
       cursor = conn.cursor()
       cursor.execute("""
           UPDATE Payment
           SET member_ID = ?, member_Address = ?, payment_type = ?
           WHERE payment_id = ?
       """, (member_ID, member_Address, payment_type, payment_id))
       conn.commit()
       
       if item_ID or Ticket_Id or subscribe_id:
            serve_id = item_ID or Ticket_Id or subscribe_id  
            if subscribe_id:
                subscribe(member_ID,subscribe_id,Subscription_Start_Date,Subscription_END_Date)
            if add_purch(payment_id,purch_Date,copon_id,purch_type,purch_Amount,purch_Tprice,serve_id):
                conn.close()
                return jsonify({'status': 'Success', 'message': 'Purchase added successfully!'}), 200
            
       else:
            conn.close()
            return jsonify({'status': 'Failed', 'message': 'serv_id  required'}), 400
       
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
@app.route("/api/Get_UserData", methods=['POST', 'GET'])
def get_user_data():
    data = request.get_json()
    id_ = data.get('id')
    if not id:
        return jsonify({'status': 'Failed', 'message': 'Error sending Data'}), 400
    conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Member WHERE Member_id = ?", (id_,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({
            'status': 'Success',
            'data': {
                'Member_ID': user[0],
                'Member_Name': user[1],
                'Member_Email': user[2],
                'Member_phoneNumber': user[4],  
                'Member_BirthDate': user[5],
                'Member_subscription_status': user[6],
                'Member_Role': user[7]
            }
        })
    else:
        return jsonify({'status': 'Failed', 'message': 'User not found'}), 404


@app.route("/api/EditUserData", methods=['POST'])
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


@app.route("/api/add_match_plan", methods=["POST"])
def add_match_plan():
    data = request.get_json()
    match_id=data.get('id')
    match_plan=data.get('match_plan')
    conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Match (match_plan) VALUES (?) where Match_ID=?""",(match_plan,match_id))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Success', 'message': 'Match plan added Successfully'})

@app.route("/api/bann_person", methods=["POST"])
def bann_person():
    data=request.get_json()
    try:
        member_id = data.get('member_id')
        conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor=conn.cursor()
        cursor.execute("""
            UPDATE Members
            SET member_status = 'inactive'
            WHERE member_id = ?
        """, (member_id,))

        conn.commit()
        conn.close()
        return jsonify({'status': 'Success', 'message': 'Member status updated to inactive'}), 200

    except Exception as e:
        print("Error occurred during banning member:", e)
        return jsonify({'status': 'Failed', 'message': 'An error occurred. Please try again.'}), 500

@app.route("/api/edit_match_plan", methods=["POST"])
def edit_match_plan():


    data = request.get_json()
    match_id=data.get('id')
    match_plan=data.get('match_plan')
    conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
    cursor = conn.cursor()
    cursor.execute("""UPDATE Match SET Match_plan=? WHERE Match_ID""",(match_plan,match_id))
    conn.commit()
    conn.close()
    return jsonify({'status': 'Success', 'message': 'Match plan updated Successfully'})



@app.route("/api/Get_match_plan", methods=["GET", "POST"])
def get_matchplane():
    pass


@app.route('/add_training', methods=['POST'])
def add_training():
    data = request.get_json()
    try:
        team_id=data.get('team_id')
        coach_id=data.get('coach_id')
        training_date=data.get('training_date') 
        start_date=data.get('start_date')
        end_date=data.get('end_date')
        conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor = conn.cursor()
        print("sucsses")
        cursor.execute("""INSERT INTO Training 
                       (Team_id,
                       coach_id,
                       Traning_Date ,
                       Training_Start_time,
                       Training_End_time)
                       VALUES (?,?,?,?,?)"""
                       ,(team_id,coach_id,training_date,start_date, end_date))
        conn.commit()
        conn.close()
        train_id=cursor.lastrowid
        traning_cost=random.randint(200,800)
        equipments=random.randint(250,500)
        Tprice=traning_cost+equipments
        add_expinses(None,train_id,Tprice)
        return jsonify({'status': 'Success', 'message': 'Training added Successfully'}),201
    except Exception as e:
        print("Error occurred during add training:", e)
        return jsonify({'status': 'Failed', 'message': 'An error occurred. Please try again.'}), 500


@app.route('/edit_training', methods=['POST'])
def edit_traning():
    data = request.get_json()
    try:
        train_id=data.get('train_id')
        team_id=data.get('team_id')
        coach_id=data.get('coach_id')
        training_date=data.get('training_date') 
        start_date=data.get('start_date')
        end_date=data.get('end_date')
        conn=sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor = conn.cursor()
        print("sucsses")
        cursor.execute("""
            UPDATE Training
            SET Team_id = ?, coach_id = ?, Traning_Date = ?, Training_Start_time = ?, Training_End_time = ?
            WHERE Training_ID = ?
        """, (team_id, coach_id, training_date, start_date, end_date, train_id))
        conn.commit()
        conn.commit()
        conn.close()
        traning_cost=random.randint(200,800)
        equipments=random.randint(250,500)
        Tprice=traning_cost+equipments
        add_expinses(None,train_id,Tprice)
        return jsonify({'status': 'Success', 'message': 'Training added Successfully'}),201
    except Exception as e:
        print("Error occurred during add training:", e)
        return jsonify({'status': 'Failed', 'message': 'An error occurred. Please try again.'}), 500


@app.route('/api/get_training', methods=['GET'])
def get_traning():
    pass



@app.route('/api/add_person',methods=["POST"])
def add_person():
    try:
        data = request.get_json()
        user_name = data.get('userName')
        number = data.get('number')
        birth_date = data.get('birthDate')
        email = data.get('email')
        password = data.get('password')
        hashed_password = hashing(password)
        member_role=data.get('Role')
        Team_id=data.get('team_id',None)
        Teammember_postion=data.get('Teammember_postion',None)
        Teammember_status=data.get('Teammember_status',None) 
        
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
            Member_Role,
            Member_status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (user_name, email, hashed_password, number, birth_date, member_role,"Active"))
        member_id=cursor.lastrowid
        conn.commit()
        conn.close()


        if member_role=='Player' :
            
            if(add_player(member_id,Team_id,Teammember_postion,Teammember_status)):
               return jsonify({'status': 'Success', 'message': 'Player added Successful'}), 201
            else:
               return jsonify({'status': 'Failed', 'message': 'An error occurred while adding player. Please try again.'}), 500
        if member_role=='coach' :
            
            if(add_coach(member_id,Team_id)):
               return jsonify({'status': 'Success', 'message': 'Coach added Successful'}), 201
            else:
               return jsonify({'status': 'Failed', 'message': 'An error occurred while adding coach. Please try again.'}), 500


        
        else:
         return jsonify({'status': 'Success', 'message': 'Member added Successful'}), 201

    except Exception as e:
        print("Error occurred during sign-up:", e)
        return jsonify({'status': 'Failed', 'message': 'An error occurred. Please try again.'}), 500



@app.route('/api/edit_person_data',methods=["POST"])
def edit_person_data():
    data=request.get_json()
    try:
        member_id = data.get('member_id')
        user_name = data.get('userName')
        number = data.get('number')
        birth_date = data.get('birthDate')
        email = data.get('email')
        member_role=data.get('Role')
        member_status=data.get('member_status',"Active")
        Team_id=data.get('team_id',None)
        Teammember_postion=data.get('Teammember_postion',None)
        Teammember_status=data.get('Teammember_status',None) 
        conn = sqlite3.connect(r'C:\YD.Project\sport-club-system-main\Data base\sports_management.db')
        cursor = conn.cursor()
        
        
        cursor.execute("""
            UPDATE Member SET
            Member_Name=?,
            Member_Email=?,
            Member_phone=?,
            Member_BirthDate=?,
            Member_Role=?,
            Member_status=?
            WHERE Member_ID=? 
        """,
        (user_name, email, number, birth_date, member_role,member_status,member_id))

        conn.commit()
        conn.close()
        if member_role=='Player' and Team_id:
            if edit_player(member_id,Team_id,Teammember_postion,Teammember_status):
              return jsonify({'status': 'Success', 'message': 'Player edited Successfully'}), 201
            else:
               return jsonify({'status': 'Failed', 'message': 'An error occurred while Editing Player. Please try again.'}), 500

        if member_role=='coach' and Team_id :
        
            if edit_coach(member_id,Team_id):
                return jsonify({'status': 'Success', 'message': 'Coach Edited Successfully'}), 201
        else:
            return jsonify({'status': 'Failed', 'message': 'An error occurred while Editing coach. Please try again.'}), 500

        return jsonify({'status': 'Success', 'message': 'Data Edited Successfully'}), 201

    except Exception as e:
        print("Error occurred during sign-up:", e)
        return jsonify({'status': 'Failed', 'message': 'An error occurred. Please try again.'}), 500


@app.route('/')
def home():
    return "API is working"


if __name__ == '__main__':
    app.run(debug=True)
