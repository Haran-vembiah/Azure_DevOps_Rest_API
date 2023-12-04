"""
The dev[ice] package contains the modules that serve as an abstraction layer for emulating and simulating HW devices.
With these modules the users (including developers) can manage 'virtual' hardware without having to deal with any of
the low-level functions required to emulate those devices.

The actual low-level access is not implemented in these modules, as those can be functionally very diverse, since the
management of simulated devices may include
- Creation and modification of various files used by the SUT
- Accessing the SUTs' database directly
- gRPC and/or Rest calls to access the SUTs' APIs

"""