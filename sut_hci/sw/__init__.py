"""
The sw package contains the modules responsible for providing access the SUTs' software interfaces. This includes
the CLI, REST, gRPC, GUI and any other interfaces that are not directly related to the hardware.

Even though the gRPC and REST interfaces should not be categorized as software interfaces, they are included here
because some SUTs may not have a GUI or CLI, but they will always have a gRPC and REST interface, and the API clients
for these interfaces are implemented in this package.

"""