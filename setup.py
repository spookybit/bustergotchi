import cx_Freeze

executables = [cx_Freeze.Executable ("Bustergotchigame1.py")]


cx_Freeze.setup(
    name= 'Bustergotchi1',
    options= {"build_exe": {"packages": ["pygame"],
                            "include_files":["beachscene.png",
                            "electricityscreen.png",
                            "employeeofthemonth.png",
                            "foodcourt.png",
                            "ghostBUSTER.png",
                            "hauntedhouse.png",
                            "jacobsunglasses.png",
                            "highfood.png",
                            "jacobcries.png",
                            "jhouse.png",
                            "jsprite.png",
                            "jwhip0.png",
                            "jwhip1.png",
                            "jwhipelec.png",
                            "lightning.png",
                            "luxury-yachts.png",
                            "luxyacht.png",
                            "mainscreen.png",
                            "needle.png",
                            "pgeinvite.png",
                            "pgeworkguy.png",
                            "pika0.png",
                            "pika1.png",
                            "smiley.png",
                            "smileymeh.png",
                            "smileysad.png",
                            "spookyending.png",
                            "takeNap.png",
                            "titlescreen.png",
                            "trip.png",
                            "vial.png"]}},
    executables =  executables
    )
