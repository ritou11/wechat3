#!/usr/bin/env python

from setuptools import setup, find_packages
from wechat import VERSION

url = "https://github.com/ritou11/wechat3.git"

long_description = "Wechat Python3 SDK"

setup(name="wechat",
      version=VERSION,
      description=long_description,
      maintainer="ritou11",
      maintainer_email="ritou11@gmail.com",
      url=url,
      long_description=long_description,
      install_requires=['requests'],
      packages=find_packages('.'),
      )
