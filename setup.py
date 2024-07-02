from setuptools import setup, find_packages

setup(
    name="uois_deu",
    version="0.1.0",
    author="Ondrej Klement",
    author_email="ondrej.klement@unob.cz",
    description="A small utility made for UOIS to extract data from current database and creates demodata.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KlementOndrej/uois_deu",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "asyncio",
        "json",
    ],
)
