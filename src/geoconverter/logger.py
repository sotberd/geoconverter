import logging

from rich.console import Console
from rich.logging import RichHandler
from rich_toolkit import RichToolkit, RichToolkitTheme
from rich_toolkit.styles import TaggedStyle

FORMAT = "%(message)s"


def setup_logging(
    terminal_width: int | None = None,
    level: int = logging.INFO,
    show_time: bool = False,
) -> None:
    logger = logging.getLogger("geoconverter")
    console = Console(width=terminal_width) if terminal_width else None
    rich_handler = RichHandler(
        show_time=show_time,
        rich_tracebacks=True,
        tracebacks_show_locals=True,
        markup=True,
        show_path=False,
        console=console,
    )
    rich_handler.setFormatter(logging.Formatter(FORMAT))
    logger.addHandler(rich_handler)

    logger.setLevel(level)
    logger.propagate = False


def get_rich_toolkit() -> RichToolkit:
    theme = RichToolkitTheme(
        style=TaggedStyle(tag_width=11),
        theme={
            "tag.title": "white on #FF7043",
            "tag": "white on #53C9D5",
            "placeholder": "grey85",
            "text": "white",
            "selected": "#53C9D5",
            "result": "grey85",
            "progress": "on #53C9D5",
            "log.info": "black on blue",
            "log.success": "green",
            "log.warning": "yellow",
            "log.error": "red",
        },
    )

    return RichToolkit(theme=theme)
