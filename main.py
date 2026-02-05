import arrow
import httpx
from rich import print


def main():
    now = arrow.now()
    print(f"[bold cyan]Current time:[/bold cyan] {now.format('YYYY-MM-DD HH:mm:ss')}")

    response = httpx.get("https://httpbin.org/json")
    print(response.json())


if __name__ == "__main__":
    main()
