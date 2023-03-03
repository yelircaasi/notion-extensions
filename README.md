# notion-extensions

Personalized tools to help me work with the Notion API and fill in its gaps, most notably wiith Selenium.

Recommended directories and files:

* `~/.cache/notion/`: store for status-tracking files and logs
* `~/.config/notion/`: user-specific configuration, especially token tokens, URLS, block IDs, xpaths, etc.
* `~/.config/notion/tokens/`: directory to store token keys, where each file has the same name as the corresponding integration and contains only the token
* `~/.config/notion/notion.toml`: configuration file

Alternative config, recipe, and token token files can be given with environment variables:

* `NOTION_EXT_CONFIG_PATH`
* `NOTION_EXT_RECIPE_PATH`
* `NOTION_EXT_TOKEN_PATH`
