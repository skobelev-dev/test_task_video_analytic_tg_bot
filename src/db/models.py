from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import func, DateTime, String, ForeignKey
from datetime import datetime



class Base(DeclarativeBase):
    pass

class Video(Base):
    __tablename__ = "videos"

    id: Mapped[str] = mapped_column(primary_key=True, autoincrement=False, nullable=False) # video url
    creator_id: Mapped[int] = mapped_column(String(10**10) ,unique=True, autoincrement=False, nullable=False)
    video_created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    view_count: Mapped[int] = mapped_column(String(10**10) ,autoincrement=False, nullable=False)
    likes_count: Mapped[int] = mapped_column(String(10**10) ,autoincrement=False, nullable=False)
    reports_count: Mapped[int] = mapped_column(String(10**10) ,autoincrement=False, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True, onupdate=func.now())

class VideoSnapshot(Base):
    __tablename__ = "video_snapshots"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    video_id: Mapped[str] = mapped_column(ForeignKey("videos.id", ondelete=None))

    views_count: Mapped[int]
    likes_count: Mapped[int]
    comments_count: Mapped[int]
    reports_count: Mapped[int]

    views_count_delta: Mapped[int]
    likes_count_delta: Mapped[int]
    comments_count_delta: Mapped[int]
    reports_count_delta: Mapped[int]

    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True, onupdate=func.now())