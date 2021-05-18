
Note: Use Powershell instead of CMD

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Get-WmiObject <cmdlet object> (Find information about the operating system) (-ComputerName, parameter to get information about remote computers)
Example: Get-WmiObject -Class win32_OperatingSystem | select Version,BuildNumber (Find the version and build number of our system)
                              Win32_Process (Class for getting a list of processes)
                              Win32_Service (Class for getting a list of services)
                              Win32_Bios  (BIOS information)
             
xfreerdp /v:<targetIp> /u:<user> /p:Password (Connect via Remote Desktop (RDP))

| (Used for collecting dat from left side as in Shell)

select <parameter name> (Filter data for an specific parameter)

man <Tool> (For a tool manual review)

ls (For listing folders and files)

clear (Clear console log)

Get-Help (Displays basic help about cmdlets and functions)

dir (To explore the file system)

tree (Is useful for graphically displaying the directory structure of a path or disk)
  Example: tree c:\ /f | more (The following command can be used to walk through all the files in the C drive, one screen at a time)
  
Get-Content <file> (Get the content of a text file)

icacls (Stands for Integrity Control Access Control List) (Used for managing permissions on files and directories)
  Examples:
    icacls <directory> (View the permissions of each user on a directory)
    icacls c:\users /grant joe:f (Grant joe full permissions to a directory)
    icacls c:\users /remove joe (Remove joe's permissions on a directory)




    
