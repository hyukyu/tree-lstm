import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tree-lstm",
    version="0.0.1",
    author="Inhyuk Na",
    author_email="ina@dblab.postech.ac.kr",
    description="pytorch tree lstm package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inyukwo1/tree-lstm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)