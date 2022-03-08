from setuptools import find_packages, setup

setup(
    name="pi_server",
    version="0.1.0",
    packages=find_packages(exclude=["tests"]),
    install_requires=["streamlit"],
    extras_require={"dev": ["pytest", "mypy", "black", "isort"]},
    entry_points={
        "console_scripts": [
            "run_server = app.__main__:main",
        ],
    },
)
