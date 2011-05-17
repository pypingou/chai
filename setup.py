from distutils.core import setup

setup(
    name='chai',
    version='0.1.6',
    author='Vitaly Babiy, Aaron Westendorf',
    author_email="vbabiy@agoragames.com, aaron@agoragames.com",
    packages=['chai'],
    url='https://github.com/agoragames/chai',
    license='LICENSE.txt',
    description="Easy to use mocking/stub framework.",
    long_description=open('README.rst').read(),
    keywords=['python', 'test', 'mock'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        "Intended Audience :: Developers",
        "Operating System :: POSIX",
        "Topic :: Communications",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
    ]
)
