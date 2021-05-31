from setuptools import setup

setup(
    name='sdr_availability',
    version='0.1',
    description='sdr_availability',
    url='ht',
    author='Ena Vu',
    author_email='ena@enavu.io',
    license='MIT',
    packages=['sdr_availability'],
    install_requires=[
        'pandas'
    ],
    python_requires='>=3.6',
    zip_safe=False)