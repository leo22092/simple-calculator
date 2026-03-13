from setuptools import setup, find_packages

setup(
    name="calcu",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points={
        "console_scripts": [
            "calcu=calcu.main:main",
        ],
    },
    author="Leo",
    description="A minimal installable calculator for Linux",
)
