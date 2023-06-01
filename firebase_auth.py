import pyrebase
from getpass import getpass

firebaseConfig = {
    'apiKey': "AIzaSyA7E5PuXAsTlI0lkrsA5NDknJgOD0Bvofw",
    'authDomain': "gpt-venv-cacao.firebaseapp.com",
    'projectId': "gpt-venv-cacao",
    'storageBucket': "gpt-venv-cacao.appspot.com",
    'messagingSenderId': "799252985573",
    'appId': "1:799252985573:web:904d97a71eab919e62060c",
    'measurementId': "G-DJDVKJD269",
    'serviceAccount': '../gpt_venv/assets/gpt-venv-cacao-559d6ada3d0b.json'
}

firebase=pyrebase.initialize_app(firebaseConfig)
authentication=firebase.auth()