from datetime import datetime
from sqlalchemy import Column, Integer, String, Enum, DateTime
from database import Base
# モデルの基底クラスのbaseのインポート
from schemas import ItemStatus

# Railsのモデルファイルの様な役割をする
class Item(Base):
  __tablename__ = "items"

  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False) # nullを許容しない
  price = Column(Integer, nullable=False)
  description = Column(String, nullable=True)
  status = Column(Enum(ItemStatus), nullable=False, default=ItemStatus.ON_SALE)
  created_at = Column(DateTime, default=datetime.now())
  updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
