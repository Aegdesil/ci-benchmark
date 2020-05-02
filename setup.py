import os

import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as readme:
    # pylint: disable=invalid-name
    long_description = readme.read()

setuptools.setup(
    name="ci_benchmark",
    version="DEV",
    url="https://github.com/aegdesil/ci-benchmark/",

    author="Aegdesil",
    description="A test repository to compare CI/CD solutions",
    long_description=long_description,
    long_description_content_type="text/markdown",

    zip_safe=False,
    platforms="any",

    install_requires=[
        "termcolor>=1.1.0,<2.0.0",
    ],
    python_requires=">=3.6,<4.0",
    packages=setuptools.find_packages(include=["ci_benchmark", "ci_benchmark.*"]),

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
