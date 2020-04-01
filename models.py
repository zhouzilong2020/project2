from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from werkzeug import generate_password_hash, check_password_hash
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)

    user_id = db.Column(db.String, primary_key = True, unique = True)
    #hash value of password
    password_hash = db.Column(db.String, nullable = False)
    password = None

    #password is transfered into hash value
    def __init__(self, user_id, password):
        #赋值user_id，user_password
        self.user_id = str(user_id)
        self.password = str(password)
        self.validity = 0

    def isAuthorized(self):
        return self.validity

    def set_password(self):
         #save password hash value into class's attribute
         self.password_hash = generate_password_hash(self.password)

    #log in user
    def login(self):
        #判断当前用户是否存在
        try:
            exist_user = User.query.filter_by(user_id = self.user_id).first()
            #当前用户名存在，并且密码匹配
            if exist_user is not None:
                if check_password_hash(exist_user.password_hash, self.password):
                    validity = True
                else: validity = False
            return True
        except:
            return False

    #add a new user
    def addUser(self):
        try:
            #set user unique id in database
            self.set_password()
            db.session.add(self)
            db.session.commit()
            User.count += 1
            return True
        except:
            return False
