# Databricks notebook source
from setuptools import setup, find_packages
  


setup(name='pitest',
      version='0.6',
      description='Databricks TPC-DI',
      long_description='Simple package to test wheel file jobs on Databricks',
      keywords='pi test',
      url='https://github.com/balbarka/pi_test',
      author='Brad Barker',
      author_email='brad.barker@databricks.com',
      license='Databricks',
      packages=find_packages(),
      install_requires=[],
      include_package_data=True,
      zip_safe=True)
