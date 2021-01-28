from setuptools import setup
from io import open
import re

def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

with open('pyMyShareAPI/version.py', 'r', encoding='utf-8') as f:
    version = re.search(r"^__version__\s*=\s*'(.*)'.*$", f.read(), flags=re.MULTILINE).group(1)

setup(name='pyMyShareAPI',
        version=version,
        description='Easy MyShare SDK for Python',
        long_description=read('README.md'),
        long_description_content_type='text/markdown',
        author='LeanderGangso',
        author_email='Leander.Gangso98@gmail.com',
        url='https://github.com/LeanderGangso/pyMyShareAPI',
        license='............',
        keywords='myshare api wrapper',
        packages=['pymyshareapi'],
        install_requires=['requests'],
        extras_require={
            'json': 'ujson',
        },
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
            'Operating System :: OS Independent',
        ],
)

