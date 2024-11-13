from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://fastspiuser:fastapipass@0.0.0.0:5432/fleamarket"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
# どのデーターベースにどうやって接続するかの設定を保持したオブジェクトを作成

session_local = sessionmaker(auto_commit=False, autoflush=False, bind=engine)
# データベースセッションの作成(データーベース操作の一連の操作をひとまとめにする)

base = declarative_base()