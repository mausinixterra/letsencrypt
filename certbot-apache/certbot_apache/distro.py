def override(method):
    """Outmost decorator wrapper to get the parameter"""
    def override_caller(caller):
        """Inner wrapper to get the caller"""
        def override_args(caller, *args, **kwargs):
            """Check if distro specific class overrides called method, return
            overriding method if found, in other case, return the default"""
            try:
                # Try to find overriding method
                return getattr(caller.os_info, method)(*args, **kwargs)
            except AttributeError:
                # Override not found, return the default
                return getattr(caller, method)(*args, **kwargs)
        return override_args
    return override_caller
