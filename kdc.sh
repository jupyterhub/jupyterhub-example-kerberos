#!/bin/bash

/etc/init.d/krb5-kdc start
/etc/init.d/krb5-admin-server start
tail -F /var/log/kerberos/krb5kdc.log
