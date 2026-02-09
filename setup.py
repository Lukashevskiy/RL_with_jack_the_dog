"""
Setup script for the RL seminar environment package (env).
Install from project root: pip install -e .
"""

from setuptools import setup, find_packages

setup(
    name="jack_the_dog",
    version="0.1.0",
    description="RL seminar: DogSocks grid environment and wrappers",
    packages=find_packages(where=".", include=["env"]),
    package_dir={"": "."},
    python_requires=">=3.9",
    install_requires=[
        "gymnasium>=0.29.0",
        "numpy>=1.24.0",
        "Pillow>=10.0.0",
    ],
)
