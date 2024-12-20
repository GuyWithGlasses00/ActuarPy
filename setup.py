from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ActuarPy",
    version="0.1.0",
    author="Issaac Hansen",
    author_email="issaac.hansen@gmail.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GuyWithGlasses00/ActuaryPy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
    install_requires=requirements
)