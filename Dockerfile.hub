FROM ubuntu:14.04

# Create local user accounts
RUN adduser alice --gecos --disabled-password && \
    adduser bob --gecos --disabled-password && \
    adduser jupyter --gecos --disabled-password

RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        libpam-krb5 \
        krb5-user \
        wget \
        bzip2 \
        ca-certificates

# Install miniconda to get jupyterhub
RUN wget -q https://repo.continuum.io/miniconda/Miniconda3-4.2.12-Linux-x86_64.sh -O /tmp/miniconda.sh  && \
    echo 'd0c7c71cc5659e54ab51f2005a8d96f3 */tmp/miniconda.sh' | md5sum -c - && \
    bash /tmp/miniconda.sh -f -b -p /opt/conda && \
    rm /tmp/miniconda.sh

RUN /opt/conda/bin/conda install --yes -c conda-forge \
    python=3.5 \
    notebook=5.0.0 \
    idna=2.5 \
    jupyterhub=0.7.2 \
    'pamela>=0.3' \
    sudospawner=0.4.1 && \
    /opt/conda/bin/conda clean -tipsy

# Configure kerberos
COPY krb5.conf /etc/
COPY kdc.conf /etc/krb5kdc/

# PAM_KRB5CCNAME is not set when opening the session for some reason and so we have to
# explicitly retain the cache created during auth instead.
# Also, turn on pam debug logging
RUN sed -i 's$1000$1000 ccache=/tmp/krb5cc_%u retain_after_close debug$' /etc/pam.d/common-auth
RUN sed -i 's$1000$1000 debug$' /etc/pam.d/common-session

# Setup for the sudospawner case
RUN mkdir -p /opt/jupyterhub && \
    chown jupyter:jupyter /opt/jupyterhub && \
    echo 'jupyter ALL=(ALL:ALL) NOPASSWD:/opt/conda/bin/sudospawner' >> /etc/sudoers

# Add the jupyterhub config
COPY jupyterhub_config.py /opt/jupyterhub/
COPY jupyterhub_sudo_config.py /opt/jupyterhub/
COPY hub.sh /opt/jupyterhub/

# Add custom sudospawner script
COPY sudospawner-singleuser /opt/conda/bin/

EXPOSE 8000
WORKDIR /opt/jupyterhub
CMD ["./hub.sh"]
