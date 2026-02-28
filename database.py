from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Tạo đường dẫn database (file sqlite sẽ tự sinh ra)
DATABASE_URL = "sqlite:///./blog_app.db"

# Engine: Động cơ thực thi các câu lệnh SQL
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal: Phiên làm việc (Giống như một phiên giao dịch tại ngân hàng)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: lớp cơ sở để các Models khác kế thừa
Base = declarative_base()
