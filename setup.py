import re
import setuptools
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('ladybug/__init__.py', 'r') as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(),
        re.MULTILINE
    ).group(1)

try:
    from semantic_release import setup_hook
    setup_hook(sys.argv)
except ImportError:
    pass

setuptools.setup(
    name="lbt-ladybug",
    version=version,
    author="Ladybug Tools",
    author_email="info@ladybug.tools",
    description="Ladybug is a Python library to load, analyze and modify EneregyPlus Weather files (epw).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ladybug-tools/ladybug",
    packages=setuptools.find_packages(),
    install_requires=[
        'euclid3==0.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
)
