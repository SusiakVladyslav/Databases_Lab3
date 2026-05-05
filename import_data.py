import csv
from datetime import datetime
from database import SessionLocal
from models import Weather, WindDirection, WindData  # Додали WindData
from repository import WeatherRepository


def parse_csv_and_import(file_path: str):
    session = SessionLocal()
    repo = WeatherRepository(session)
    weather_records = []

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                parsed_date = datetime.strptime(row['last_updated'], "%Y-%m-%d %H:%M").date()

                try:
                    parsed_sunrise = datetime.strptime(row['sunrise'], "%I:%M %p").time()
                except ValueError:
                    parsed_sunrise = None

                try:
                    wind_dir_enum = WindDirection(row['wind_direction'])
                except ValueError:
                    continue

                weather = Weather(
                    country=row['country'],
                    last_updated=parsed_date,
                    sunrise=parsed_sunrise
                )

                wind_info = WindData(
                    wind_degree=int(row['wind_degree']),
                    wind_kph=float(row['wind_kph']),
                    wind_direction=wind_dir_enum,
                    wind_mph=float(row['wind_mph']),
                    gust_kph=float(row['gust_kph']),
                    gust_mph=float(row['gust_mph'])
                )

                weather.wind_info = wind_info

                weather_records.append(weather)

        repo.bulk_save(weather_records)
        print(f"Успішно імпортовано {len(weather_records)} записів.")

    except Exception as e:
        import traceback
        print(f"Помилка під час імпорту: {e}")
        traceback.print_exc()
        session.rollback()
    finally:
        session.close()


if __name__ == "__main__":
    parse_csv_and_import("GlobalWeatherRepository.csv")