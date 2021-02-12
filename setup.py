from distutils.core import setup

setup(
    # Application name:
    name="narpy - NASA AMES Reader for Python",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Jago Strong-Wright",
    author_email="jagoosw@protonmail.com",

    # Packages
    packages=["narpy"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/jagoosw/narpy",

    #
    license="LICENSE.txt",
    description="A simple NASA AMES file Reader for Python",

    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",

    # Dependent packages (distributions)
    install_requires=[
        "numpy",
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GLP-3.0 ",
        "Operating System :: OS Independent",
    ],
)