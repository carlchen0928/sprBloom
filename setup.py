from distutils.core import setup

ext_files = ['sprBloom/bloom.c']

kwargs = {}

try:
    from Cython.Distutils import build_ext
    from Cython.Distutils import Extension
    print 'Building from Cython'
    ext_files.append('sprBloom/sprBloom.pyx')
    kwargs['cmdclass'] = {'build_ext': build_ext}
except ImportError:
    from distutils.core import Extension
    ext_files.append('sprBloom/sprBloom.c')
    print 'Building from C'


ext_modules = [Extension('sprBloom', ext_files, libraries=['hiredis'])]


setup(
    name = "sprBloom",
    version = '1.0.0',
    author = "Yiyu Chen",
    author_email = "chen_yiyu@foxmail.com",
    license = "MIT License",
    ext_modules = ext_modules,
    classifiers = [
        'Intended Audience :: Developers', 
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: C', 
        'Programming Language :: Cython', 
        'Topic :: Sofeware Development :: Libraries :: Python Modules',
    ],
    **kwargs
)
