from setuptools import setup

setup(name='mypackage',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description='Package to test python packaging opions and functionality',
      url='http://github.com/mheikenfeld/package_testing',
      author='Max Heikenfeld',
      author_email='maxheikenfeld@web.de',
      license='MIT',
      packages=['mypackage','mypackage.subpackageb', 'mypackage.subpackage_A'],
      install_requires=[],
      zip_safe=False)
