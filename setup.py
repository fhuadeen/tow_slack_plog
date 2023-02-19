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
    version='0.3.1',
    description='Slack Python logging handler',
    long_description=long_description,
    url='https://github.com/fhuadeen/tow_slack_plog',
    author='Fhuad Balogun',
    author_email='fhuadbalogun@gmail.com',
    license='MIT',
    test_suite='tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Communications :: Chat',
        'Topic :: System :: Logging',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='slack logging',
    py_modules=['tow_slack_plog'],
)
