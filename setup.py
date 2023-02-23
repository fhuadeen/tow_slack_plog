"""For publishing on Pypi"""

from setuptools import setup # type: ignore
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='slack-plog',
    version='0.0.1',
    description='Slack Python logging handler',
    py_modules=['tow_slack_plog'],
    package_dir={'': 'tow_slack_plog'},
    extras_require={
        "test": ["pytest >= 7.2.1"]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Communications :: Observability',
        'Topic :: System :: Logging',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3',
    long_description=long_description,
    author='Fhuad Balogun',
    author_email='fhuadbalogun@gmail.com',
    url='https://github.com/fhuadeen/tow_slack_plog',
    license='MIT',
    test_suite='tests',
    keywords='slack logging observability',
)
