from pathlib import Path
from yt_dlp import YoutubeDL

project_folder = Path(__file__).parent

def main():
    input_text_file = project_folder / "input.txt"
    output_folder = project_folder / "output"

    output_folder.mkdir(exist_ok=True, parents=True)
        

    urls = input_text_file.read_text().strip().split("\n")
    dl(urls, output_folder)
    
def dl(urls: list[str], output_folder: Path):
    ydl_opts = {
        "cookiesfrombrowser": ("firefox",),
        "playliststart": 2,
        "playlistend": 8,
        "paths": {"home": output_folder.__str__()},
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)


if __name__ == "__main__":
    main()
