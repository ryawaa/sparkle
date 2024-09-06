# sparkle

#### running sparkle via docker (recommended)
```bash
docker run -d -p 8000:8000 ryanamay/sparkle
```

#### running sparkle directly
sparkle uses poetry to manage dependencies. 

to install `poetry`, run the following command:
##### via pipx (recommended)
```bash
pipx install poetry
```



##### via pip
```bash
python3 -m venv $VENV_PATH
$VENV_PATH/bin/pip install -U pip setuptools
$VENV_PATH/bin/pip install poetry
```

##### running the app via uvicorn
```bash
git clone https://github.com/ryanamay/sparkle.git
poetry install
cd app
poetry run uvicorn main:app --host 0.0.0.0 --port 8000
```


