import io
import os
import re

from setuptools import setup, find_packages


NAME = "package"


# https://packaging.python.org/guides/single-sourcing-package-version/
def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
    )
    if version_match:
        return version_match.group(1)


project_root = os.path.dirname(os.path.abspath(__file__))

long_description = ""
with open(os.path.join(project_root, "README.md")) as f:
    long_description = f.read()

install_requires = []
with open(os.path.join(project_root, "requirements.txt")) as f:
    install_requires = f.read().splitlines()


setup(
    name=NAME,
    version=find_version(os.path.join(project_root, NAME, "__init__.py")),
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    author="",
    author_email="",
    license="MIT",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Operating System :: MacOS",
    ],
    zip_safe=False,
    python_requires=">=3.6",
)
