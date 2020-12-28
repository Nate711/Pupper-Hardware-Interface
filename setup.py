import setuptools

setuptools.setup(
    name="Pupper-Hardware-Interface",
    version="0.1",
    author="Nathan Kau",
    author_email="nathankau@gmail.com",
    description="Library for controlling servo-based Pupper",
    packages=["quadrupedcontroller"],
    install_requires=[
        "numpy",
        "pyyaml",
        "transforms3d",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
