# GPX utils

This cli will merge several gpx files into one. Built using [uv](https://docs.astral.sh/uv/).

# Installation

```bash
make && make install
```

# Usage

```
> gpxutil --help
gpxutil --help
                                                                                                                       
 Usage: gpxutil [OPTIONS] FILES...                                                                                   
                                                                                                                       
╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ *    files      FILES...  [required]                                                                                │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --output              -o      TEXT  Output file path [default: /Users/charles/mactynow/merge_gpx/merged.gpx]        │
│ --install-completion                Install completion for the current shell.                                       │
│ --show-completion                   Show completion for the current shell, to copy it or customize the              │
│                                     installation.                                                                   │
│ --help                              Show this message and exit.                                                     │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```