import enum
from sqlalchemy import Column, Integer, Float, String, Date, Time, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class WindDirection(enum.Enum):
    N = "N"
    NNE = "NNE"
    NE = "NE"
    ENE = "ENE"
    E = "E"
    ESE = "ESE"
    SE = "SE"
    SSE = "SSE"
    S = "S"
    SSW = "SSW"
    SW = "SW"
    WSW = "WSW"
    W = "W"
    WNW = "WNW"
    NW = "NW"
    NNW = "NNW"


class WindData(Base):
    __tablename__ = "wind_data"

    id = Column(Integer, primary_key=True, index=True)

    weather_id = Column(Integer, ForeignKey("weather_data.id"), unique=True)

    wind_degree = Column(Integer, nullable=False)
    wind_kph = Column(Float, nullable=False)
    wind_direction = Column(Enum(WindDirection), nullable=False)
    wind_mph = Column(Float, nullable=True)
    gust_kph = Column(Float, nullable=True)
    gust_mph = Column(Float, nullable=True)

    weather = relationship("Weather", back_populates="wind_info")

class Weather(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, nullable=False)
    last_updated = Column(Date, nullable=False)
    sunrise = Column(Time, nullable=True)

    wind_info = relationship("WindData", back_populates="weather", uselist=False)
