#!/usr/bin/env python3
import os
import shutil

def get_mainmenu():
    back = ["y", "Y", "yes", "YES"]
    warning = """
    Sorry, the entered value must be a number, please try again!
    """
    INFO = """
    Installing Minimal Desktop
    Custom Suckless DWM window manager ...

    -------------------------
    2020 Wizard Packed, Free Software by appath.
    GitHub Home https://github.com/appath\n"""
    print(INFO)

    _element = 0;
    print("1.  Set a password or change it to a new one for user")
    print("2.  Used to install the newest versions of all <update system> packages")
    print("3.  Metapackages required to compile software")
    print("4.  Add module (Nvidia, VirtualBox and VMware) support for new hardware")
    print("5.  Remove unnecessary packages on the system")
    print("6.  Disable MOTD this file on Unix-like systems contains message of the day.")
    print("7.  Change console TTY font type")
    print("8.  Install additional packages (and update pip3)")
    print("9.  Clone the repository to install CustomDWM")
    print("10. Unfold the wrapper CustomDWM")
    print("11. Exit")
    _element = input("\n")

    if int(_element) == 1:
        note_00 = """
    Set a password or change it to a new one <root> user
        """
        print(note_00)
        name_user = input("Current user: ")
        print()
        passwd = os.system("sudo passwd")
        print(passwd, name_user, "\n")

    elif int(_element) == 2:
        note_01 = """
    It does not install new software versions.
    Instead, it update the package lists for updates that require
    updating and for new packages that have just arrived in
    the repositories
        """
        print(note_01)
        os.system("sudo apt update && sudo apt dist-upgrade && sudo apt autoremove")
        print("\n")

    elif int(_element) == 3:
        note_02 = """
    These are the metapackages needed to compile the software.
    These include the GNU Debugger, the g++/GNU collection
    of compilers, and a few other tools and libraries
    needed to compile the program
        """
        print(note_02)
        os.system("sudo apt install build-essential")
        print("\n")

    elif int(_element) == 4:
        note_03 = """
    The headers are the kernel source and are usually needed if you build
    kernel modules manually or with some packages like
    Nvidia or VirtualBox and VMware
        """
        print(note_03)
        os.system("sudo apt install linux-headers$(uname -r)")
        print("\n")

    elif int(_element) == 5:
        note_04 = """
    Unnecessar packages on the system are removed.

    Package list:
            plymouth
        """
        print(note_04)
        os.system("sudo apt remove plymouth")
        print("\n")

    elif int(_element) == 6:
        note_05 = """
    Disable MOTD ...
    News of the day (a massage intended to be read by users when
    logging in and containing important information for example,
    about changes made to the system)
        """
        print(note_05)
        file_motd = os.path.expanduser("~/.gitclone/CustomDWM/login")
        copy_file_motd = "../../etc/pam.d"
        filename0 = os.path.basename(file_motd)
        filename1 = os.path.join(copy_file_motd, filename0)
        shutil.copy(file_motd, filename1)
        print("\n")

    elif int(_element) == 7:
        note_06 = """
    Change console TTY font type ...
        """
        print(note_06)
        os.system("sudo dpkg-reconfigure console-setup")
        print("\n")

    elif int(_element) == 8:
        note_07 = """
    Install additional packages.

    Package list:
            python3-pip,
            tree,
            vim,
            mc,
            git ...
        """
        note_08 = """
    Check update PIP3
        """
        print(note_07)
        os.system("sudo apt install vim mc git python3-pip")
        print(note_08)
        os.system("sudo pip3 install --upgrade pip")
        print("\n")

    elif int(_element) == 9:
        note_09 = """
    Clone the repository:
            https://github.com/appath/CustomDWM.git
        """
        print(note_09)
        os.system("git clone https://github.com/appath/CustomDWM.git $HOME/.gitclone/CustomDWM")
        print("\n")

    elif int(_element) == 10:
        note_10 = """
    Unfold the wrapper CustomDWM
    to the $HOME of the directory ...
        """
        print(note_10)
        source_folder = os.path.expanduser("~/.gitclone/CustomDWM/dist")
        target_folder = os.path.expanduser("~")

        if not os.path.exists(target_folder):
            files = os.listdir(source_folder)
            shutil.copytree(source_folder, target_folder, dirs_exist=True)

        print("\n")

    elif int(_element) == 11:
        raise SystemExit

    else:
        print(warning)
        raise SystemExit

    restart = input("Do you want to return to the main menu? ").lower()
    if restart in back:
        os.system("clear")
        get_mainmenu()

    else:
        raise SystemExit

if __name__ == "__main__":
    try:
        get_mainmenu()

    except NameError:
        #NameError, ValueError
        print("\nWARNING: Forced closing of the script!")

    except ValueError:
        print("""
    Sorry, the entered value of numbers, symbols and letters
    must be a number, please try again!
        """)

    except (EOFError, KeyboardInterrupt):
        pass

