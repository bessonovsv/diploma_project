from setuptools import setup, find_packages

setup(
    name="diploma_project",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "selenium",
        "requests",
        "pytest",
        "webdriver-manager",
        "allure-pytest",
        "flake8",
    ],
    entry_points={
        "console_scripts": [
            "run_tests=diploma_project.tests:main",
        ],
    },
)
