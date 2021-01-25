# PyPI lib checker

This script was developed in order to automate Python libs update check of you project.
It reads you `requirements.txt` file and checks in [PyPI](https://pypi.org/) if your libs needs to be updated.

## Usage

First install required libs.

```bash
pip install requests==2.24.0 lxml==4.6.2
```

Then run the script `pypi.py` with a `requirements.txt` in the same directory.

```
.
├── pypi.py
└── requirements.txt
```

```bash
python pypi.py
```

## Example requirements.txt

In this repository there is a random [`requirements.txt`](./requirements.txt) example file, change it's content with your requirements file.

```txt
boto3==1.16.59
PyMySQL==1.0.1
SQLAlchemy==1.3.22
pylertalertmanager==0.1.0
```
