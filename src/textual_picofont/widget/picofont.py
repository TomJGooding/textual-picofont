from __future__ import annotations

from textual.app import RenderResult
from textual.geometry import Size
from textual.widget import Widget

from textual_picofont.renderable import PicoFont as PicoFontRenderable


class PicoFont(Widget):
    DEFAULT_CSS = """
    PicoFont {
        width: 1fr;
        height: auto;
    }
    """

    def __init__(
        self,
        text: str = "",
        *,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        disabled: bool = False,
    ) -> None:
        if not isinstance(text, str):
            raise TypeError("text must be a str")
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        self._text = text

    def render(self) -> RenderResult:
        rich_style = self.rich_style
        return PicoFontRenderable(self._text, rich_style)

    @property
    def text(self) -> str:
        return self._text

    def update(self, text: str) -> None:
        if not isinstance(text, str):
            raise TypeError("text must be a str")
        layout_required = len(text) != len(self._text) or (
            PicoFontRenderable.get_width(text) != PicoFontRenderable.get_width(text)
        )
        self._text = text
        self.refresh(layout=layout_required)

    def get_content_width(self, container: Size, viewport: Size) -> int:
        return PicoFontRenderable.get_width(self._text)

    def get_content_height(self, container: Size, viewport: Size, width: int) -> int:
        return 3
