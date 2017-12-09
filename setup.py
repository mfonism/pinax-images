from setuptools import find_packages, setup

LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-images.svg
    :target: https://pypi.python.org/pypi/pinax-images/

============
Pinax Images
============

.. image:: https://img.shields.io/pypi/v/pinax-images.svg
    :target: https://pypi.python.org/pypi/pinax-images/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://pypi.python.org/pypi/pinax-images/
.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-images.svg
    :target: https://circleci.com/gh/pinax/pinax-images
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-images.svg
    :target: https://codecov.io/gh/pinax/pinax-images
.. image:: https://img.shields.io/github/contributors/pinax/pinax-images.svg
    :target: https://github.com/pinax/pinax-images/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-images.svg
    :target: https://github.com/pinax/pinax-images/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-images.svg
    :target: https://github.com/pinax/pinax-images/pulls?q=is%3Apr+is%3Aclosed
.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/

``pinax-images`` is a Django app for managing collections of images associated with a content object.

Features
--------
* Good helpful stuff

Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+-----+
| Django \ Python | 2.7 | 3.4 | 3.5 | 3.6 |
+=================+=====+=====+=====+=====+
| 1.11            |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
| 2.0             |     |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="an app for managing collections of images associated with a content object",
    name="pinax-images",
    long_description=LONG_DESCRIPTION,
    version="3.0.0",
    url="http://github.com/pinax/pinax-images/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "images": []
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "django-appconf>=1.0.1",
        "django-imagekit>=3.2.7",
        "pilkit>=1.1.13",
        "pillow>=3.3.0",
        "pytz>=2016.6.1",
    ],
    tests_require=[
        "django-test-plus>=1.0.11",
        "mock>=2.0.0",
    ],
    test_suite="runtests.runtests",
    zip_safe=False
)
