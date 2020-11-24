#!/usr/bin/env python3

from pytm.pytm import TM, Server, Process, Dataflow, Boundary, Actor, Lambda

tm = TM("Test DFD")
tm.description = "Test DFD"
tm.isOrdered = True

Boundary_Device = Boundary("Device")

Boundary_UI = Boundary("UI")
Boundary_UI.inBoundary = Boundary_Device

Boundary_Services = Boundary("Services")
Boundary_Services.inBoundary = Boundary_Device

userActor = Actor("User")

uiElem = Process("UI")
uiElem.inBoundary = Boundary_UI

service = Server("User Info service")
service.inBoundary = Boundary_Services

periodicActionLambda = Lambda("Synchronize User Data with backend")
periodicActionLambda.hasAccessControl = True
periodicActionLambda.inBoundary = Boundary_Services

userToUi = Dataflow(userActor, uiElem, "Get User Data")

uiToService = Dataflow(ui, service, "IPC: Get user data")
uiToService.protocol = "gRPC"
uiToService.data = "User data"

syncData = Dataflow(periodicActionLambda, service, "Sync data from clound")
syncData.protocol = "gRPC"

tm.process()