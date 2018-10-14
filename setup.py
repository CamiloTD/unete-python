from distutils.core import setup
setup(
  name = 'unete',         
  packages = ['unete'],   
  version = '1.1.1',      
  license='MIT',        
  description = 'Unete client for Python, access remote methods with native syntax.',   
  author = 'CamiloTD',                   
  author_email = 'camilotd1999@gmail.com',      
  url = 'https://github.com/CamiloTD/unete-python',   
  download_url = 'https://github.com/CamiloTD/unete-python/archive/1.0.tar.gz',    
  keywords = ['unete', 'microservices', 'remote', 'native', 'api'],   
  install_requires=['edict'],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)