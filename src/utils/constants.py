from pathlib import Path

(output_dir := Path(__file__).parent.parent.parent / "output").mkdir(parents=True, exist_ok=True)


def get_output_path(filename: str) -> Path:
    """Get the output path for a given filename."""
    return output_dir / filename
