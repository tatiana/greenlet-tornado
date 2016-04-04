from setuptools import setup, find_packages

try:
    README = open('readme.md').read()
except IOError:
    README = "An easy way to seamlessly use Greenlet with Tornado"

setup(name="greenlet_tornado",
      author="jphaas1, simonrad, rodsenra, tati_alchueyr (tatiana)",
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python'],
      download_url = 'http://pypi.python.org/pypi/greenlet_tornado',
      description=u"An easy way to seamlessly use Greenlet with Tornado",
      include_package_data=True,
      install_requires=["greenlet==0.4.9", "pycurl==7.43.0", "tornado>=3.2"],
      license="MIT License",
      long_description=README,
      packages=find_packages(),
      tests_require=["coverage==3.6", "nose==1.3.7", "mock==1.0.1", "tornado-cors"],
      url = "http://github.com/tatiana/greenlet_tornado",
      version="1.1.2"
)
