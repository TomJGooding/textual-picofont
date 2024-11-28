import string

from textual.app import App, ComposeResult
from textual.widgets import Static

from textual_picofont.renderable import PicoFont as PicoFontRenderable


class PicoFontApp(App):
    def compose(self) -> ComposeResult:
        yield Static(
            PicoFontRenderable(string.ascii_uppercase),
        )
        yield Static(
            PicoFontRenderable(string.digits),
        )
        yield Static(
            PicoFontRenderable(" !\"#$%&'()*+,-./"),
        )
        yield Static(
            PicoFontRenderable(":;<=>?@"),
        )


if __name__ == "__main__":
    app = PicoFontApp()
    app.run()
