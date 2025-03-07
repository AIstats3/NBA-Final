try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    "description": "movement",
    "author": "Neil Seward",
    "author_email": "sealneaward@gmail.com",
    "version": "0.0.1",
    "packages": find_packages(),
    "install_requires": ["pandas", "tqdm", "matplotlib", "seaborn", "numpy", "scipy", "mpl_toolkits"],
    "name": "movement",
}

setup(**config)
