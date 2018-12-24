from setuptools import setup, find_packages
from os import path

my_loc = path.abspath(path.dirname(__file__))

with open(path.join(my_loc, "README.rst"), "r") as readme:
    long_description = readme.read()

setup(
        name="howmuchtime",
        version="0.2.0",
        license="MIT",
        packages=find_packages(),
        python_requires="~=3.0",
        description="Countdown to a date.",
        long_description=long_description,
        author="Filip Osowski",
        author_email="filiposowski5@gmail.com",
        url="https://github.com/FilipOsowski/howmuchtime",
        include_package_data=True,
        entry_points={
            "console_scripts": [
                "hmt = howmuchtime.hmt:cli"
            ]
        },
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
        ],
)
