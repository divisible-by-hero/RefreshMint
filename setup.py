from setuptools import setup, find_packages

setup(
    name='RefreshMint',
    version='0.1.0',
    zip_safe = False,
    packages=find_packages(exclude=['example']),
    include_package_data=True,
    url='https://github.com/divisible-by-hero/RefreshMint',
    license='MIT',
    author='Garrett Pennington, Derek Stegelman, Jon Faustman',
    author_email='garrettp@gmail.com',
    description='RefreshMint is an open-source starter kit for creating your own Refresh communities.',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        "Framework :: Django",
    ],
    install_requires=[]
)

