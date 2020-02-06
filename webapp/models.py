from sqlalchemy import Boolean, Column, DateTime, Integer, JSON, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Token(Base):
    __tablename__ = "token"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    token = Column(String, nullable=False)


class Asset(Base):
    __tablename__ = "asset"

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False)
    data = Column(JSON, nullable=False)
    file_path = Column(String, nullable=False)

    def as_json(self):
        return {
            **self.data,
            "created": self.created.strftime("%a, %d %b %Y %H:%M:%S"),
            "file_path": self.file_path,
        }


class Redirect(Base):
    __tablename__ = "redirect"

    id = Column(Integer, primary_key=True)
    redirect_path = Column(String, nullable=False)
    target_url = Column(String, nullable=False)
    permanent = Column(Boolean, nullable=False)

    def as_json(self):
        return {
            "redirect_path": self.redirect_path,
            "target_url": self.target_url,
            "permanent": self.permanent,
        }