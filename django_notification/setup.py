from distutils.core import setup

setup(
  name = 'django-pack-notification',
  version = '0.1',
  description = 'Permite comunicar django con slack',
  author = 'Eliacer Fernandez Guevara',
  author_email = 'eliacer.fernandez@upeu.edu.pe',
  url = 'https://github.com/eliacer95/dn-django-notification', # use the URL to the github repo
  download_url = 'https://github.com/eliacer95/dn-django-notification/tarball/0.1',
  keywords = ['django', 'slack'],
  classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python  :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Environment :: Other Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: Python Modules",
  ],
)