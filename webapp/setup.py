from setuptools import find_packages, setup

setup(
    name="webapp",
    version="0.1.0",
    packages=find_packages(exclude=["tests"]),
    install_requires="streamlit==1.8.1",
    extras_require={"dev": ["pytest", "mypy", "black"]},
    entry_points={
        "console_scripts": [
            "run_server = webapp.__main__:main",
        ],
    },
)
