import sys

from distutils.core import setup, Extension

incDirs = ['../libspeex', '../include/speex']
libs = ['speex']
libDirs = []
runtimeLibDirs = []
cMacros = []
extraLinkArgs = ['-g']

if sys.platform == 'win32':
    libDirs.append('..\\win32\\Release')
    libs = []
    extraLinkArgs = ['..\\win32\\libspeex\\Release\\libspeex.lib']

speexmodule = Extension('speex',
                        sources = ['speex.c'],
                        define_macros=cMacros,
                        include_dirs=incDirs,
                        libraries=libs,
                        library_dirs=libDirs,
                        runtime_library_dirs=runtimeLibDirs,
                        extra_compile_args=['-g'],
                        extra_link_args=extraLinkArgs
                        )

setup(name = 'speex',
      version = '1.0',
      description = 'Python interface to the Speex audio codec',
      ext_modules = [speexmodule],
      )
