import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="konbata", # Replace with your own username
    version="0.0.1",
    author="Jonas Zeuner",
    author_email="jzeuner.oss@gmail.com",
    description="Python File Converter for hierarchical data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jzeuner/konbata",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
