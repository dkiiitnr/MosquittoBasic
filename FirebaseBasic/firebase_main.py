import pyrebase

firebaseConfig={'apiKey': "AIzaSyCBbaxSdffK3JWapEAL3J9QcbsAU3ogpLU",
    'authDomain'        : "deepak-y20.firebaseapp.com",
    'projectId'         : "deepak-y20",
    'storageBucket'     : "deepak-y20.appspot.com",
    'messagingSenderId' : "112902510651",
    'appId'             : "1:112902510651:web:1d101b93283547aa86e41e",
    'measurementId'     : "G-WMWZ49812L"}

firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()
auth=firebase.storage()