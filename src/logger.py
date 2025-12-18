import logging
import pathlib

file = pathlib.Path(__file__).parent / "logs_dir"
file.mkdir(exist_ok=True)



logging.basicConfig(level=logging.INFO, filename=file / "logs.log")