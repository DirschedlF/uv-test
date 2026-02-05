import pytest
from pydantic import ValidationError

from main import ApiResponse, Slide, Slideshow


class TestSlide:
    def test_basic_slide(self):
        slide = Slide(title="Intro", type="all")
        assert slide.title == "Intro"
        assert slide.type == "all"
        assert slide.items == []

    def test_slide_with_items(self):
        slide = Slide(title="Overview", type="all", items=["a", "b"])
        assert slide.items == ["a", "b"]

    def test_slide_missing_title(self):
        with pytest.raises(ValidationError):
            Slide(type="all")

    def test_slide_missing_type(self):
        with pytest.raises(ValidationError):
            Slide(title="Intro")


class TestSlideshow:
    def test_basic_slideshow(self):
        slideshow = Slideshow(
            author="Alice",
            date="2026-01-01",
            title="My Talk",
            slides=[Slide(title="Intro", type="all")],
        )
        assert slideshow.author == "Alice"
        assert slideshow.title == "My Talk"
        assert len(slideshow.slides) == 1

    def test_slideshow_missing_slides(self):
        with pytest.raises(ValidationError):
            Slideshow(author="Alice", date="2026-01-01", title="My Talk")

    def test_slideshow_empty_slides(self):
        slideshow = Slideshow(
            author="Alice", date="2026-01-01", title="My Talk", slides=[]
        )
        assert slideshow.slides == []


class TestApiResponse:
    def test_valid_response(self):
        data = {
            "slideshow": {
                "author": "Yours Truly",
                "date": "date of publication",
                "title": "Sample Slide Show",
                "slides": [
                    {"title": "Wake up to WonderWidgets!", "type": "all"},
                    {
                        "title": "Overview",
                        "type": "all",
                        "items": ["Why WonderWidgets are great"],
                    },
                ],
            }
        }
        response = ApiResponse.model_validate(data)
        assert response.slideshow.author == "Yours Truly"
        assert len(response.slideshow.slides) == 2
        assert response.slideshow.slides[1].items == ["Why WonderWidgets are great"]

    def test_missing_slideshow(self):
        with pytest.raises(ValidationError):
            ApiResponse.model_validate({})
