from setuptools import setup


setup(
    name='loockup_dictionary',
    version=0.1,
    description='Loockup dictionary module',
    author='',  # author name
    author_email='',
    packages=[
        'loockup_dictionary',
    ],
    include_package_data=True,
    install_requires=[
        'pymouse==1.0',
        'pyperclip==1.5.27',
        'pyobjc==4.0',
        'pyobjc-core==4.0',
        'pynput==1.3.7',

    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
