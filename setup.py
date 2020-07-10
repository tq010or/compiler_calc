from os import path as os_path
from setuptools import setup

from compiler_calc import simple_calc

this_directory = os_path.abspath(os_path.dirname(__file__))

def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

setup(
    name='compiler_calc',
    python_requires='>=3.7.0',
    version=simple_calc.__version__,
    description="This is a simple calculator when I try to recall my compiler courses.",
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    author=simple_calc.__author__,
    author_email=simple_calc.__email__,
    url='https://github.com/tq010or/calc',
    packages=[
        'compiler_calc'
    ],
    install_requires=read_requirements('requirements.txt'),
    include_package_data=True,
    license="MIT",
    keywords=['calculator', 'syntax analysis', 'lex analysis', 'compiler course'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
