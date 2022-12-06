import argparse
from backup import Backup
from datenbank import Datenbank
from repair import Repair
from show_tables import ShowTables
from restore import Restore
from datetime import datetime
import info_handler as ih
import platform
import datetime

# Hier startet das Programm
if __name__ == "__main__":

    # get Table Functions
    sT = ShowTables()
    parser = argparse.ArgumentParser(description="Dies ist eine Beschreibung des Programms",
                                     epilog="Dies ist der Epilog")
    # command: python3 execute.py show (user enters display of tables section)
    subparser = parser.add_subparsers(dest='command')
    
    showTables = subparser.add_parser('show', help="Get into show section of program. Eg. show File Table.")
    # user can choose either of one commands now
    group = showTables.add_mutually_exclusive_group()
    # command: python3 execute.py show -J
    group.add_argument('-J', '--showJewel', action='store_true', help='Show Jewels')
    # command: python3 execute.py show -F
    group.add_argument('-F', '--showFile', action='store_true', help='Show Files')
    # command: python3 execute.py show -sF
    group.add_argument('-sF', '--showSkippedFile', action='store_true', help='Show skipped Files')
    # command: python3 execute.py show -B
    group.add_argument('-B', '--showBlob', action='store_true', help='Show Blobs')
    # command: python3 execute.py show -[J F sf B] 123hi
    showTables.add_argument('id', type=str, nargs='?')
    # command: python3 execute.py show -[J F sf B] ? -[v vv]
    showTables.add_argument('-v', '--verbose', action='store_true', help="more detail")
    showTables.add_argument('-vv', '--verboseverbose', action='store_true', help="all of the detail")
    paths = parser.add_mutually_exclusive_group()

    #command: python3 rs -[c ca r ra] ############################## TODO 
    reed_solomon = subparser.add_parser('rs', help="Get into Reed-Solomon section of program. E.g. -create and -repair.")
    group2 = reed_solomon.add_mutually_exclusive_group()
    group2.add_argument('-ca', '--createall', action='store_true', help='Create forward error correction for everything')
    group2.add_argument('-c', '--createone', action='store_true', help='Create forward error correction for one')
    group2.add_argument('-ra', '--repairall', action='store_true', help='Create forward error correction for one')
    group2.add_argument('-r', '--repairone', action='store_true', help='Create forward error correction for one')
    reed_solomon.add_argument('id', type=str, nargs='?')
    reed_solomon.add_argument('-v', '--verbose', action='store_true', help="more detail")
    reed_solomon.add_argument('-o', '--overwrite', action='store_true', help="overwrite Files")

    # command: python3 execute.py restore
    restoreSection = subparser.add_parser('restore', help="Get into restore section of program.")
    group = restoreSection.add_mutually_exclusive_group()
    # command: python3 execute.py restore -F 12hi
    group.add_argument('-F', '--restoreFile', action='store_true', help='Restore certain File')
    # command: python3 execute.py restore -J 12hi
    group.add_argument('-J', '--restoreJewel', action='store_true', help='Restore certain Jewel')
    # needed Id to restore
    restoreSection.add_argument('id', type=str, help="File ID in Table File")
    restoreSection.add_argument('datetime', type=str, help="Date in Format: Y-m-D-H-M-S")

    # command: python3 execute.py backup
    backupSection = subparser.add_parser('backup', help="Get into backup section of program.")
    group = backupSection.add_mutually_exclusive_group()
    # command: python3 execute.py backup -v
    group.add_argument('-v', '--verbose', action='store_true', help='Backup with detailed information')

    helpSection = subparser.add_parser('help', help="info for all commands")
    group = helpSection.add_mutually_exclusive_group()

    # makes args accessable
    try:
        args = parser.parse_args()
    except:
        print("unknown command, use help for more information")
        exit(0)

    # user chooses the help section
    if args.command == "help":
        print("helping right now")

    # user chooses the show section
    if args.command == "show":

        # user chooses show jewel
        if args.showJewel:
            verbose_level = 0
            if args.verbose:
                verbose_level = 1
            elif args.verboseverbose:
                verbose_level = 2
            if args.id is not None:
                sT.show_jewel_via_id(args.id, verbose_level)
            else:
                sT.show_all_jewels(verbose_level)

        # user chooses show File
        elif args.showFile:
            verbose_level = 0
            if args.verbose:
                verbose_level = 1
            elif args.verboseverbose:
                verbose_level = 2
            if args.id is not None:
                sT.show_file_via_id(args.id, verbose_level)
            else:
                sT.show_all_files(verbose_level)

        # user chooses show skipped File
        elif args.showSkippedFile:
            verbose_level = 0
            if args.verbose:
                verbose_level = 1
            elif args.verboseverbose:
                verbose_level = 2
            if args.id is not None:
                sT.show_skipped_file_via_id(args.id, verbose_level)
            else:
                sT.show_all_skipped_Files(verbose_level)

        # user chooses show Blob
        elif args.showBlob:
            verbose_level = 0
            if args.verbose:
                verbose_level = 1
            elif args.verboseverbose:
                verbose_level = 2
            if args.id is not None:
                sT.show_blob_via_id(args.id, verbose_level)
            else:
                sT.show_all_blobs(verbose_level)

        # user chooses nothing
        else:
            print("No action selected.")

    elif args.command == "restore":

        restore_object = Restore()

        if args.restoreFile:
            try:
                # User date input
                date_input = args.datetime
                print(date_input)
                if date_input == 'today':
                    # needs to be converted into a string of the specific format
                    date_var = datetime.date.today().strftime("%Y-%m-%d-%H-%M-%S")
                    # creates a datetime object supporting the correct format
                    date_var = datetime.datetime.strptime(date_var, "%Y-%m-%d-%H-%M-%S")
                    date_var = date_var.replace(hour=23, minute=59, second=59)
                elif date_input == 'yesterday':
                    # calculates the date for yesterday
                    date_var = datetime.date.today() + datetime.timedelta(-1)
                    date_var = datetime.datetime.strftime("%Y-%m-%d-%H-%M-%S")
                    date_var = datetime.datetime.strptime(date_var, "%Y-%m-%d-%H-%M-%S")
                    date_var = date_var.replace(hour=23, minute=59, second=59)
                elif date_input == 'now':
                    # procedure for now
                    date_var = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                    date_var = datetime.datetime.strptime(date_var, "%Y-%m-%d-%H-%M-%S")
                elif ih.validate_date_format(date_input, "%Y-%m-%d-%H-%M-%S"):
                    # if datetime is given in the correct format
                    date_var = datetime.datetime.strptime(date_input, "%Y-%m-%d-%H-%M-%S")
                elif ih.validate_date_format(date_input, "%Y-%m-%d-%H-%M"):
                    # without the second timestamp
                    date_var = datetime.datetime.strptime(date_input, "%Y-%m-%d-%H-%M")
                    date_var = date_var.strftime("%Y-%m-%d-%H-%M-%S")
                    date_var = datetime.datetime.strptime(date_var, "%Y-%m-%d-%H-%M-%S")
                    date_var = date_var.replace(second=59)
                elif ih.validate_date_format(date_input, "%Y-%m-%d-%H"):
                    # without second and minute
                    date_var = datetime.datetime.strptime(date_input, "%Y-%m-%d-%H")
                    date_var = date_var.strftime("%Y-%m-%d-%H-%M-%S")
                    date_var = datetime.datetime.strptime(date_var, "%Y-%m-%d-%H-%M-%S")
                    date_var = date_var.replace(minute=59, second=59)
                elif ih.validate_date_format(date_input, "%Y-%m-%d"):
                    # without hour, minute and second
                    date_var = datetime.datetime.strptime(date_input, "%Y-%m-%d")
                    date_var = date_var.strftime("%Y-%m-%d-%H-%M-%S")
                    date_var = datetime.datetime.strptime(date_var, "%Y-%m-%d-%H-%M-%S")
                    date_var = date_var.replace(hour=23, minute=59, second=59)
                else:
                    print("No valid format. Use YYYY-mm-DD-HH-MM-SS")
                restore_object.restore_file(args.id, date_var)
            except:
                print("No valid format. Use YYYY-mm-DD-HH-MM-SS")
            
            pass
        elif args.restoreJewel:
            restore_object.restore_jewel(args.id, args.datetime)
        else:
            print("Please enter appropriate flag (-F or -J) ")

    if args.command == "backup":
        verbose_level = 0
        if args.verbose == 1:
            verbose_level = 1
        config = ih.get_json_info()
        backup = Backup(config["jewel_sources"][platform.node()], config["destination"][platform.node()])
        backup.initialize_backup(verbose_level)

    # user chooses the Reed-Solomon section
    if args.command == "rs":
        verbose_level = 0
        if args.verbose == 1:
            verbose_level = 1
        repair=Repair()
        daten = Datenbank()
        blobs=[]
        if args.createall:
            blobs = daten.get_all_Blobs()
            for blob in blobs:
                repair.create_repair_data(blob)
            print("Redundancy information created")
        elif args.createone:
            if args.id is not None:
                blob = daten.get_Blob_via_id(args.id)
                repair.create_repair_data(blob)
                print("Redundancy information created")
        
            
        else:
            print("ID missing! exiting...")
  

       

     
  

    if args.command == None:
        print("no command given, use help for more information")

