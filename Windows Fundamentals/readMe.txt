
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


