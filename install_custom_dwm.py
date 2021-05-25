#!/usr/bin/env python3
import os

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
    print("1. Set a password or change it to a new one for user")
    print("2. Used to install the newest versions of all <update system> packages")
    print("3. Metapackages required to compile software")
    print("4. Add module (Nvidia, VirtualBox and VMware) support for new hardware")
    print("5. Remove unnecessary packages on the system")
    print("6. Disable MOTD this file on Unix-like systems contains message of the day.")
    print("7. Exit")
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
        os.system("sudo cp --force $HOME/.gitclone/CustomDWM/dist/motd/login ../../etc/pam.d")
        print("\n")

    elif int(_element) == 7:
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

