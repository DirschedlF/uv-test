import httpx


def main():
    response = httpx.get("https://httpbin.org/json")
    print(response.json())


if __name__ == "__main__":
    main()
