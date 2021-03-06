from setuptools import setup
from subprocess import check_call
import shutil
import sys
import fstrings


if sys.argv[-1] == 'cheeseit!':
    check_call('nosetests -v --with-coverage --with-doctest --doctest-extension rst')
    check_call('python setup.py sdist bdist_wheel')
    check_call('twine upload dist/*')
    shutil.rmtree('dist')
    sys.exit()
elif sys.argv[-1] == 'testit!':
    check_call('nosetests -v --with-coverage --with-doctest --doctest-extension rst')
    check_call('python setup.py sdist bdist_wheel upload -r pypitest')
    sys.exit()


with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name=fstrings.__title__,
    version=fstrings.__version__,
    url=fstrings.__url__,
    license=fstrings.__license__,
    author=fstrings.__author__,
    author_email=fstrings.__email__,
    description=fstrings.__doc__,
    long_description=long_description,
    py_modules=[fstrings.__title__,],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
