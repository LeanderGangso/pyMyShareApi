from setuptools import setup
from io import open
import re

base_url = 'https://github.com/LeanderGangso/pyMyShareAPI'

def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

with open('mysdk/version.py', 'r', encoding='utf-8') as f:
    version = re.search(r"^__version__\s*=\s*'(.*)'.*$", f.read(), flags=re.MULTILINE).group(1)

setup(name='pyMyShareSDK',
        version=version, # gets version from version.py file
        description='Easy MyShare SDK for Python',
        long_description=read('README.md'),
        long_description_content_type='text/markdown',
        author='LeanderGangso',
        author_email='Leander.Gangso98@gmail.com',
        url=base_url,
        download_url=f'{base_url}/archive/v{version}.tar.gz', # download same version as pypi
        license='LGPLv3',
        keywords='python myshare sdk api tools',
        packages=['mysdk'],
        install_requires=['requests'],
        extras_require={
            'json': 'ujson',
        },
        classifiers=[
            'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
            'Operating System :: OS Independent',
            'Development Status :: 3 - Alpha', # 3 - Alpha, 4 - Beta, 5 - Production/Stable
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Programming Language :: Python :: 3.8',
        ],
        python_requires='>=3.8'
)

