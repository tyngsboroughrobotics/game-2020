'''
Call functions from the `libwallaby` C library from Python. See the `libwallaby`
documentation for a list of available functions.
'''

from ctypes import cdll

try:
    libwallaby = cdll.LoadLibrary("/usr/lib/libwallaby.so")
except OSError:
    from sys import argv

    if '--ignore-no-libwallaby' not in argv:
        print('WARNING: Could not load the libwallaby library. Make sure you\'re running on a robot and not on your local machine.')

    class _libwallaby_noop(object):
        def __getattr__(self, name):
            if '--ignore-no-libwallaby' not in argv:
                print(f'WARNING: Attempted to call libwallaby.{name}, but the libwallaby library couldn\'t be loaded. Make sure you\'re running on a robot and not on your local machine.')

            def noop(*args, **kwargs):
                pass

            return noop

    libwallaby = _libwallaby_noop()
