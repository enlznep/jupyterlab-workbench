# JupyterLab Workbench

JupyterLab Workbench is an opensource software with pre-installed JupyterLab and essential packages intended for corporations, researchers, scientists, students, educators, and etc.

List of pre-installed packages:
- Pillow
- Bash Kernel
- IPython
- IPyWidgets
- JupyterHub LDAP Authenticator
- MGLearn
- Numpy
- Pandas
- Scikit-learn
- SciPy
- ...more
---

## Installation ##

You can install it from pip with:
```
pip install jupyterlab-workbench
```
---
## Usage ##

After the install, rebuild the workbench
```
jlwb build
```

Generate a `jupyterhub_config.py` file
```
jlwb generate_config
```

Start the JupyterLab-Workbench
```
jlwb start -f <path/to/generated_config>
```

For more information
```
jlwb help
```
---
## Deployment ##
Edit the generated config file and uncomment the following block
```
c.JupyterHub.spawner_class = 'systemdspawner.SystemdSpawner'
c.SystemdSpawner.default_shell = '/bin/bash'
c.SystemdSpawner.unit_extra_properties = {'LimitMEMLOCK': 'infinity'}
```

Create a systemd environment file: `jlwb.env`
```
PATH=$PATH:/path/to/env/bin

# for FreeIPA (optional)
AUTH_TYPE='freeipa'
LDAP_SERVER_HOST='freeipa.example.com'
LDAP_BIND_USER_DN='uid=imauser,cn=users,cn=accounts,dc=example,dc=com'
LDAP_BIND_USER_PASSWORD='imapasssword'
LDAP_USER_SEARCH_BASE='cn=users,cn=accounts,dc=example,dc=com'
LDAP_USER_SEARCH_FILTER='(&(objectClass=person)(uid={username}))'

# for OpenLDAP (optional)
AUTH_TYPE='openldap'
LDAP_SERVER_HOST='openldap.example.com'
LDAP_BIND_USER_DN='uid=imauser,ou=People,dc=example,dc=com'
LDAP_BIND_USER_PASSWORD='iampassword'
LDAP_USER_SEARCH_BASE='ou=People,dc=example,dc=com'
LDAP_USER_SEARCH_FILTER='(&(objectClass=posixAccount)(uid={username}))'
```

Create a systemd service file: `jlwb.service`
```
vi /etc/systemd/system/jlwb.service
```
```
[Unit]
Description=JupyterLab Workbench
After=syslog.target network.target

[Service]
User=root
EnvironmentFile=/path/to/jlwb.env
StandardOutput=file:/path/to/log/jlwb.sysout.log
ExecStart=/path/to/env/bin/jlwb start -f /path/to/jupyterhub_config.py

Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```
Start JupyterLab Workbench
```
systemctl daemon-reload
systemctl start jlwb.service
systemctl enable jlwb.service
systemctl status jlwb.service
```
---
## Development ##

Clone the project
```
git clone git@github.com:enlznep/jupyterlab-workbench.git
```

Create a virtualenv
```
python -m virtualenv env
source env/bin/activate
```

Install the package
```
pip install .
```
