from database import SessionLocal, engine, Base
from models import User, Post

# 1. Tạo các bảng trong Database (nếu chưa có)
Base.metadata.create_all(bind=engine)

# 2. Khởi tạo một phiên làm việc (Session)
db = SessionLocal()

try:
    # 3. Tạo một User mới
    new_user = User(username="fresher_dev", email="dev@example.com")
    db.add(new_user)
    db.commit()  # Lưu User để lấy được ID
    db.refresh(new_user)  # Lấy lại thông tin User kèm theo ID vừa tạo

    # 4. Tạo bài viết cho User đó
    new_post = Post(title="Học SQLAlchemy",
                    content="Rất thú vị !", owner_id=new_user.id)
    db.add(new_post)
    db.commit()

    print(f"Đã tạo User: {new_user.username} với bài viết: {new_post.title}")
finally:
    db.close()  # Cực kỳ quan trọng: Luôn đóng session để giải phóng tài nguyên!
