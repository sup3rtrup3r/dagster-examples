import setuptools

setuptools.setup(
    name="zitarice",
    packages=setuptools.find_packages(exclude=["zitarice_tests"]),
    install_requires=[
        "dagster==0.11.14",
        "dagit==0.11.14",
        "pytest",
    ],
)
