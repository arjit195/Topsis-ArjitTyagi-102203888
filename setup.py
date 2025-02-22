from distutils.core import setup
setup(
  name = 'Topsis-Arjit-102203888',         # How you named your package folder (MyLib)
  packages = ['topsis'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A Python package to perform TOPSIS analysis',   # Give a short description about your library
  author = 'Arjit Tyagi',                   # Type in your name
  author_email = 'arjittyagi195@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/arjit195/Topsis-Arjit-102203888',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/arjit195/Topsis-Arjit-102203888/archive/refs/tags/v_01.tar.gz',    # I explain this later on
  long_description=open("README.md").read(),
  long_description_content_type="text/markdown",
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      ],
  entry_points={
        'console_scripts': [
            'topsis=Topsis.topsis:main',  # Entry point for CLI usage
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
