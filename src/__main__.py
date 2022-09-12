from uvicorn import run

from social_links_service.create_app import create_app

if __name__ == "__main__":
    app = create_app()

    run(app, host="0.0.0.0")  # type: ignore
