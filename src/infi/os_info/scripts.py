def uname():
    from . import get_platform_string
    print get_platform_string()


def git_version():
    from . import get_version_from_git
    print get_version_from_git()


def git_short_version():
    from . import get_version_from_git, shorten_version_string
    print shorten_version_string(get_version_from_git())

