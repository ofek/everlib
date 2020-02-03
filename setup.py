from setuptools import find_packages, setup


def get_version():
    with open('everlib/__init__.py', 'r') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.strip().split('=')[1].strip(' \'"')


def get_long_description():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()


setup(
    name='everlib',
    version=get_version(),
    description='Everlasting media library backed by cloud storage',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    keywords=['plex', 'calibre', 'media', 'kubernetes', 'cloud', 'storage', 'filesystem'],
    url='https://github.com/ofek/everlib',
    project_urls={
        'Documentation': 'https://ofek.dev/everlib',
        'Source Code': 'https://github.com/ofek/everlib',
        'Bug Tracker': 'https://github.com/ofek/everlib/issues',
    },
    author='Ofek Lev',
    author_email='ofekmeister@gmail.com',
    license='Apache-2.0 OR MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Multimedia',
        'Topic :: System :: Archiving :: Mirroring',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities',
    ],
    packages=find_packages(include=['everlib', 'everlib.*']),
    python_requires='>=3.6',
    install_requires=[
        'appdirs',
        'atomicwrites',
        'binary',
        'click',
        'colorama',
        'pyperclip>=1.7.0',
        'pytz>=2018.7',
        'PyYAML>=3.13',
        'requests',
        'toml>=0.10.0',
        'tzlocal>=1.5.1',
    ],
    entry_points={'console_scripts': ['everlib = everlib.cli:everlib']},
    include_package_data=True,
)
