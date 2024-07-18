from setuptools import setup, find_packages

setup(
	name='kwresearch',
	version='0.2.0',
	packages=find_packages(),
	install_requires=[
        "aiohttp",
        "requests",
        "python-dotenv",
	],
	author='Chinmay Shrivastava',
	license='MIT'
)