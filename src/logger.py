import logging
import pathlib

logs_dir = pathlib.Path(__file__).parent / "logs_dir"
logs_dir.mkdir(exist_ok=True)
print(logs_dir)
print(logs_dir.exists())



logging.basicConfig(level=logging.DEBUG, filename=logs_dir / "logs.log", filemode="w")
logger = logging.getLogger(name=__name__,)
