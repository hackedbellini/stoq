# -*- Mode: Python; coding: iso-8859-1 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## Copyright (C) 2005 Async Open Source
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU Lesser General Public License
## as published by the Free Software Foundation; either version 2
## of the License, or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
##
##
## Author(s):       Evandro Vale Miquelito      <evandro@async.com.br>
##


import os
import string

# All of these are relative to the root directory of the parent
file_path   = os.path.abspath(__file__)
prefix      = string.join(file_path.split(os.sep)[:-1], os.sep)
pixmap_dir  = os.path.abspath(os.path.join(prefix, "gui", "pixmaps"))
glade_dir   = os.path.abspath(os.path.join(prefix, "gui", "glade"))
