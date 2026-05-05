from database import SessionLocal
from repository import WeatherRepository
from service import WeatherService

def main():
    session = SessionLocal()
    repository = WeatherRepository(session)
    service = WeatherService(repository)

    print("=========================================")
    print("           ПОГОДНИЙ ІНФОРМАТОР           ")
    print("=========================================")
    print("Для виходу з програми введіть 'exit' або 'quit'.\n")

    try:
        while True:
            country = input("Введіть назву країни (англійською): ").strip()
            if country.lower() in ['exit', 'quit']:
                break
            if not country:
                print("Назва країни не може бути порожньою. Спробуйте ще раз.\n")
                continue

            date_input = input("Введіть дату в форматі РРРР-ММ-ДД: ").strip()
            if date_input.lower() in ['exit', 'quit']:
                break

            print("\nШукаю інформацію в базі даних...")
            report = service.get_formatted_weather_report(country, date_input)
            print(report)

    except KeyboardInterrupt:
        print("\nРаптове завершення роботи.")
    finally:
        session.close()
        print("Роботу завершено!")

if __name__ == "__main__":
    main()