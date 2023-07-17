import os
from setuptools import setup, find_packages
import sys
import subprocess

here = os.path.abspath(os.path.dirname(__file__))
import codecs

requires = ['Django', 'django-import-export', 'django-author']

# version = subprocess.check_output(['git','describe','--abbrev=0','--tags']).decode("utf-8")
version = '1.1.6.4'

setup(
        name='django-import-export-celery',
        version=version,
        author='Timothy Hobbs',
        author_email='timothy.hobbs@auto-mat.cz',
        url='https://github.com/auto-mat/django-import-export-celery',
        download_url="http://pypi.python.org/pypi/django-import-export-celery/",
        description="Process long running django imports and exports in celery",
        long_description=codecs.open(
            os.path.join(
                here, 'README.rst'), 'r', 'utf-8').read(),
        license='License :: OSI Approved :: GNU Lesser General Public License v3.0 or later (LGPLv3.0+)',
        install_requires=requires,
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        classifiers=['Topic :: Utilities',
                     'Natural Language :: English',
                     'Operating System :: OS Independent',
                     'Intended Audience :: Developers',
                     'Environment :: Web Environment',
                     'Framework :: Django',
                     'Programming Language :: Python :: 3.3',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5'],
)
