import os
import sys
from setuptools import setup, find_packages
#import get_suite

DESCRIPTION = "the_pci_data: base application for ZeroBit"
VERSION = '1.0.0'
LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

requirements = [
    'django==4.0.5',
    'django-fernet-fields==0.6'
]

# python setup.py publish
if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    sys.exit()

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django',
]

# https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

setup(
    name='the_pci_data',
    version=VERSION,
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,
    author='ZeroBit',
    author_email='support@ZeroBit.tech',
    url='https://github.com/zerobit-tech/the_pci_data/',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    platforms=['any'],
    classifiers=CLASSIFIERS,
    install_requires=requirements,
    python_requires = '>=3.8',
    # test_suite = load_tests.get_suite
)