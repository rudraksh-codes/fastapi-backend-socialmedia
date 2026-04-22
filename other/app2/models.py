from .database import Base 
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.sql import func
class Post(Base) : 
    __tablename__ = 'postis' 

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False) 
    content = Column(String, nullable = False) 
    published = Column(Boolean, default=True) 
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())