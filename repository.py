from sqlalchemy.orm import Session
from models import Weather, WindData


class WeatherRepository:
    def __init__(self, session: Session):
        self.session = session

    def bulk_save(self, weather_records: list[Weather]):
        self.session.bulk_save_objects(weather_records)
        self.session.commit()

    def get_all_wind_data(self) -> list[WindData]:
        return self.session.query(WindData).all()

    def commit_changes(self):
        self.session.commit()