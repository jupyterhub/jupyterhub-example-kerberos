#!/bin/bash

# Run the syslog service so that we can see PAM Kerberos logging
/etc/init.d/rsyslog start

# Run JupyterHub
source /opt/conda/bin/activate /opt/conda
exec jupyterhub -f jupyterhub_config.py --no-ssl
