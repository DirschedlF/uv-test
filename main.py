import arrow
import click
import httpx
from pydantic import BaseModel
from rich import print


class Slide(BaseModel):
    title: str
    type: str
    items: list[str] = []


class Slideshow(BaseModel):
    author: str
    date: str
    title: str
    slides: list[Slide]


class ApiResponse(BaseModel):
    slideshow: Slideshow


@click.command()
@click.option("--url", default="https://httpbin.org/json", help="URL to fetch JSON from.")
def main(url):
    now = arrow.now()
    print(f"[bold cyan]Current time:[/bold cyan] {now.format('YYYY-MM-DD HH:mm:ss')}")

    response = httpx.get(url)
    data = ApiResponse.model_validate(response.json())
    print(f"[bold green]Slideshow:[/bold green] {data.slideshow.title} by {data.slideshow.author}")
    for slide in data.slideshow.slides:
        print(f"  - {slide.title}")


if __name__ == "__main__":
    main()
