from rich.console import Console, ConsoleOptions, RenderResult
from rich.measure import Measurement
from rich.segment import Segment
from rich.style import Style, StyleType

CHARACTERS = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_{|}~"

PICO_CHARACTERS = """\
   


 ▄
 █
 ▄
▄ ▄
▀ ▀

▄ ▄
█▀█
█▀█
▄▄▄
▀█▄
▀█▀
▄ ▄
 ▄▀
█ ▄
▄▄ 
██▄
█▄█
 ▄
▀

 ▄
█ 
▀▄
 ▄ 
  █
 ▄▀
▄ ▄
▄█▄
▄▀▄

▄█▄
 ▀


▄▀

▄▄▄



 ▄
  ▄
 █ 
▄▀ 
▄▄▄
█ █
█▄█
▄▄ 
 █ 
▄█▄
▄▄▄
▄▄█
█▄▄
▄▄▄
 ▄█
▄▄█
▄ ▄
█▄█
  █
▄▄▄
█▄▄
▄▄█
▄  
█▄▄
█▄█
▄▄▄
  █
  █
▄▄▄
█▄█
█▄█
▄▄▄
█▄█
  █

 ▀
 ▀

 ▀
▄▀
  ▄
▄▀ 
 ▀▄

▀▀▀
▀▀▀
▄  
 ▀▄
▄▀
▄▄▄
 ▄█
 ▄
 ▄ 
█ █
▀▄▄
▄▄▄
█▄█
█ █
▄▄▄
█▄▀
█▄█
 ▄▄
█  
▀▄▄
▄▄ 
█ █
█▄█
▄▄▄
█▄ 
█▄▄
▄▄▄
█▄ 
█
 ▄▄
█  
█▄█
▄ ▄
█▄█
█ █
▄▄▄
 █ 
▄█▄
▄▄▄
 █ 
▄█ 
▄ ▄
█▄▀
█ █
▄  
█  
█▄▄
▄▄▄
█▀█
█ █
▄▄ 
█ █
█ █
 ▄▄
█ █
█▄▀
▄▄▄
█▄█
█
 ▄ 
█ █
▀█▄
▄▄▄
█▄▀
█ █
 ▄▄
█▄▄
▄▄▀
▄▄▄
 █ 
 █ 
▄ ▄
█ █
▀▄█
▄ ▄
█ █
▀█▀
▄ ▄
█ █
███
▄ ▄
▀▄▀
█ █
▄ ▄
█▄█
▄▄█
▄▄▄
 ▄▀
█▄▄
▄▄
█ 
█▄
▄  
 █ 
 ▀▄
 ▄▄
  █
 ▄█
 ▄ 
▀ ▀



▄▄▄
 ▄▄
▄█ 
 █▄
 ▄ 
 █ 
 █ 
▄▄
 █▄
▄█

▄▄█
▀
""".splitlines()


class PicoFont:
    def __init__(self, text: str, style: StyleType = "") -> None:
        self._text = text
        self._style = style

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        style = console.get_style(self._style)
        yield from self.render(style)

    def render(self, style: Style) -> RenderResult:
        # Render stolen from the Textual digits!
        character_pieces: list[list[str]] = [[], [], []]
        row1 = character_pieces[0].append
        row2 = character_pieces[1].append
        row3 = character_pieces[2].append

        for character in self._text.upper():
            try:
                position = CHARACTERS.index(character) * 3
            except ValueError:
                row1(" ")
                row2(" ")
                row3(character)
            else:
                row1(PICO_CHARACTERS[position].ljust(4))
                row2(PICO_CHARACTERS[position + 1].ljust(4))
                row3(PICO_CHARACTERS[position + 2].ljust(4))

        new_line = Segment.line()
        for line in character_pieces:
            yield Segment("".join(line), style)
            yield new_line

    @classmethod
    def get_width(cls, text: str) -> int:
        width = sum(4 if character in CHARACTERS else 1 for character in text)
        return width

    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement:
        width = self.get_width(self._text)
        return Measurement(width, width)
