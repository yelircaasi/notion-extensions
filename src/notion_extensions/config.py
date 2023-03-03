import os
from pathlib import Path

import tomlkit

from notion_extensions.utils.dicts import as_dotdict

config_toml = Path.expanduser(
    Path(os.environ.get("NOTION_EXT_CONFIG_PATH") or "~/.config/notion/notion.toml")
)
with open(config_toml) as f:
    config = as_dotdict(tomlkit.parse(f.read()))

path_to_token = Path.expanduser(
    Path(os.environ.get("NOTION_EXT_TOKEN_PATH") or config.paths.integration_token)
)
with open(path_to_token) as f:
    config.integration_token = f.read().strip()

path_to_recipe = Path.expanduser(
    Path(
        os.environ.get("NOTION_EXT_RECIPE_PATH")
        or "~/.config/notion/update_recipe.toml"
    )
)
with open(path_to_recipe) as f:
    recipe = as_dotdict(tomlkit.parse(f.read()))
