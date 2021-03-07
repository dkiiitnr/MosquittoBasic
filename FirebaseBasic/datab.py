import pyrebase
firebaseConfig = {
    "apiKey": "AIzaSyBXaDH7xSNkteQryv5n2GK7oD-hDgGdlyA",
    "authDomain": "testtrolley-ee578.firebaseapp.com",
    "databaseURL": "https://testtrolley-ee578-default-rtdb.firebaseio.com",
    "projectId": "testtrolley-ee578",
    "storageBucket": "testtrolley-ee578.appspot.com",
    "messagingSenderId": "1097697149394",
    "appId": "1:1097697149394:web:f9f2ddf9ac1028df75480b",
    "measurementId": "G-EP9YNN19BR"
  }

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
email = input("Enter your email : \n")
password = input("Enter your password: \n")
user = auth.create_user_with_email_and_password(email,password)
#in order to verify
#user = auth.sign_in_with_email_and_password(email,password)
print("user created successfully")
