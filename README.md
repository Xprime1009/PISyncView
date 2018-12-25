# PISyncView
This is an synchronous multi-flow viewer for CAM program iterator dumps, basically a text viewer with application specific parsing, tagging, navigation. Written in python.

Program Iterator Dumps (PI dumps) are long/unwieldy/garrulous outputs of computer aided manufacturing (CAM) process engine commands. Despite often running multiple process flows simultaneously, the dumps are output in a single thread making it difficult for a human reader to make use of the output (as she might want to for the purpose of debugging issues CAD simulation or CAM post processors). The purpose of this program is to separate the single output thread into the individual process flows, and clean up the display so that a person viewing the file can easily determine what is happening on a the virtual machine in a time-ordered way.

This is similar to a text difference viewer, except that lines are matched by similar time tags.