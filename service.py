from repository import WeatherRepository
from datetime import datetime


class WeatherService:
    def __init__(self, repository: WeatherRepository):
        self.repository = repository

    def calculate_should_go_out(self):
        wind_records = self.repository.get_all_wind_data()
        updated_count = 0

        for record in wind_records:
            if record.wind_kph > 36.0:
                record.should_go_out = False
            else:
                record.should_go_out = True

            updated_count += 1

        self.repository.commit_changes()
        print(f"Успішно оновлено колонку should_go_out для {updated_count} записів!")

    def get_formatted_weather_report(self, country: str, date_str: str) -> str:
        try:
            target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return "Помилка: Неправильний формат дати. Використовуйте формат РРРР-ММ-ДД."

        records = self.repository.get_weather_by_country_and_date(country, target_date)

        if not records:
            return f"Інформації про погоду в '{country}' на {date_str} не знайдено у базі."


        report = f"\nПОГОДНИЙ ЗВІТ: {country.upper()} | {date_str}\n"

        for record in records:
            report += f"Схід сонця: {record.sunrise if record.sunrise else 'Немає даних'}\n"

            if record.wind_info:
                wind = record.wind_info
                report += f"Швидкість вітру: {wind.wind_kph} км/год\n"
                report += f"Напрямок вітру: {wind.wind_direction.value}\n"

                if wind.gust_kph:
                    report += f"Пориви вітру до: {wind.gust_kph} км/год\n"

                report += "-" * 30 + "\n"
                if wind.should_go_out is True:
                    report += "Погода сприятлива, можна виходити на вулицю!\n"
                elif wind.should_go_out is False:
                    report += "Сильний вітер, краще залишитися вдома!\n"

            report += "=" * 45 + "\n"

        return report
