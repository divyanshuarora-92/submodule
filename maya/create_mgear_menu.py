from maya import cmds
from pymel import mayautils
import pymel.core as pm
from cvwrap.menu import create_menuitems

from impeller.imp_libs.pathlib3 import Path
from impeller import packager


def append_plugin_path():
    maya_version = pm.about(version=True)

    root = Path(__file__).parent.absolute()
    plugin_win = root / 'platforms' / maya_version / 'windows' / 'x64' / 'plug-ins'
    plugin_lin = root / 'platforms' / maya_version / 'linux' / 'x64' / 'plug-ins'
    plugin_mac = root / 'platforms' / maya_version / 'osx' / 'x64' / 'plug-ins'

    evar = packager.Evar(name='MAYA_PLUG_IN_PATH', win=plugin_win, lin=plugin_lin, mac=plugin_mac, action='append')
    evar.commit()


def mGear_menu_loader():
    """Create mGear menu"""

    # Install mGear Menu
    import mgear
    mgear.install()

    # Install Shifter Menu
    import mgear.shifter.menu
    mgear.shifter.menu.install()

    # Install Simple Rig Menu
    import mgear.simpleRig.menu
    mgear.simpleRig.menu.install()

    # Install Rigbits Menu
    import mgear.rigbits.menu
    mgear.rigbits.menu.install()

    # Install Skinning Menu
    import mgear.core.menu
    mgear.core.menu.install_skinning_menu()

    # Install Animbits Menu
    import mgear.animbits.menu
    mgear.animbits.menu.install()

    # Install Synoptic Menu
    import mgear.crank.menu
    mgear.crank.menu.install()

    # Install Synoptic Menu
    import mgear.synoptic.menu
    mgear.synoptic.menu.install()

    # Install Flex Menu
    import mgear.flex.menu
    mgear.flex.menu.install()

    # Install Utilities Menu
    import mgear.menu
    m = mgear.menu.install_utils_menu()
    mgear.core.menu.install_utils_menu(m)
    mgear.rigbits.menu.install_utils_menu(m)

    # Install Help Menu
    mgear.menu.install_help_menu()


append_plugin_path()
if not cmds.about(batch=True):
    mayautils.executeDeferred(mGear_menu_loader)
    mayautils.executeDeferred(create_menuitems)
