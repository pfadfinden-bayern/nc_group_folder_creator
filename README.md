
# nc_group_folder_creator

creates group folders with name, groups and quota given in a csv file

## usage

1. fill `config/config.toml` with your required values
1. run `save_cookies.py`, login with your credentials and press enter in the python console
1. fill `config/folders.json` (or another file, as defined in config.toml) with your required values
1. run `create_group_folders.py`

## requirements

- selenium `pip install selenium`
- webdriver ([installation](https://selenium-python.readthedocs.io/installation.html#drivers))
