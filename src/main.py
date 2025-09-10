from config.settings import get_settings

settings = get_settings()


def main():
    for key, value in settings.APP.model_dump().items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
