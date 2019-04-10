from setuptools import setup

setup(name='youtube-url-scraper',
      version='1.1',
      description='Python script to scrape videos urls on any YouTube page',
      url='https://github.com/zvk/youtube_url_scraper',
      author='Zack Zukowski',
      author_email='zack@pex.com',
      license='MIT',
      packages=[
        'youtube_url_scraper'
      ],
      install_requires=[
        'apscheduler',
        'gitpython',
        'datetime',
        'bs4',
        'requests'
      ])
