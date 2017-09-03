import filecmp
import os

from certbot import errors

class Override(object):
    """Baseclass for overrides"""
    def __init__(self, config):
        self.config = config

class OverrideDebian(Override):
    def __init__(self, *args, **kwargs):
        super(OverrideDebian, self).__init__(*args, **kwargs)

    def is_site_enabled(self, avail_fp):
        """Checks to see if the given site is enabled.

        .. todo:: fix hardcoded sites-enabled, check os.path.samefile

        :param str avail_fp: Complete file path of available site

        :returns: Success
        :rtype: bool

        """
        enabled_dir = os.path.join(self.config.parser.root, "sites-enabled")
        if not os.path.isdir(enabled_dir):
            error_msg = ("Directory '{0}' does not exist. Please ensure "
                         "that the values for --apache-handle-sites and "
                         "--apache-server-root are correct for your "
                         "environment.".format(enabled_dir))
            raise errors.ConfigurationError(error_msg)
        for entry in os.listdir(enabled_dir):
            try:
                if filecmp.cmp(avail_fp, os.path.join(enabled_dir, entry)):
                    return True
            except OSError:
                pass
        return False
