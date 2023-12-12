from argparse import ArgumentParser, Namespace
import socket
import logo as lo
from pyfiglet import Figlet
import itertools
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def main():
    logo = lo.logo.split('\n')
    tool_name = Figlet(font='slant').renderText('DiscoverIP').split('\n')

    tool_name = [''] * 5 + tool_name

    for logo_line, name_line in itertools.zip_longest(logo, tool_name, fillvalue=''):
        print(logo_line, name_line)

    while True:
        print("\n1. Display IP address")
        print("2. Display MAC address")
        print("00. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(f'IP address: {get_ip_address()}')
        elif choice == '2':
            print(f"MAC address option is not avilabe in this version.")
            # print(f'MAC address: {get_mac_address()}')
        elif choice == '00':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()