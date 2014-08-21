#!/usr/bin/env python
import rospy
import roslib
import roslib; roslib.load_manifest('elderly_care_simulation')
from elderly_care_simulation.msg import DiceRollTrigger
from Tkinter import *

class DiceRollerGUI:
    """
    TkInter GUI for the visualisation of dice rolls carried out by the 
    various *DiceRoller implementations
    """
    def __init__(self):
        """
        Initialises tkInter elements and subscribes to relevant ROS Topics
        """
        # create root element with fixed size
        self.root = Tk()
        self.root.geometry('600x400+1+1')

        # create the left most frame which will hold an embeded frame with the grid of current tasks being performed ny the robots
        self.frame_left = Frame(self.root, height=400, width=300)
        self.frame_left.pack(side=LEFT, fill=BOTH)

        # create right most frame which will hold other embeded frames detailing dice rolls, upcoming events and allow event injection
        self.frame_right = Frame(self.root, height=400, width = 300)        
        self.frame_right.pack(side=TOP, fill=BOTH)

        # create frame element to host the grid detailing current tasks being performed by robots
        self.frame_robotGrid = Frame(self.frame_left, bd=3)        
        self.frame_robotGrid.pack(side=LEFT, padx=10, pady=20)

        # create frame element to host upcoming events and dice rolls
        self.frame_events_dice = Frame(self.frame_right)        
        self.frame_events_dice.pack(side=TOP, padx=10)

        # create frame element to host the event injection interface
        self.frame_eventManipulate = Frame(self.frame_right)        
        self.frame_eventManipulate.pack(side=BOTTOM, padx=10)

        # create frame element to host upcoming events
        self.frame_events = Frame(self.frame_events_dice)        
        self.frame_events.pack(side=LEFT, padx=10, pady=20, fill=BOTH)

        # create frame element to host dice rolls
        self.frame_dice = Frame(self.frame_events_dice, width=100)        
        self.frame_dice.pack(side=LEFT, padx=10, pady=20, fill=BOTH)

        # create frame element to host the event injection interface
        self.frame_injectEvent = Frame(self.frame_eventManipulate)        
        self.frame_injectEvent.pack(side=LEFT, padx=10, pady=10, fill=BOTH)

        # create frame element to host the event injection interface
        self.frame_eventChange = Frame(self.frame_eventManipulate)        
        self.frame_eventChange.pack(side=LEFT, padx=10, pady=10, fill=BOTH)

        # create variable labels
        self.resident_task = StringVar()
        self.resident_n_task = StringVar()
        self.resident_task.set("None")
        self.resident_n_task.set("None Scheduled")

        self.dice_label = StringVar()

        gridRelief = RIDGE
        gridAnchor = W
        gridWidth = 15
        gridHeight = 2

        # Creates Labels which will eventually contain information about robots and their tasks
        # :Column Names
        Label(self.frame_robotGrid, text="Robot Name", anchor=gridAnchor, relief=gridRelief, bg='ivory4', width=gridWidth).grid(row=0, column=0)
        Label(self.frame_robotGrid, text="Current Task", anchor=gridAnchor, relief=gridRelief, bg='ivory4', width=gridWidth).grid(row=0, column=1)

        # : Row 1: Resident
        Label(self.frame_robotGrid, text="Resident", anchor=gridAnchor, relief=gridRelief, height=gridHeight, width=gridWidth).grid(row=1, column=0)
        Label(self.frame_robotGrid, textvariable=self.resident_task, anchor=gridAnchor, relief=gridRelief, height=gridHeight, width=gridWidth).grid(row=1, column=1)

        # : Row 1: Cook
        Label(self.frame_robotGrid, text="Cook", anchor=gridAnchor, relief=gridRelief, height=gridHeight, width=gridWidth).grid(row=2, column=0)
        Label(self.frame_robotGrid, text="None", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=2, column=1)

        # : Row 1: Medication
        Label(self.frame_robotGrid, text="Medication", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=3, column=0)
        Label(self.frame_robotGrid, text="None", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=3, column=1)

        # : Row 1: Entertainment
        Label(self.frame_robotGrid, text="Entertainment", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=4, column=0)
        Label(self.frame_robotGrid, text="None", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=4, column=1)

        # : Row 1: Companionship
        Label(self.frame_robotGrid, text="Companionship", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=5, column=0)
        Label(self.frame_robotGrid, text="None", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=5, column=1)

        # : Row 1: Friend
        Label(self.frame_robotGrid, text="Friend", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=6, column=0)
        Label(self.frame_robotGrid, text="None", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=6, column=1)

        # : Row 1: Relative
        Label(self.frame_robotGrid, text="Relative", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=7, column=0)
        Label(self.frame_robotGrid, text="None", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=7, column=1)

        # : Row 1: Doctor
        Label(self.frame_robotGrid, text="Doctor", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=8, column=0)
        Label(self.frame_robotGrid, text="None", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=8, column=1)

        # : Row 1: Nurse
        Label(self.frame_robotGrid, text="Nurse", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=9, column=0)
        Label(self.frame_robotGrid, text="None", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=9, column=1)

        # : Row 1: Caregivier
        Label(self.frame_robotGrid, text="Caregivier", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=10, column=0)
        Label(self.frame_robotGrid, text="None", anchor=gridAnchor, relief=gridRelief, width=gridWidth, height=gridHeight).grid(row=10, column=1)

        # Set the Labels that contain information about current events
        Label(self.frame_events, text="Current Events", relief=gridRelief, bg='ivory4').pack(fill=X)
        Label(self.frame_events, text="Cooking", relief=gridRelief).pack(fill=X)
        Label(self.frame_events, text="Medication", relief=gridRelief).pack(fill=X)
        Label(self.frame_events, text="", relief=gridRelief).pack(fill=X)
        Label(self.frame_events, text="").pack(fill=X)
        Label(self.frame_events, text="Upcoming Events", relief=gridRelief, bg='ivory4').pack(fill=X)
        Label(self.frame_events, text="Shower", relief=gridRelief).pack(fill=X)
        Label(self.frame_events, text="", relief=gridRelief).pack(fill=X)

        # Label for the dice rollers
        Label(self.frame_dice, text="Dice Rollers", relief=gridRelief, bg='ivory4', width=15).pack(fill=X)

        # Label for event injection
        Label(self.frame_injectEvent, text="Event Injection", bg='ivory4', width=15).pack(side=TOP, padx=10, pady=5, fill=X)

        # Set up event type dropdown menu
        self.eventOption = ["Food", "Moral", "Companion", "Entertainment"]
        self.eventType = StringVar(self.root)
        self.eventType.set(self.eventOption[0])

        # Set up event priority menu
        self.priorityOption = ["0", "1", "2"]
        self.eventPriority = StringVar(self.root)
        self.eventPriority.set(self.priorityOption[0])

        # Create dropdown menus and inject button
        Button(self.frame_injectEvent, text="Inject").pack(side=BOTTOM, padx=10, fill=X)
        OptionMenu(self.frame_injectEvent, self.eventPriority, *self.priorityOption).pack(side=BOTTOM, padx=10, pady=5, fill=X)
        Label(self.frame_injectEvent, text="Event Priority", bg='ivory2', width=15).pack(side=BOTTOM, padx=10, fill=X)
        OptionMenu(self.frame_injectEvent, self.eventType, *self.eventOption).pack(side=BOTTOM, padx=10, pady=5, fill=X)
        Label(self.frame_injectEvent, text="Event Type", bg='ivory2', width=15).pack(side=BOTTOM, padx=10, fill=X)
        
        # Label for event changing
        Label(self.frame_eventChange, text="Change Events", bg='ivory4', width=15).pack(side=TOP, padx=5, pady=5, fill=X)
        Button(self.frame_eventChange, text="Repopulate Daily \n Events", width=18).pack(side=TOP, padx=5, pady=10, fill=X)
        Button(self.frame_eventChange, text="Clear All Events").pack(side=TOP, padx=10, pady=10, fill=X)

        # create and assign dice label to label widget. Updating dice_label will
        # automatically update the widget's text
        #self.dice_label_widget = Label(self.frame_events, textvariable=self.dice_label)
        #self.dice_label_widget.pack()

        # initialise listener node
        # anonymous ensures a unique listeners allowing multiple instances
        # of DiceRollListener to running simultanously
        rospy.init_node('DiceRollListener', anonymous=True)

        # subscribe to topic
        rospy.Subscriber("dice_roll", DiceRollTrigger, self.dice_roll_callback)


    def run(self):
        """
        Initiate tkInter's main loop. This will populate the root window
        with widgets as declared in __init__
        """
        self.root.mainloop()

    def update_dice_label(self, data):
        self.dice_label.set(data)

    def dice_roll_callback(self, msg):
        data = 'Dice Type: %d Threshold: %4d Rolled: %4d' % (msg.type, msg.threshold, msg.rolled)
        # rospy.loginfo("Dice Type: %d Threshold: %4d Rolled: %4d",msg.type, msg.threshold, msg.rolled)
        self.update_dice_label(data)

if __name__=='__main__':
    gui = DiceRollerGUI()
    gui.run()