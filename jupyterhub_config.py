# Set the Hub to listen on all interfaces in the container on port 8000
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000

# The authenticator can call pam_open_session before spawning a notebook server
# and pam_close_session when shutting one down. With pam_krb5, this results
# in a log message stating:
    # Nov 15 14:22:28 workbook python: pam_krb5(login:session):
    # (user bob) unable to get PAM_KRB5CCNAME, assuming non-Kerberos login
# most likely because the pam_authentication and pam_setcreds calls are
# happening in a wholly separate pam transaction where the env var is set.
# So opening sessions has no impact on Kerberos ticketing in the current Hub
# design for auth and spawn.
c.PAMAuthenticator.open_sessions = False

