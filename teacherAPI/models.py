"""
.. module:: models
   :synopsis: Contains model of a Teacher Record

.. moduleauthor:: Rich Yap <github.com/richyap13>


"""

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from teacherAPI.database import metadata, db_session


# class Teacher defining each column in our company table
class Teacher(object):
    """This class is the model of a Teacher record.
    """
    query = db_session.query_property()

    def __init__(self, id=None, name=None, subject=None):
        self.id = id
        self.name = name
        self.subject = subject

    def __repr__(self):
        return '<Teacher %r %r %r>' % (self.id, self.name, self.subject)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'subject': self.subject
        }


# Metadata of the teacher table
teacher = Table('teacher', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String(120), unique=True, nullable=False),
                Column('subject', String(120)))

# Map the teacher metadata to the class Teacher
mapper(Teacher, teacher)