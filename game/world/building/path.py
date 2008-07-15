# ###################################################
# Copyright (C) 2008 The OpenAnno Team
# team@openanno.org
# This file is part of OpenAnno.
#
# OpenAnno is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# ###################################################

from building import Building
import fife
import game.main
import math
from buildable import BuildableLine, BuildableSingle

class Path(Building, BuildableLine):
	def init(self):
		"""
		"""
		super(Path, self).init()
		island = game.main.session.world.get_island(self.x, self.y)
		for tile in [island.get_tile(self.x + 1, self.y), island.get_tile(self.x - 1, self.y), island.get_tile(self.x, self.y + 1), island.get_tile(self.x, self.y - 1)]:
			if tile is not None and isinstance(tile.object, Path):
				tile.object.recalculateOrientation()
		self.recalculateOrientation()

	def remove(self):
		super(Path, self).remove()
		island = game.main.session.world.get_island(self.x, self.y)
		for tile in [island.get_tile(self.x + 1, self.y), island.get_tile(self.x - 1, self.y), island.get_tile(self.x, self.y + 1), island.get_tile(self.x, self.y - 1)]:
			if tile is not None and isinstance(tile.object, Path):
				tile.object.recalculateOrientation()

	def recalculateOrientation(self):
		"""
		"""
		action = ''
		island = game.main.session.world.get_island(self.x, self.y)
		if isinstance(island.get_tile(self.x, self.y - 1).object, (Path, Bridge)):
			action += 'a'
		if isinstance(island.get_tile(self.x + 1, self.y).object, (Path, Bridge)):
			action += 'b'
		if isinstance(island.get_tile(self.x, self.y + 1).object, (Path, Bridge)):
			action += 'c'
		if isinstance(island.get_tile(self.x - 1, self.y).object, (Path, Bridge)):
			action += 'd'
		if action == '':
			action = 'default'
		location = fife.Location(game.main.session.view.layers[1])
		location.setLayerCoordinates(fife.ModelCoordinate(int(self.x + 1), int(self.y), 0))
		self._instance.act(action, location, True)

class Bridge(Building, BuildableSingle):
	#@classmethod
	#def getInstance(cls, x, y, action=None, **trash):
	#	super(Bridge, cls).getInstance(x = x, y = y, action = 'default', **trash)

	def init(self):
		"""
		"""
		super(Bridge, self).init()
		island = game.main.session.world.get_island(self.x, self.y)
		for tile in [island.get_tile(self.x + 1, self.y), island.get_tile(self.x - 1, self.y), island.get_tile(self.x, self.y + 1), island.get_tile(self.x, self.y - 1)]:
			if tile is not None and isinstance(tile.object, Path):
				tile.object.recalculateOrientation()
