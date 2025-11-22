import gpxpy
import typer
import os
from rich.progress import Progress, SpinnerColumn, TextColumn
from typing_extensions import Annotated

app = typer.Typer()

@app.command("merge")
def merge(files: list[str],
          output: Annotated[str, typer.Option("--output", "-o", help="Output file path")] = f"{os.getcwd()}/merged.gpx"
):
  with Progress(
      SpinnerColumn(),
      TextColumn("[progress.description]{task.description}"),
      transient=True,
  ) as progress:
    progress.add_task(description="Processing files...", total=None)

    gpx_files = []
    for file in files:
      with open(file, 'r') as f:
        parsed = gpxpy.parse(f)
        if parsed.tracks:
          gpx_files.append(parsed)

    list.sort(gpx_files, key=lambda gpx: gpx.get_time_bounds().start_time)

    merged = gpx_files.pop(0)
    for gpx in gpx_files:
      if gpx.tracks:
        for track in gpx.tracks:
          for segment in track.segments:
            merged.tracks[0].segments.append(segment)

    with open(output, 'w') as f:
        f.write(merged.to_xml())

    print(f"Merged file written to {output}")