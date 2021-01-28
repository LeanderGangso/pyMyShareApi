# pyMyShareSDK

**Important!  
We do not have access to the API at this point, as the API itself is not yet launched.  
We will be updating this repo as soon as the situation changes!**

We have made the MyShare API easy to use.  

[![License](https://img.shields.io/pypi/l/pymysharesdk.svg?label=License&logo=license&logoColor=red&labelColor=white)](#edit-me)
[![MyShare](https://img.shields.io/badge/MyShare-white?logo=data:image/svg%2bxml;base64,PHN2ZyB2ZXJzaW9uPSIxLjEiIHZpZXdCb3g9IjAgMCA1NSA1NSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGc+Cjxwb2x5Z29uIGNsYXNzPSIiIHBvaW50cz0iNTMuNjY4IDIyLjM3NCAzNC44NjggMjIuMjc0IDQxLjg2OCAzLjM3NDIgMzAuNDY4IDMuMjc0MiAyMy40NjggMjIuMTc0IDQuNjY4NSAyMi4wNzQgMC44Njg0NSAzMS44NzQgMTkuNzY4IDMxLjk3NCAxMi43NjggNTAuODc0IDI0LjE2OCA1MC45NzQgMzEuMTY4IDMyLjA3NCA0OS45NjggMzIuMTc0IiBmaWxsPSIjOEFCQThCIi8+Cjxwb2x5Z29uIGNsYXNzPSIiIHBvaW50cz0iNTMuNjY4IDIyLjM3NCAzNC44NjggMjIuMjc0IDQxLjg2OCAzLjM3NDIgMzAuNDY4IDMuMjc0MiAyMy40NjggMjIuMTc0IDE5Ljc2OCAzMS45NzQgMzEuMTY4IDMyLjA3NCA0OS45NjggMzIuMTc0IiBmaWxsPSIjM0UzRTNFIi8+CjwvZz4KPC9zdmc+Cg==)](#pyMySharesdk)
[![Open source](https://img.shields.io/badge/Open_Source-white?logo=GitHub-Sponsors&logoColor=red)](#pyMySharesdk)  
[![PyPi](https://img.shields.io/pypi/v/pymysharesdk.svg?logo=pypi&label=PyPi&labelColor=white)](https://pypi.org/project/pymysharesdk/)
[![Python versions](https://img.shields.io/pypi/pyversions/pymysharesdk.svg?label=Python&logo=python&labelColor=white)](https://pypi.org/project/pymysharesdk/)
[![Downloads](https://img.shields.io/pypi/dm/pymysharesdk?labelColor=white&logo=pypi&label=Downloads)](https://pypistats.org/packages/pymysharesdk)

## Table on contents

- [Introduction](#introduction)
- [API support](#api-support)
- [Installing](#installing)
- [Getting started](#getting-started)
  - [Example setup](#example-setup)
  - [Documentation](#documentation)
- [Getting help](#getting-help)
- [Contributing](#contributing)
- [License - key points](#license---key-points)

## Introduction

We are currently waiting on MyShare API to launch.  
This project will start as soon as we have access to the newly created API.

## API support

We are currently supporting the following methods:

- [ ] Method name
- [x] Method name
- [ ] Method name

## Installing

With PIP (recommended):

```bash
pip install pymysharesdk
```

With git-clone:

```bash
git clone https://github.com/LeanderGangso/pyMyShareSDK
cd pyMyShareSDK
python setup.py install
```

## Getting started

Our Wiki contains a lot of resources to get you started with `pyMyShareSDK`:

- [Introduction to the SDK](#edit-me)
- [Make your first function](#edit-me)
- Go to [documentation](#documentation) to see the official documentations.

### Example's

We believe that the best way to learn this package is to learn by seeing. We have some examples that you can look at and use as your template for you new project.  

Starting template with environment variables:

```python
import pymysharesdk
import os

# get TOKEN from environment
TOKEN = os.environ('TOKEN')

# create an instance
pms = pymysharesdk.MyShareSDK(token=TOKEN)

# make a call :return dict
pms.create_job(name, start_date, end_date, hours)
```

For more, visit [this page](https://github.com/leandergangso/pyMyShareSDK/examples/) and discover our official examples.

### Documentation

- Thake a look at our official [Wiki page](https://github.com/LeanderGangso/pyMyShareSDK/wiki).

- Or visit the origional [MyShare API](https://api.myshare.today) documentation.  

> All our methods have the same name's as the origional API, but with **snake_casing** instead.

## Getting help

You can get help in serveral ways:

- We have a [telegram group](t.me/pyMyShareSDK) that you can join and ask any questions.

- Report bugs, request features or ask questions by [creatin an issue](https://github.com/LeanderGangso/pyMyShareSDK/issues/new/choose) or [a discussion](https://github.com/LeanderGangso/pyMyShareSDK/discussions/new).

- Our [Wiki pages](https://github.com/LeanderGangso/pyMyShareSDK/wiki) has the information you need.  

> You could always help us improve by adding the missing information to the wiki.

## Contributing

Contributions of all sizes are welcome. Please review our [contribution guidelines](https://github.com/LeanderGangso/pyMyShareSDK/blob/master/CODE_OF_CONDUCT.md) to get started. You can also help by [reporting bugs](https://github.com/LeanderGangso/pyMyShareSDK/issues/new/choose).

## License - key points

To be determined...
<!---
- When distributing derived works, the source code of the work must be made available under the same license.
- All modification's has to have the same license and be open source.
- You do not need to release you modified code, but we would really apreacheate it you did do a [pull request](https://www.freecodecamp.org/news/how-to-make-your-        first-pull-request-on-github-3/) with you changes.
--->

Disclaimer: I am not a lawyer, so any and all information given is strictly based on my understanding and may or may not be correct.
