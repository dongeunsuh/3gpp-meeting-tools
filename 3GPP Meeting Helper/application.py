import configparser
import server
import parsing.outlook as outlook
import parsing.word as word
import datetime

# Read config
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

sa2_current_meeting_tdoc_data = None
sa2_inbox_tdoc_data           = None
sa2_meeting_data              = None
current_tdocs_by_agenda       = None
word_own_reporter_name        = None

# Write config
server.default_http_proxy              = config['HTTP']['DefaultHttpProxy']
outlook.sa2_list_folder_name           = config['OUTLOOK']['Sa2MailingListFolder']
outlook.sa2_email_approval_folder_name = config['OUTLOOK']['Sa2EmailApprovalFolder']

if outlook.sa2_list_folder_name[0]=='/':
    outlook.sa2_list_folder_name = outlook.sa2_list_folder_name[1:]
    outlook.sa2_list_from_inbox  = False
if outlook.sa2_email_approval_folder_name[0]=='/':
    outlook.sa2_email_approval_folder_name = outlook.sa2_email_approval_folder_name[1:]
    outlook.sa2_email_approval_from_inbox  = False

# Write other configuration
try:
    word_own_reporter_name = config['REPORTING']['ContributorName']
except:
    pass

print('Loaded configuration file')

def get_now_time_str():
    current_dt = datetime.datetime.now()
    current_dt_str = '{0:04d}.{1:02d}.{2:02d} {3:02d}{4:02d}{5:02d}'.format(current_dt.year, current_dt.month, current_dt.day, current_dt.hour, current_dt.minute, current_dt.second)
    return current_dt_str