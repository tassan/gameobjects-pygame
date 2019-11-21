from game.main import App

game = App()


def test_screen():
    assert game.screenHeight > 0
    assert game.screenWidth > 0
    assert game.SCREEN is None


def test_init():
    assert game.RUNNING is True


def test_render():
    assert game.COLOR == (0, 0, 0)
