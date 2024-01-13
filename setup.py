from setuptools import setup, find_packages

setup(
    name='phishing_campaign_tool',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pytest>=6.0.0',
        'scapy>=2.4.0',
    ],
    entry_points={
        'console_scripts': [
            'generate_email_list=scripts.generate_email_list:generate_email_list',
            'run_campaign=scripts.run_campaign:run_campaign',
        ],
    },
    author='Tom Souillard',
    author_email='tom.souillard@gmail.com',
    description='A comprehensive Python package designed to create and manage phishing campaigns using email and Scapy.',
    license='Apache License 2.0',
    keywords='phishing campaign security pentest email scapy',
    url='https://github.com/Tom-Souillard/phishing_campaign_tool',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Security',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
