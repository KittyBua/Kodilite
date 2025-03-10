#!/usr/bin/python
# -*- coding: utf-8 -*-

# ###########################################################################
#    Copyright (C) 2008 by Volker Christian                                #
#    Volker.Christian@fh-hagenberg.at                                      #
#                                                                          #
#    This program is free software; you can redistribute it and#or modify  #
#    it under the terms of the GNU General Public License as published by  #
#    the Free Software Foundation; either version 2 of the License, or     #
#    (at your option) any later version.                                   #
#                                                                          #
#    This program is distributed in the hope that it will be useful,       #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#    GNU General Public License for more details.                          #
#                                                                          #
#    You should have received a copy of the GNU General Public License     #
#    along with this program; if not, write to the                         #
#    Free Software Foundation, Inc.,                                       #
#    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             #
# ###########################################################################


from skin import loadSkin
from enigma import getDesktop
import os
from .. import Utils
DESKHEIGHT = getDesktop(0).size().height()


def loadSkinReal(skinPath):
    if os.path.exists(skinPath):
        print("[SKLDR] Loading skin ", skinPath)
        loadSkin(skinPath)


def loadPluginSkin(pluginPath):
    # print("config.skin.primary_skin.value A =", config.skin.primary_skin.value)
    # print("config.plugins.kodiplug.skinres.value A =", config.plugins.kodiplug.skinres.value)
    # loadSkinReal(pluginPath + "/skin/" + config.skin.primary_skin.value)
    # if DESKHEIGHT > 1000:
    #    loadSkinReal(pluginPath + "/skin/skin.xml")
    # else:
    if Utils.isFHD():
        loadSkinReal(pluginPath + "/skin/skin.xml")
    else:
        loadSkinReal(pluginPath + "/skin/skin1.xml")
