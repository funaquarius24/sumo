#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot, ['--new'])

# Change to create edge mode
netedit.createEdgeMode()

# select two-way mode
netedit.changeEditMode('4')

# select chain mode
netedit.changeEditMode('3')

# create a circular road
netedit.leftClick(referencePosition, 300, 150)
netedit.leftClick(referencePosition, 400, 150)
netedit.leftClick(referencePosition, 400, 250)
netedit.leftClick(referencePosition, 400, 350)
netedit.leftClick(referencePosition, 300, 350)
netedit.leftClick(referencePosition, 200, 350)
netedit.leftClick(referencePosition, 200, 250)
netedit.cancelEdge()

# go to select mode
netedit.selectMode()

# select all elements using invert operation
netedit.selectionInvert()

# go to inspect mode
netedit.inspectMode()

# inspect set of junctions
netedit.leftClick(referencePosition, 350, 140)

# Set all Junctions as traffic lighs
netedit.modifyAttribute(0, "traffic_light", False)

# inspect set of edges
netedit.leftClick(referencePosition, 400, 140)

# change all speed of edges
netedit.modifyAttribute(0, "20", False)

# rebuild network
netedit.rebuildNetwork()

# Check undo and redo
netedit.undo(referencePosition, 9)
netedit.redo(referencePosition, 9)

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
