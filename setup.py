import os
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django-simplemde',
    version='0.1.2',
    description='django-simplemde is a WYSIWYG markdown editor for Django',
    long_description=readme,
    author="Siyuan Zhang",
    author_email='onepill@gmail.com',
    url='https://github.com/onepill/django-simplemde',
    license='MIT',
    packages=['simplemde'],
    include_package_data=True,
    install_requires=['setuptools'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords='django,admin,wysiwyg,markdown,editor,simplemde',
)
