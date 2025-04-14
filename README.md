# real-time-streaming-dashboard-for-iot
Utlizes Azure Iothub, ASA, and Power BI as well as py. file emulating an IoT device. 

Create an Azure account.  
FOR AZURE CLI-
download and install azure cli (just in case)-https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
use "az login" to log in to operate this Azure CLI, will pop up microsoft log in prompt. 
use  az group create --name group --location "Central US" OR centralus
use az iot hub create --resource-group MyResource --name hub --sku [S1 or R1] --location "Central US"
az iot hub device-identity create --hub-name hub --device-id devicename
az iot hub device-identity connection-string show --hub-name hub --device-id device --output table

Copy primary connections string. 

Download .py file and change conn_str from current primary key to coppied primary key. 
Create two CMD to check if information is being sent successfully. 
Use az iot hub monitor-events --hub-name hub --device-id device AND py datasimulateforiot.py (will require py to use successfully

Check if information is being relayed being opening Azure and going to the AzureIoTHub to overview it signals are being sent. 

Go to ASA (Azure Stream Analytics) and create a new one, make sure it is sent to cloud and remember the name. That's a suprise tool that will help us later. In the Job Topology change add the input as the hub you are currently using make the query as follows: 

Select * Into PowerBliWorkspace From IoThubname

Make sure Output coorelates to the workspace name. 

Go to PowerBI and use your account. Add workspace, make sure you use the name for the output in ASA. Create. 

Test both input and output to see if they can connect, as well as testing the query. If successful you can start. 

Go back to the powerBI and select item as well as dashboard (top left), give dashboard a name. Clic, edit and add title. Wait until you can select the name of the Stream you are currently using upon creation. Select and click card or any graph you wish to use. (use card for each temperature and humidity), check if they are fluctuating along with the cli that you ended up inputting the py datasimulateforiot.pyaz iot hub monitor-events --hub-name IoTHubUnique001 --device-id Device001 stuff. 

Upon it doing that, success. 



