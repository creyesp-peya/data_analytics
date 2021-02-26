from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = [k for k in f.readlines()]

setup(
    name='data_analytics',
    version='0.1',
    description='Data Analytics',
    long_description='',
    long_description_content_type="text/markdown",
    author='Analytic Factory',
    author_email='analytic.factory@pedidosya.com',
    packages=find_packages(include=['data_analytics/']),
    url=None,
)
