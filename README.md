# jupyterhub-example-kerberos

A proving ground for configuring JupyterHub to work with Kerberos.

This project exists to help you (and us) learn how JupyterHub and Kerberos can
interoperate. It will never provide an out-of-the-box, production-ready
experience.

At the moment, it is very much a work in progress. If you have experience
configuring JupyterHub with Kerberos, please jump in and help us out!

## Goals

* [x] Two local users (principals), `alice` and `bob` can successfully log into
  JupyterHub when it is configured with PAM backed by Kerberos.
* [x] The two users automatically receive a Kerberos ticket granting ticket
  (TGT) upon Hub login.
* [x] The TGT resides in an on-disk credential cache (ccache) which is
  read-write accessible by the owner alone.
* [x] The users can refresh the TGT with the `kinit` command from within any
  terminal or Python notebook.
* [x] The users can create keytab files with the `kutil` command from within
  any terminal or Python notebook.
* [x] All other JupyterHub functions behave as expected: starting notebook
  servers, stopping notebook servers, logging out, admin functions, etc.
* [x] The above works with the following spawners:
    * [x] default spawner
    * [x] sudospawner
    * [ ] your contribution welcome!

## Running

Start a KDC container and two JupyterHub containers, one using the default
local spawner and the other the sudo spawner, by running `docker-compose up`.

Visit http://localhost:8000 to access the JupyterHub instance running as `root`
and configured with the local spawner. Visit http://localhost:8001 to access
the instance running as `jupyter` and configured with the sudo spawner. Login
to either instance with username `alice` or `bob` with a password matching the
username.

Click New &rarr; Terminal to start a terminal session. View the ticket granting
ticket received during login by running `klist`. Renew the TGT by running
`kinit -R`.

Generate a keytab by running the following commands, substituting `bob` for
`alice` if you logged into JupyterHub with that user instead.

```bash
ktutil
addent -password -p alice@KDC.LOCAL -k 1 -e rc4-hmac
wkt /home/alice/.keytab
```

Show the contents of the keytab by running `klist -k ~/.keytab`.
