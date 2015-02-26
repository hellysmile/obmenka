from setuptools import setup


classifiers = '''\
Programming Language :: Python :: 2
Operating System :: MacOS :: MacOS X
'''


description = 'Mac OS X UAH currency tracker'


py_modules = [
    'obmenka'
]


def long_description():
    f = open('README.rst')
    rst = f.read()
    f.close()
    return rst


setup(
    name='obmenka',
    version='0.1',
    py_modules=py_modules,
    description=description,
    long_description=long_description(),
    author='hellysmile',
    author_email='hellysmile@gmail.com',
    url='https://github.com/hellysmile/obmenka',
    zip_safe=False,
    install_requires=[
        'lxml',
        'requests',
        'pync'
    ],
    license='http://www.apache.org/licenses/LICENSE-2.0',
    classifiers=filter(None, classifiers.split('\n')),
    keywords=[
        'obmenka'
    ],
    entry_points={
        'console_scripts': [
            'obmenka = obmenka:main',
        ],
    }
)
