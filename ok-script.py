import subprocess

# List of commands to be executed 
commands = [

        "sudo mkdir -p /var/lib/dpkg",
        "sudo touch -c -m /var/lib/dpkg/status",
        "sudo apt update",
        "sudo dpkg --configure -a",
        "sudo apt upgrade",

        "END"]

print("\033[42m" + "Process started..." + "\033[0m" + "\n")

# Start executing the list of commands 
for command in commands:
    if command == "END":
        print("\033[42m" + "End of process!" + "\033[0m")
        break

    # Run the command
    print ("\033[32m" + "Running command:" + "\033[0m", command, "...")
    process = subprocess.run(command, shell=True, capture_output=True, text=True, check=False)

    # When the command runs successfully
    if process.returncode == 0:
        # Show the output 
        print(process.stdout)
        print("\033[42m" + "OK" + "\033[0m" + "\n")

    # When something went wrong
    else:
        # Show the error...
        print("\033[41m" + "Error:" + "\033[0m", process.stderr)

        # And ask the user if they whish to continue
        response = input("\033[33m" + "Continue executing the the script? (Y/n): " + "\033[0m")

        if response.lower() != "y":
            # If not, then stop the execution 
            print("\033[41m" + "Execution stopped" + "\033[0m")
            break

