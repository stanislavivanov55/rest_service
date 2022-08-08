from core.config import DATABASE_TYPE

if DATABASE_TYPE == "db":
    from repositories.users import UserRepository
    from db.base import database

    def get_user_repository() -> UserRepository:
        return UserRepository(database)
