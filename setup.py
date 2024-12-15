from setuptools import setup, find_packages

setup(
    name="pypro",
    version="0.1.0",
    description="A python project template.",
    author="You Zhou",
    author_email="zhouyou.xy@gmail.com",
    packages=find_packages(),  # Automatically find packages in the project
    install_requires=[],  # Add dependencies here (or use requirements.txt)
    entry_points={
        "console_scripts": [
            "pypro=pypro.main:main",  # Enables running `pypro` from the command line
        ]
    },
)
