# PISyncView
This is a synchronous multi-flow viewer for CAM program iterator dumps, basically a text viewer with application specific parsing, tagging, and navigation. Written in python.

Program Iterator Dumps (PI dumps) are long/unwieldy/garrulous outputs of computer aided manufacturing (CAM) process engine commands. Despite often running multiple process flows simultaneously, the dumps are output in a single thread making it difficult for a human reader to make use of the output (as she might want to for the purpose of debugging issues with CAD simulation or CAM post processors). The purpose of this program is to separate the single output thread into the individual process flows, and clean up the display so that a person viewing the file can easily determine what is happening on the virtual machine in a time-ordered way.

This is similar to a text difference viewer, except that lines are matched by time tags.

~~~~~~~~~~~~~~~~~~~~~~~~
To Do:
> remove information about other flows from steps
> add background color to operations (different color for each operation)
> add default maximum window width
> add horizontal scrollbar when window width is insufficient to display all flows
> add horizontal scrollbar when flow text contents is wider than flow display
> add ability to search the text area
> filter tool info sections so that only 
> add button to collapse tool information
	add ability to uncollapse individual tool infos
	indent or prefix & highlight values that changed (show previous value as well? Keep changes visible when the rest is hidden?)
> add button to collapse axis information
	add ability to uncollapse indivisual axis infos
	indent or prefix & highlight values that changed (show previous value as well? Keep changes visible when the rest is hidden?)
> align tops of steps with same numbers (they will always have the same time) when they are in the center of the screen
	this is for lack of a better initial concept on how to align until a prototype can be played with.
> add highlight line between steps in a single flow (not a hightlighted text line, but a line of highlight between two lines)
	add margin between two flows
		add lines to margin which connect highlight lines between flows
> add timeline viewer with blocks representing operations
	add a line to the timeline representing current cursor position, or perhaps current visible position
> hide the console and/or make it part of the main dialog window.
> add command line argument to point toward path of input dump file.