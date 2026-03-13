from setuptools import setup, find_packages

setup(
    name="calcu",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "calcu=calcu.main:main",
        ],
    },
    author="Leo",
    description="A minimal installable calculator for Linux",
)
