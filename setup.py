from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='forty',
      version='0.1',
      description='Time tracker',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities'
      ],
      url='https://github.com/vikian050194/forty',
      author='Kirill Vinogradov',
      author_email='vikian050194@gmail.com',
      license='MIT',
      packages=find_packages(where='.', exclude=['tests*'], include='*'),
      install_requires=[],
      test_suite='nose.collector',
      tests_require=['nose'],
      # scripts=['bin/forty'],
      entry_points = {
        'console_scripts': ['forty=forty.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
