from sqlalchemy.orm import Session
from models import Weather, WindData
from datetime import date


class WeatherRepository:
    def __init__(self, session: Session):
        self.session = session

    def bulk_save(self, weather_records: list[Weather]):
        self.session.add_all(weather_records)
        self.session.commit()

    def get_all_wind_data(self) -> list[WindData]:
        return self.session.query(WindData).all()

    def commit_changes(self):
        self.session.commit()

    def get_weather_by_country_and_date(self, country_name: str, target_date: date):
        return self.session.query(Weather).filter(
            Weather.country.ilike(f"%{country_name}%"),
            Weather.last_updated == target_date
        ).all()