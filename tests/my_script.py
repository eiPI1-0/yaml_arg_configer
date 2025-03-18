import sys
from pathlib import Path

path_root = Path(__file__).parent.parent
sys.path.append(str(path_root))

from src import YamlArgParser

yaml_parser = YamlArgParser()
cmd_args = yaml_parser.parse_cmd_args()
print(yaml_parser.parse_args(cmd_args))
