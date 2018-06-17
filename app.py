"""A simple teacher API

.. moduleauthor:: Rich Yap <github.com/richyap13>

"""

from flask import Flask
from teacherAPI.controller import teacher_api


def create_app(config=None):
    """
        **Create application**

        This creates an instance of the TeacherAPI and runs it

    """
    app = Flask(__name__)
    app.register_blueprint(teacher_api)
    app.run()


create_app()

