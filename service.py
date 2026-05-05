from repository import WeatherRepository


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