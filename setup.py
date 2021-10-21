from pathlib import Path
from setuptools import setup


DIRECTORY = Path(__file__).parent
DESCRIPTION = (DIRECTORY / "README.md").read_text()


setup(
    name='jupyterlab-workbench',
    version='0.1.3',
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/enlznep/pyexample',
    author='Ray Marc Marcellones (XTREME-D Inc)',
    author_email='devops@xtreme-d.net',
    license='GPLv3+',
    scripts=['bin/jlwb'],
    python_requires='>=3.6',
    packages=['jupyterlab_workbench'],
    install_requires=[
        'Pillow==8.4.0',
        'bash-kernel==0.7.2',
        'ipympl==0.8.0',
        'ipython==7.28.0',
        'ipywidgets==7.6.5',
        'jupyterhub-idle-culler==1.2',
        'jupyterhub-ldap-authenticator==0.4.1',
        'jupyterhub-systemdspawner==0.15.0',
        'jupyterhub==1.4.2',
        'jupyterlab-templates==0.3.0',
        'jupyterlab==3.2.0',
        'matplotlib==3.4.3',
        'mglearn==0.1.9',
        'numpy==1.21.2',
        'pandas==1.3.4',
        'pycurl==7.44.1',
        'scikit-learn==1.0',
        'scipy==1.7.1',
    ],
    classifiers=[
        'Framework :: Jupyter :: JupyterLab :: 3',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)
