FROM ubuntu:14.04

# Make a directory for logs
RUN mkdir -p /var/log/kerberos

# Install the admin and KDC packages
RUN apt-get update && \
    apt-get install --no-install-recommends -y krb5-kdc krb5-admin-server

# Write configuration and start script
COPY krb5.conf /etc/
COPY kdc.conf /etc/krb5kdc/
COPY kdc.sh /

# Create the master key
RUN kdb5_util -P 'masterkey' -r KDC.LOCAL create -s
# Create principals for the notebook users
RUN kadmin.local -q "addprinc -pw alice alice"
RUN kadmin.local -q "addprinc -pw bob bob"

CMD ["/kdc.sh"]
