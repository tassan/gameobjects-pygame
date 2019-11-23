from game.__main__ import App

game = App()


def test_screen():
    assert game.screenHeight > 0
    assert game.screenWidth > 0
    assert game.screen is None


def test_init():
    assert game.RUNNING is True

