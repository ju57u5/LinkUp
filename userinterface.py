from datenbank import *
import argparse
import datetime
import sys
from rich.console import Console
from rich.table import Table

last_input = None

# self,id,comment, monitoring_Startdate, jewelSource):
def show_all_jewels():
    daten = Datenbank()
    jewels = daten.get_all_Jewels()
    console = Console()

    if jewels is not None:
        table = Table(title="All jewels")
        table.add_column("Jewel ID", justify="left", style="black", no_wrap=True)
        table.add_column("Comment", justify="left", style="black", no_wrap=True)
        table.add_column("Monitoring startdate", justify="left", style="black", no_wrap=True)
        table.add_column("Source of the jewel", justify="left", style="black", no_wrap=True)

        for jewel in jewels:
            table.add_row(str(jewel.id), str(jewel.comment), str(jewel.monitoring_Startdate), str(jewel.jewelSource))
        console.print(table)

    else: console.print("No jewels have been created by the user yet")
    


def show_all_files():
    daten = Datenbank()
    files = daten.get_all_Files()
    console = Console()

    if files is not None:
        table = Table(title="All Files")
        table.add_column("File ID", justify="left", style="black", no_wrap=True)
        table.add_column("Number of BackUps", justify="left", style="black", no_wrap=True)
        table.add_column("File birth", justify="left", style="black", no_wrap=True)

        for file in files:
            table.add_row(str(file.id), str(len(file.blobs)), str(file.birth))
        console.print(table)
        
    else: console.print("No files have been created by the user yet")


def show_all_blobs():
    daten = Datenbank()
    blobs = daten.get_all_Blobs()
    console = Console()

    if blobs is not None:
        table = Table(title="All Blobs")
        table2 = Table(title="All Blobs")
        table.add_column("Blob ID", justify="left", style="black", no_wrap=True)
        table.add_column("File version", justify="left", style="black", no_wrap=True)
        table.add_column("Hash", justify="left", style="black", no_wrap=True)
        table.add_column("Name", justify="left", style="black", no_wrap=True)
        table.add_column("File size", justify="left", style="black", no_wrap=True)
        table.add_column("Creationdate", justify="left", style="black", no_wrap=True)
        table2.add_column("Change", justify="left", style="black", no_wrap=True)
        table2.add_column("Modify", justify="left", style="black", no_wrap=True)
        table2.add_column("File ID", justify="left", style="black", no_wrap=True)
        table2.add_column("Origin name", justify="left", style="black", no_wrap=True)
        table2.add_column("Source path", justify="left", style="black", no_wrap=True)
        table2.add_column("Store destination", justify="left", style="black", no_wrap=True)

        for blob in blobs:
            table.add_row(str(blob.id), str(blob.number), str(blob.hash), str(blob.name), str(blob.fileSize), str(blob.creationDate))
            table2.add_row(str(blob.change), str(blob.modify), str(blob.iD_File), str(blob.origin_name), str(blob.source_path), str(blob.store_destination))
        console.print(table)
        console.print(table2)

    else: console.print("No blobs have been created by the user yet")

def show_jewel_via_id(id):
    daten = Datenbank()
    jewel = daten.get_Jewel_via_id(id)
    text = "Jewel: " + str(id)
    console = Console() 

    if jewel is not None:
        table = Table(title= text)
        table.add_column("Jewel ID", justify="left", style="black", no_wrap=True)
        table.add_column("Comment", justify="left", style="black", no_wrap=True)
        table.add_column("Monitoring startdate", justify="left", style="black", no_wrap=True)
        table.add_column("Source of the jewel", justify="left", style="black", no_wrap=True)
        table.add_row(str(jewel.id), str(jewel.comment), str(jewel.monitoring_Startdate), str(jewel.jewelSource))
        console.print(table)
    else: console.print("There is no file with the id " + str(id))


def show_file_via_id (id):
    daten = Datenbank()
    file = daten.get_File_via_id(id)
    text = "File: " + str(id)
    console = Console()

    if file is not None:
        table = Table(title= text)
        table.add_column("File ID", justify="left", style="black", no_wrap=True)
        table.add_column("Number of BackUps", justify="left", style="black", no_wrap=True)
        table.add_column("File birth", justify="left", style="black", no_wrap=True)
        table.add_row(str(file.id), str(len(file.blobs)), str(file.birth))
        console.print(table)

        blobtable = Table(title= "Blobs of the file " + str(id))
        blobtable2 = Table(title= "Blobs of the file " + str(id))
        blobtable.add_column("Blob ID", justify="left", style="black", no_wrap=True)
        blobtable.add_column("File version", justify="left", style="black", no_wrap=True)
        blobtable.add_column("Hash", justify="left", style="black", no_wrap=True)
        blobtable.add_column("Name", justify="left", style="black", no_wrap=True)
        blobtable.add_column("File size", justify="left", style="black", no_wrap=True)
        blobtable.add_column("Creationdate", justify="left", style="black", no_wrap=True)
        blobtable.add_column("Change", justify="left", style="black", no_wrap=True)
        blobtable2.add_column("Modify", justify="left", style="black", no_wrap=True)
        blobtable2.add_column("File ID", justify="left", style="black", no_wrap=True)
        blobtable2.add_column("Origin name", justify="left", style="black", no_wrap=True)
        blobtable2.add_column("Source path", justify="left", style="black", no_wrap=True)
        blobtable2.add_column("Store destination", justify="left", style="black", no_wrap=True)

        for blob in file.blobs:
            blobtable.add_row(str(blob.id), str(blob.number), str(blob.hash), str(blob.name), str(blob.fileSize), str(blob.creationDate))
            blobtable2.add_row(str(blob.change), str(blob.modify), str(blob.iD_File), str(blob.origin_name), str(blob.source_path), str(blob.store_destination) )
        console.print(blobtable)

    else: console.print("There is no file with the id " + str(id))



def show_blob_via_id (id):
     daten = Datenbank()
     blob = daten.get_Blob_via_id(id)
     text = "Blob: " + str(id)
     console = Console()

# (id, number, hash, name, fileSize, creationDate, change, modify,  iD_File, origin_name, source_path, store_destination ):
     if blob is not None:
        table = Table(title=text)
        table2 = Table(title=text)
        table.add_column("Blob ID", justify="left", style="black", no_wrap=True)
        table.add_column("File version", justify="left", style="black", no_wrap=True)
        table.add_column("Hash", justify="left", style="black", no_wrap=True)
        table.add_column("Name", justify="left", style="black", no_wrap=True)
        table.add_column("File size", justify="left", style="black", no_wrap=True)
        table.add_column("Creationdate", justify="left", style="black", no_wrap=True)
        table2.add_column("Change", justify="left", style="black", no_wrap=True)
        table2.add_column("Modify", justify="left", style="black", no_wrap=True)
        table2.add_column("File ID", justify="left", style="black", no_wrap=True)
        table2.add_column("Origin name", justify="left", style="black", no_wrap=True)
        table2.add_column("Source path", justify="left", style="black", no_wrap=True)
        table2.add_column("Store destination", justify="left", style="black", no_wrap=True)
        table.add_row(str(blob.id), str(blob.number), str(blob.hash), str(blob.name), str(blob.fileSize), str(blob.creationDate))
        table2.add_row(str(blob.change), str(blob.modify), str(blob.iD_File), str(blob.origin_name), str(blob.source_path), str(blob.store_destination) )
        console.print(table)
        console.print(table2)
     else:  console.print("There is no blob with the id " + str(id))




# Hier startet das Programm
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dies ist eine Beschreibung des Programms",
                                     epilog="Dies ist der Epilog")
    parser.add_argument('-sJ', type=str, help='Show Jewels')
    parser.add_argument('-sF', type=str, help='Show Files')
    parser.add_argument('-sB', type=str, help='Show Blobs')

    arglist = sys.argv
    is_number = bool(0)
    number = 0

    for arg in arglist:
         if arglist[1] == '-sJ' and last_input is None : last_input = 0
         if arglist[1] == '-sF' and last_input is None : last_input = 1
         if arglist[1] == '-sB' and last_input is None : last_input = 2



   