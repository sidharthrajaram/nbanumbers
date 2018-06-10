from setuptools import setup

setup(name='nbanumbers',
      version='0.8',
      description='nba stats retrieval package',
      url='http://github.com/sidharthrajaram/nbanumbers',
      author='Sid Rajaram',
      author_email='tmzturtle@gmail.com',
      license='MIT',
      packages=['nbanumbers'],
      install_requires=['google-api-python-client','pandas',
      'urllib3','bs4','requests','numpy','regex'],
      zip_safe=False)

