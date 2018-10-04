#!/usr/bin/env python3

from setuptools import setup
import versioneer

PROJECT = 'Joule'

# Change docs/sphinx/conf.py too!

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version = versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Process manager for embedded systems',
    long_description=long_description,

    author='John Donnal',
    author_email='donnal@usna.edu',

    url='https://git.wattsworth.net/wattsworth/example_modules.git',
    download_url='[none]',

    classifiers=['Programming Language :: Python',
                 'Environment :: Console',
                 ],
    platforms=['Any'],
    scripts=[],
    provides=[],
    install_requires=['click',
                      'treelib',
                      'numpy',
                      'scipy',
                      'psutil',
                      'requests',
                      'aiohttp',
                      'markdown',
                      'BeautifulSoup4',
                      'dateparser',
                      'tabulate',
                      'sqlalchemy',
                      'aiohttp-jinja2',
                      'jinja2',
                      'joule'],
    namespace_packages=[],
    packages=['jouleexamples'],
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'joule-example-reader = jouleexamples.example_reader:main',
            'joule-high-bandwidth-reader = jouleexamples.high_bandwidth_reader:main',
            'joule-example-filter = jouleexamples.example_filter:main',
            'joule-example-median-filter = jouleexamples.median_filter:main',
            'joule-example-composite = jouleexamples.example_composite:main',
            'joule-example-interface = jouleexamples.example_interface:main',
            'joule-bootstrap-interface = jouleexamples.bootstrap_interface:main'
        ]
    },
    zip_safe=False,
)
