from distutils.core import setup
setup(
  name = 'adsk',         # How you named your package folder (MyLib)
  packages = ['adsk'],   # Chose the same as "name"
  version = '2.0.12157',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Autodesk API Library to aid in developing scrips and Add Ins for Fusion 360 in a virtural environment',   # Give a short description about your library
  author = 'Danno Peters',                   # Type in your name
  author_email = 'Danno@DannoPeters.ca',      # Type in your E-Mail
  url = 'https://github.com/DannoPeters/adsk',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/DannoPeters/adsk/archive/refs/tags/v_2.0.12157.tar.gz',    # I explain this later on
  keywords = ['AutoDesk', 'Fusion360', 'CAD', 'Computer Aided Design', 'Automation', 'API', 'Fusion', 'CAD-CAM', 'Design'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Manufacturing',      # Define that your audience are developers
    'Topic :: Scientific/Engineering',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
