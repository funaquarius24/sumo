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
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot, ['--gui-testing-debug-gl'])

# go to additional mode
netedit.additionalMode()

# select parkingArea
netedit.changeAdditional("parkingArea")

# create parkingArea in mode "reference left"
netedit.leftClick(referencePosition, 200, 210)

# select space
netedit.changeAdditional("space")

# select parent
netedit.selectAdditionalChild(8, 3)

# create space
netedit.leftClick(referencePosition, 250, 150)

# Change to delete
netedit.deleteMode()

# delete created parkingArea
netedit.leftClick(referencePosition, 140, 160)

# delete first loaded parkingArea
netedit.leftClick(referencePosition, 360, 130)

# delete lane with the second loaded parkingArea
netedit.leftClick(referencePosition, 360, 320)

# Check undo
netedit.undo(referencePosition, 3)

# Change to delete
netedit.deleteMode()

# disable 'Automatically delete additionals'
netedit.changeAutomaticallyDeleteAdditionals(referencePosition)

# try to delete lane with the second loaded parkingArea (doesn't allowed)
netedit.leftClick(referencePosition, 300, 210)

# wait warning
netedit.waitDeleteWarning()

# check redo
netedit.redo(referencePosition, 3)

# save additionals
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
