#src/model_struc/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from .BlogpostModel import BlogpostSchema, BlogpostModel
from .UserModel import UserSchema, UserModel

# initialize our db
db = SQLAlchemy()

#######
# existing code remains #
#######
bcrypt = Bcrypt()