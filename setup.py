from setuptools import setup, find_packages

setup(
    name="blue-eagle",
    version="1.0.0",
    author="HUBAX Team",
    author_email="n0merc@hubax.team",
    description="Bluetooth Spammer Tool for Security Testing",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/blue-eagle",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Topic :: Security",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pybluez==0.23",
        "colorama==0.4.6",
    ],
    entry_points={
        'console_scripts': [
            'blue-eagle=blue_eagle_spammer:main',
        ],
    },
)
