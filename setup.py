from distutils.core import setup

setup(
    name='expybox',  # How you named your package folder (MyLib)
    packages=['expybox'],  # Chose the same as "name"
    version='0.0.1',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Jupyter notebook toolbox for model interpretability/explainability',  # Give a short description about your library
    author='Jakub Štercl',  # Type in your name
    author_email='stercjak@fit.cvut.cz',  # Type in your E-Mail
    url='https://github.com/Kukuksumusu/expybox',  # Provide either the link to your github or to your website
    download_url='https://github.com/Kukuksumusu/expybox/archive/0.0.1.tar.gz',  # I explain this later on
    # keywords=['SOME', 'MEANINGFULL', 'KEYWORDS'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'shap',
        'pdpbox',
        'lime',
        'alibi',
        'numpy',
        'pandas',
        'ipywidgets'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3.7',
    ],
)
