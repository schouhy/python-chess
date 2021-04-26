from setuptools import setup

setup(
    name="chess",
    version=chess.__version__,
    author="Sergio Chouhy",
    author_email="sergio.chouhy@gmail.com",
    description="Minitchess variant of python-chess",
    license="GPL-3.0+",
    url="https://github.com/schouhy/python-chess.git",
    packages=["chess"],
    zip_safe=False, 
)
