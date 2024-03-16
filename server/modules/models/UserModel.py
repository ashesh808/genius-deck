from sqlalchemy_common import Base, Column, UUID, String, Integer
UniqueIdentifer = UUID(as_uuid=True)

class UserModel(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))

