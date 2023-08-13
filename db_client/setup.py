from setuptools import setup

REQUIRES = [
    'records',
    'requests',
    'structlog',
    'allure-pytest'
]

setup(
    name='db_client',
    version='0.0.1',
    packages=['db_client'],
    url='https://github.com/GalinaN-create/db_client.git',
    license='MIT',
    author='Galina Nosova',
    author_email='-',
    install_requires=REQUIRES,
    description='db_client'
)
