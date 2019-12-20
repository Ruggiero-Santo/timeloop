from timeloop.exceptions import ServiceExit


def service_shutdown(signum, frame):
    """Utility function used as a callback function ti catch system signals and
    raise ServiceExit (custom Exception) to handle the stopping of all active
    jobs.
    """    
    raise ServiceExit
