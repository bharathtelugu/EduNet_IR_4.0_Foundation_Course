# Day - 2 Linux OS
## linux command
### Users and Permissions
 #### 1. adduser command: This command is used to add a user.
   ![Adding User](./resource/addUser.png)
 #### 2. passwd command: This command is used to change the password of a user.
   ![passwd](./resource/passwd.png)
 #### 3. userdel command: This command is used to remove a newly created user.
   ![delete User](./resource/userdel.png)
 #### 4. finger command: This command shows the information of all the users logged in.
   ![finger command](./resource/finger.png)
### File Permissions
 #### 1. ls -l (or with filename) command: This command is used to show the file permissions along with the owner and other details of the specified file. 
   ![ls_l with filname](./resource/lsLfilename.png)
 #### 2. chmod command: The chmod command stands for “change-mode” which means that using this command, we can change the mode in which some user is able to access the file
   ![chmod](./resource/chmod.png)
### System Information Commands
 #### history command: This command displays the list of all the typed commands in the current terminal session.
   ![history](./resource/history.png)
 #### clear command: Clears the terminal i.e. no previous command will be visible on the screen now.
   $ clear
 #### hostname command: Shows the name of the system host.
   ![hostname](./resource/hostname.png)
 #### hostid command: Shows the name of the system host.
   ![hostid](./resource/hostid.png)
 #### sudo command: Allows a regular user to run the programs with the security privileges of a superuser or root.
 #### apt-get command: 
  Example <br/> 
   $ sudo apt-get update <br/> 
   $ sudo apt-get upgrade <br/> 
   $ sudo apt-get install package_name <br/>
   $ sudo apt-get purge package_name <br/>
   $ sudo apt-get remove package_name <br/>
 #### date command: This command is used to show the current date and time. 
  ![date command](./resource/date.png)
 #### cal command: Shows the calendar of the current month.
   ![cal command](./resource/cal.png)
 #### whoami command: This command displays the name with which you are logged in.
   ![whoami](./resource/whoami.png)
 #### whereis command: The "whereis" command in Linux is used to locate the binary, source code, and manual page files for a given command or program.
   ![whereis](./resource/whereis.png)
 #### top command: This command is used to get the details of all active processes.
   ![top commmand](./resource/top.png)
 #### ps command: The "ps" command in Linux is used to provide information about the currently running processes on the system.
   ![ps command](./resource/ps.png)
 #### ps PID command: This command gives the status of a particular process.
   ![ps PID command](./resource/psPID.png)
 #### pidof command: This command is used to give the process ID of a particular process.
   ![pidof command](./resource/pidof.png)

### Hardware Configuration Commands
  #### cpu-info command: This command is used to display the information about your CPU. It can be used after installation of the necessary package using sudo apt install cpuinfo.
   ![cpuInfo command](./resource/cpuInfo.png)
  #### free -h command: This command is used to display the free and used memory. The -h flag is used for converting the information (to be displayed) to human-readable form.
   ![free -h](./resource/free-h.png)
  #### lsusb -tv command: List all the USB connected devices.
   ![lsusb -tv command](./resource/lsusb-tv.png)
  #### cat /proc/meminfo command: Gives the information about memory like total and occupied and so on.
   ![cat /proc/memifo](./resource/catMemory.png)
  #### du command: This command stands for disk usage and is used to estimate the space usage for a file or directory. 
   ![du command](./resource/du.png)


