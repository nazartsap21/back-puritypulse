from uvicorn import run

from app.app import app


# "192.168.1.119"
def main():
    run(app, host="0.0.0.0", port=443)


if __name__ == "__main__":
    main()