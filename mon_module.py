def addition(a, b):
    import requests
    return int(requests.get(f"http://localhost:8000/addition?a={a}&b={b}").content.decode("utf-8"))