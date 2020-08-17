from setuptools import setup
import os

_here = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(_here, 'somepackage', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='basicmath',
    version=version['__version__'],
    description=('Show how to structure a Python project.'),
    long_description='Python project setup with code and unittest cases.',
    author='z09_homework1',
    author_email='',
    url='https://github.com/se20z09/z09_homework1',
    license='MPL-2.0',
    packages=['z09_homework1'],
    include_package_data=True,
    classifiers=[
        'Development Status :: Dev',
        'Intended Audience :: Software Engineers',
        'Programming Language :: Python :: 3.6'],
    )
