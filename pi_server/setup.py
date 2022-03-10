from setuptools import find_packages, setup

setup(
    name="pi_server",
    version="0.1.0",
    packages=find_packages(exclude=["tests"]),
    install_requires=["flask==2.0.3"],
    extras_require={"dev": ["pytest", "mypy", "black", "isort"]},
    entry_points={
        "console_scripts": [
            "run_server = app.__main__:main",
        ],
    },
)