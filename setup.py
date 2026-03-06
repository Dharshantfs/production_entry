
from setuptools import setup, find_packages

setup(
	name='production_entry',
	version='0.0.1',
	description='Integrated Production Entry for Multi-Width Fabric Manufacturing',
	author='Your Company',
	author_email='info@yourcompany.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=['frappe'],
)
