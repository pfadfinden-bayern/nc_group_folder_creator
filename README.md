
# nc_group_folder_creator

creates group folders with name, groups and quota given in a csv file

## usage

1. copy `config/config.toml.template` to `config/config.toml` and fill with your required values
1. run `save_cookies.py`, login with your credentials and press enter in the python console
1. copy `config/folders.json.template` to `config/folders.json` (or another file, as defined in config.toml) and fill with your required values
1. run `create_folders.py`

## requirements

- selenium `pip install selenium`
- webdriver ([installation](https://selenium-python.readthedocs.io/installation.html#drivers))
