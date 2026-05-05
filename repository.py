from sqlalchemy.orm import Session
from models import Weather


class WeatherRepository:
    def __init__(self, session: Session):
        self.session = session

    def bulk_save(self, weather_records: list[Weather]):
        self.session.bulk_save_objects(weather_records)
        self.session.commit()