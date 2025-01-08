How to enable local env?
1. `python -m venv venv` in the root dir
2. For entering virtual env, call:  Windows: `venv\Scripts\activate` or Linux: `source venv/bin/activate` (and `deactivate` when close)
3. Call `pip install <name>` to install a package
4. Call `pip freeze > requirements.txt` for saving current requirements
5. Call  `pip install -r requirements.txt` for installing packages from `requirements.txt`