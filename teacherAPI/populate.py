"""
.. module:: populate
   :synopsis: Populates database with Teacher Records

.. moduleauthor:: Rich Yap <github.com/richyap13>


"""

from teacherAPI.models import Teacher
from teacherAPI.database import db_session


def populate():
    """
        **Populate Database**

        This populates the teacher table.

    """
    teacher_samp = Teacher(1, 'Jane Vargas', 'Science')
    teacher_samp2 = Teacher(2, 'John Doe', 'Math')
    teacher_samp3 = Teacher(3, 'Jenny Lisa', 'English')
    db_session.add(teacher_samp)
    db_session.add(teacher_samp2)
    db_session.add(teacher_samp3)
    db_session.commit()
