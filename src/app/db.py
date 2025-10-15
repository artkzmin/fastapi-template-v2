from infra.db import session_maker
from persistence.utils import DBManager as PersistenceDBManager


class DBManager(PersistenceDBManager):
    pass


def get_db_manager() -> DBManager:
    return DBManager(session_factory=session_maker)
