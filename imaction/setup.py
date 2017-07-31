from setuptools import setup, find_packages

version_parts = (0, 0, 1)
version = '.'.join(map(str, version_parts))

setup(
    name='imaction',
    version=version,
    keywords=('redux', 'action', 'multi-lang', 'interface', 'document'),
    description='Package for creating json based interfaces between different develop languages',
    license='MIT License',
    install_requires=['six>=1.10.0'],

    author='jacksing.Tang',
    author_email='iterrole@163.com',

    packages=find_packages(include=('imaction',)),
    platforms='any',
)
