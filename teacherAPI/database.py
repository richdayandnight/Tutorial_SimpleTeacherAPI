"""
.. module:: database
   :synopsis: Connects to the database and creates teacher table under the Teacher database

.. moduleauthor:: Rich Yap <github.com/richyap13>


"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

# Connect to mysql database
engine = create_engine('mysql://root:password@localhost/Teacher', convert_unicode=True)
metadata = MetaData()

# db_session, used for persistence operation (connection) to the database
db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))

# initialize database (create table)
def init_db():
    """
        **Initialize Database**

        This creates teacher table under the Teacher database.

    """
    import teacherAPI.models
    metadata.create_all(bind=engine)
