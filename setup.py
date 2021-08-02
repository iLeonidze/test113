import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="test113",
    version="1.0.0",
    description="Demo package for testing purposes",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/iLeonidze/test113",
    author="Leonid Fedotov",
    author_email="me@ileonidze.ml",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["test113"],
    include_package_data=True,
    install_requires=["jinja2"],
    entry_points={
        "console_scripts": [
            "test113=test113.__main__:main",
        ]
    },
)