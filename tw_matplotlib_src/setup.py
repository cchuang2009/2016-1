# encoding: utf8
from distutils.core import setup
from setuptools import find_packages
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['matplotlib']

setup(name='tw_matplotlib_src',
      version='1.0.0',
      description='matplotlib Taiwanized setting',
      author='cchuang',
      author_email='cchuang2009@gmail.com',
      url='https://github.com/cchuang2009/tw_matplotlib_src',
      long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT License',
      packages=find_packages(),
      install_requires=install_requires,
      include_package_data=True,
      package_data={
          'tw_matplotlib': ['fonts/*'],
      })
