# pylint: disable=E1101
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakerRepo:
    """A simple repository"""

    @classmethod
    def insert_use(cls):
        """Something"""

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Carlos", password="123")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
