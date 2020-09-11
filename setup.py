import os

__location__ = os.path.dirname(__file__)

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='spark-df-profiling',
    version='1.1.13',
    version='1.2.0',
    author='Julio Antonio Soto de Vicente',
    author_email='julio@esbet.es',
    packages=['spark_df_profiling'],
    url='https://github.com/julioasotodv/spark-df-profiling',
    license='MIT',
    description='Create HTML profiling reports from Apache Spark DataFrames',
    install_requires=[
        "pandas>=0.17.0",
        "pandas>=0.25",
        "matplotlib>=1.4",
        "jinja2>=2.8",
        "six>=1.9.0"
    ],
    include_package_data = True,
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Build Tools',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Framework :: IPython',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='spark pyspark report big-data pandas data-science data-analysis python jupyter ipython',
)