# Database modelの定義
from sqlalchemy import Column, Integer, String, DateTime
from models.database import Base
from datetime import datetime


# テーブルは、Baseを継承したクラスで定義
class MemberContent(Base):
    __tablename__ = 'membercontent'
    # 複合ユニーク制約
    #__table_args__ = (UniqueConstraint('name','email'),{})
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    email = Column(String(257), unique=True)
    birthday = Column(DateTime)

    def __init__(self, name=None, email=None, birthday=None):
        self.name = name
        self.email = email
        self.birthday = birthday

    def __repr__(self):
        return 'id:{}, name:{}, emali:{}, birthday:{}'.format(self.id, self.name, self.email, self.birthday)