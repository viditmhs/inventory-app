# This is controller tp control User Collections

from dbService import mongoConnect as mc
from models import User

def getUserByEmail(email):
    user = User()
    print("email:" + email)
    u = user.convert(mc().User.find_one({"email" : email}))
    return u
