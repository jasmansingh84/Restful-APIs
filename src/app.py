# # # src/app.py
# #
# # from flask import Flask
# #
# # from .config import app_config
# # from .model_struc import db, bcrypt
# #
# # # import user_api blueprint
# # from .Views.UserView import user_api as user_blueprint
# # from .Views.BlogpostView import blogpost_api as blogpost_blueprint
# #
# #
# # def create_app(env_name):
# #     """
# #     Create app
# #     """
# #
# #     # app initiliazation
# #     app = Flask(__name__)
# #
# #     app.config.from_object(app_config[env_name])
# #
# #     # initializing bcrypt and db
# #     bcrypt.init_app(app)
# #     db.init_app(app)
# #
# #     # app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
# #     # app.register_blueprint(blogpost_blueprint, url_prefix='/api/v1/blogposts')
# #
# #     @app.route('/', methods=['GET'])
# #     def index():
# #         """
# #         example endpoint
# #         """
# #         return 'Congratulations! Your part 2 endpoint is working'
# #
#     return app

#2
# src/app.py

from flask import Flask

from .config import app_config


# def create_app(env_name):
#     """
#     Create app
#     """
#
#     # app initiliazation
#     app = Flask(__name__)
#
#     app.config.from_object(app_config[env_name])
#
#     @app.route('/', methods=['GET'])
#     def index():

    #     return 'Congratulations! Your first endpoint is workin'
    #
    # return app


# src/app.py

# from .model_struc import db, bcrypt  # add this new line
#
# def create_app(env_name):
#     """
#     Create app
#     """
#
#     # app initiliazation
#     app = Flask(__name__)
#
#     app.config.from_object(app_config[env_name])
#
#     # initializing bcrypt
#     bcrypt.init_app(app)  # add this line
#
#     db.init_app(app)  # add this line
#
#
#
#     return app

#3

from flask import Flask

from .config import app_config
from .model_struc import db, bcrypt
from .Views.UserView import user_api as user_blueprint


def create_app(env_name):
    # app init


    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    bcrypt.init_app(app)

    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')

    @app.route('/', methods=['GET'])
    def index():
        """
        test endpoint
        """
        return 'Congratulations! Your first endpoint is working'

    return app

