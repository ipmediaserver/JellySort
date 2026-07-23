#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from tqdm import tqdm

VIDEO_EXTENSIONS = {
    ".mkv",
    ".mp4",
    ".avi",
    ".ts",
    ".m2ts",
    ".mov",
    ".wmv",
    ".iso"
}

MOVIES = Path("/home/dropbox/PELICULAS")
SERIES = Path("/home/dropbox/SERIES")


def scan(path):
    files = []

    for f in path.rglob("*"):
        if f.is_file() and f.suffix.lower() in VIDEO_EXTENSIONS:
            files.append(f)

    return files


def main():

    print("=" * 50)
    print(" JellySort v0.1")
    print("=" * 50)

    print("\nEscaneando películas...")

    movies = scan(MOVIES)

    for _ in tqdm(movies):
        pass

    print(f"\nPelículas encontradas: {len(movies)}")

    print("\nEscaneando series...")

    episodes = scan(SERIES)

    for _ in tqdm(episodes):
        pass

    print(f"\nEpisodios encontrados: {len(episodes)}")

    print("\nFinalizado correctamente.")


if __name__ == "__main__":
    main()
