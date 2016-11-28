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

from jupyterhub.auth import PAMAuthenticator
import pamela
from tornado import gen

class KerberosPAMAuthenticator(PAMAuthenticator):
    @gen.coroutine
    def authenticate(self, handler, data):
        """Authenticate with PAM, and return the username if login is successful.

        Return None otherwise.

        Establish credentials when authenticating instead of reinitializing them
        so that a Kerberos cred cache has the proper UID in it.
        """
        username = data['username']
        try:
            pamela.authenticate(username, data['password'], service=self.service, resetcred=pamela.PAM_ESTABLISH_CRED)
        except pamela.PAMError as e:
            if handler is not None:
                self.log.warning("PAM Authentication failed (%s@%s): %s", username, handler.request.remote_ip, e)
            else:
                self.log.warning("PAM Authentication failed: %s", e)
        else:
            return username

c.JupyterHub.authenticator_class = KerberosPAMAuthenticator
