from database import SessionLocal
from repository import WeatherRepository
from service import WeatherService


def main():
    session = SessionLocal()
    try:
        repo = WeatherRepository(session)
        service = WeatherService(repo)

        print("Починаємо аналіз погодних даних...")
        service.calculate_should_go_out()

    except Exception as e:
        print(f"Сталася помилка: {e}")
        session.rollback()
    finally:
        session.close()


if __name__ == "__main__":
    main()