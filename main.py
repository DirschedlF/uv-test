import arrow
import click
import httpx
from rich import print


@click.command()
@click.option("--url", default="https://httpbin.org/json", help="URL to fetch JSON from.")
def main(url):
    now = arrow.now()
    print(f"[bold cyan]Current time:[/bold cyan] {now.format('YYYY-MM-DD HH:mm:ss')}")

    response = httpx.get(url)
    print(response.json())


if __name__ == "__main__":
    main()
