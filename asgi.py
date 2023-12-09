from uvicorn import run
from app.app import app

def main():
    run(app, host="0.0.0.0", port=443)

if __name__ == "__main__":
    main()