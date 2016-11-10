# jupyterhub-example-kerberos

A proving ground for configuring JupyterHub to work with Kerberos.

This project exists to help you (and us) learn how JupyterHub and Kerberos can interoperate. It will never provide an out-of-the-box, production-ready experience.

At the moment, it is very much a work in progress. If you have experience configuring JupyterHub with Kerberos, please jump in and help us out!

## Goals

* [ ] Two local users (principals), `alice` and `bob` can successfully log into JupyterHub when it is configured with PAM backed by Kerberos.
* [ ] The two users automatically receive a Kerberos ticket granting ticket (TGT) upon Hub login.
* [ ] The on-disk credential cache (ccache) for each user is read-write accessible by the owner alone and without additional user action.
* [ ] The users can refresh the TGT with the `kinit` command.
* [ ] The users can request a ticket for a service princpal named `service` using the `kvno` command.
* [ ] TODO: keytabs?
* [ ] All other JupyterHub functions behave as expected: starting notebook servers, stopping notebook servers, logging out, admin functions, etc.
* [ ] The above works with the following spawners:
    * [ ] default spawner
    * [ ] sudospawner
    * [ ] (your contribution welcome!)
