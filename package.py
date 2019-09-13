from impeller.imp_libs.pathlib3 import Path


def getpackage(module=None):
    """ Using Pathlib2 to create handy paths """
    # Imports first
    mod = module
    if not mod: import packager as mod
    Evar = mod.Evar
    Package = mod.Package

    # Some useful variables:
    root = Path(__file__).parent.absolute()
    name = root.name

    # Package Tags
    tags = ['3d', 'maya', 'newversion']

    # Package instance( Name, Environ(), Path, [Tags] )
    pkg = Package(name, None, root, tags)

    # Environemnt vars
    pkg.env.add(Evar(name='MAYA_SCRIPT_PATH', win=root / 'maya', lin=root / 'maya', mac=root / 'maya', action='append'))
    pkg.env.add(Evar(name='PYTHONPATH', win=root / 'maya', lin=root / 'maya', mac=root / 'maya', action='append'))

    return pkg
