import uvicorn

from config.settings import create_app


def main():
    return create_app("HiFi")


if __name__ == '__main__':
    uvicorn.run("manage:main", host="0.0.0.0", port=8000, reload=True)
