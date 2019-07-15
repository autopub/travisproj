from travisproj.hello import hello


def test_hello():
    hello_world = hello()
    assert hello_world == "Hello World"
