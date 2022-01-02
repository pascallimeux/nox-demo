# setup.py
import setuptools

setuptools.setup(
    name="mylib",
    version="0.0.1",
    author="pascal Limeux",
    author_email="pascal.limeux@orange.com",
    description="exemple de package",
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(include=['mylib']),
        entry_points = {
        'console_scripts': ['ola=mylib.hello:main'],
    },
)
