from setuptools import setup

setup(
    name="delete-entities",
    version="0.1.0",
    description="Deletes entities from Datastore",
    url="https://github.com/[your-username]/delete-entities",
    author="Denis Santos",
    author_email="denissys@gmail.com",
    license="MIT",
    packages=["delete_entities"],
    python_requires=">=3.8",
    install_requires=["google-cloud-datastore","logging"],
    tests_require=["pytest"],
    entry_points={
        "console_scripts": ["delete-entities=delete_entities.main:main"],
    },
)
