import arrow
import httpx


def main():
    now = arrow.now()
    print(f"Current time: {now.format('YYYY-MM-DD HH:mm:ss')}")

    response = httpx.get("https://httpbin.org/json")
    print(response.json())


if __name__ == "__main__":
    main()
