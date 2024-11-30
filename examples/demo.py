import string

from textual.app import App, ComposeResult

from textual_picofont.widget import PicoFont


class PicoFontApp(App):
    CSS = """
    Screen {
        align: center middle;
    }

    PicoFont {
        width: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield PicoFont(" !\"#$%&'()*+,-./")
        yield PicoFont(string.digits + ":;<=>?")
        yield PicoFont("@" + string.ascii_uppercase[:15])
        yield PicoFont(string.ascii_uppercase[15:] + "[\\]^_")
        yield PicoFont("{|}~")


if __name__ == "__main__":
    app = PicoFontApp()
    app.run()
