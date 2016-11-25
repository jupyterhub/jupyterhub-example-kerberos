#!/bin/bash

# Run the syslog service so that we can see PAM Kerberos logging
# /etc/init.d/rsyslog start

# Run JupyterHub in the conda environment
source /opt/conda/bin/activate /opt/conda
exec jupyterhub --no-ssl $@
