
# coding: utf-8

# For parsing pdf I used tika which is a python port of the Apache Tika library that makes tika available using the Tika REST Server. This makes Apache Tika available as a Python library, installable via Setuptools, Pip and Easy Install.
# Java 7+ need to be installed on the system as tika-python starts up the Tika REST server in the background.

# In[7]:

import re #It will be used for handling standard textual context to parse the pdf.
from tika import parser #parsing pdf contents
import pandas as pd #making table of the contents of pdf


# In[8]:

# This contains the name of columns of our dataframe as keys.
dicty = {}
dicty['SRN']=[]
dicty['Service_Request_Date']=[]
dicty['Payment_Mode_Into']=[]
dicty['Received_From']=[]
dicty['Name']=[]
dicty['Address']=[]
dicty['Service_Type']=[]
dicty['Service_Description']=[]
dicty['Type_of_Fee']=[]
dicty['Amount']=[]
dicty['Total']=[]
dicty['Mode_of_Payment']=[]
dicty['Received_Payment_Rs']=[]


# In[9]:

#This function adds the data to dictionary which will be later converted into dataframe. 
def create_dicty(parsed_pdf,pattern):
    
#    parsed_pdf contains the content of pdf and regex parsing methods will be applies on this to etract the particular pattern.
#    pattern contains the list of pattern for every column. 
    
    p = parsed_pdf
    
#   Filling every column with the pattern detected anbd splitting.
    searched_pattern = re.findall(pattern[0],p,re.I)
    dicty['SRN'].append(searched_pattern[0][6:])
    
    searched_pattern = re.findall(pattern[1],p,re.I)
    dicty['Service_Request_Date'].append(searched_pattern[0][23:])
    
   
    searched_pattern = re.findall(pattern[2],p,re.I)
    dicty['Payment_Mode_Into'].append(searched_pattern[0][2:-2])
    
    
    searched_pattern = re.findall(pattern[3],p,re.I)
    new_pattern = searched_pattern[0].replace('\n','')
    dicty['Address'].append(new_pattern)
    
    
    searched_pattern = re.findall(pattern[4],p,re.I)
    dicty['Name'].append(searched_pattern[0])
    
    
    searched_pattern = re.findall(pattern[5],p,re.I)
    dicty['Service_Type'].append(searched_pattern[0][14:-1])
    
    searched_pattern = re.findall(pattern[6][0],p,re.I)
    new_pattern = searched_pattern[0].replace('\n',' ')
    dicty['Service_Description'].append(new_pattern[2:pattern[6][1]])
    dicty['Type_of_Fee'].append(new_pattern[pattern[6][2]:pattern[6][3]])
    dicty['Amount'].append(float(new_pattern[pattern[6][4]:pattern[6][5]]))
    
    searched_pattern = re.findall(pattern[7],p,re.I)
    dicty['Total'].append(float(searched_pattern[0][6:12]))
    
    searched_pattern = re.findall(pattern[8],p,re.I)
    dicty['Received_Payment_Rs'].append(searched_pattern[0][25:-2])
    
    
    searched_pattern = re.findall(pattern[9],p,re.I)
    dicty['Mode_of_Payment'].append(searched_pattern[0][2:-2])
    
    dicty['Received_From'].append(pattern[10])   


# In[10]:

parsedPDF = parser.from_file("./U16571275.pdf")
parsedPDF_content = parsedPDF['content']
parsedPDF_content


# In[11]:

pattern_srn = r'SRN\s.\sU\d+'
#Above pattern is used to find where 'SRN' is present in the content and feed it into table/dataframe.

pattern_date = r'Service\s.*17'
#Above pattern is used to find string which starts from 'Service Request date' and end at '17' in the content and feed it into table/dataframe.

pattern_payment_mode = r'\n\n[A-Z]+\s[A-Z]+\n\n'
#This is used to find the pattern written in complete capital words ICICI BANK.

pattern_address = '\n\nNo.*\n\nAPMC.*\n\nBangalore.*\n\nIndia.*\n\n'
#This is used to find the pattern starting from APMC containing Banglore and India also.

pattern_name = r'Za.*vat'
#This is used to find the pattern starting from 'Za'(representing Zauba) and ending to 'vat'(representing Privat).

pattern_service_type = r'Service\sType.*\n'
#This is used to find the pattern containing service type.


pattern_service_description_1 = [r'\n\nInspection\sof\sPublic\sdocuments\sof.*\n.*\n.*\n\n.*\n\n',98,100,106,107,113]
pattern_service_description_2 = [r'\n\nInspection\sof\sPublic\sdocuments\sof.*\n.*\n\n.*\n.*\n\n',97,98,104,105,111]
pattern_service_description_3 = [r'\n\nInspection\sof\sPublic\sdocuments\sof.*\n.*\n.*\n\n.*\n\n',103,104,110,111,117]
# Above 3 are different patterns for service descriptions in differnet pdf's. Integer values are given manually after checking 
# to split only useful part of detected string.

pattern_total = r'Total\s.*\n\n'
# Designed to find Total.

payment_received = r'Received.*\n\n'
# Designed to find Payment Received.

pattern_mode = '\n\n.*Card/.*Card.*Bank\n\n'
# Designed to find Payment mode.

pattern_received_from = 'Nan'
# filling with null values gor which is empty in all the pdf's


# In[12]:

# This is the list of patterns for all the pdf's.
pattern_1 = [pattern_srn,pattern_date,pattern_payment_mode,pattern_address,pattern_name,pattern_service_type,pattern_service_description_1,
            pattern_total,payment_received,pattern_mode,pattern_received_from]
pattern_2 = [pattern_srn,pattern_date,pattern_payment_mode,pattern_address,pattern_name,pattern_service_type,pattern_service_description_2,
            pattern_total,payment_received,pattern_mode,pattern_received_from]
pattern_3 = [pattern_srn,pattern_date,pattern_payment_mode,pattern_address,pattern_name,pattern_service_type,pattern_service_description_3,
            pattern_total,payment_received,pattern_mode,pattern_received_from]


# In[13]:

# Parsing first pdf and adding it's data to dictionary.
parsedPDF = parser.from_file("./U16571275.pdf")
parsedPDF_content = parsedPDF['content']
create_dicty(parsedPDF_content,pattern_1)


# In[14]:

# Parsing second pdf and adding it's data to dictionary.
parsedPDF = parser.from_file("./U16572745.pdf")
parsedPDF_content = parsedPDF['content']
create_dicty(parsedPDF_content,pattern_2)


# In[15]:

# Parsing third pdf and adding it's data to dictionary.
parsedPDF = parser.from_file("./U16573131.pdf")
parsedPDF_content = parsedPDF['content']
create_dicty(parsedPDF_content,pattern_3)


# In[16]:

#Converting pdf to Dataframe form.
df = pd.DataFrame(dicty,columns=['SRN','Service_Request_Date','Payment_Mode_Into','Address','Name','Service_Type','Service_Description',
                                'Type_of_Fee','Amount','Total','Received_Payment_Rs','Mode_of_Payment','Received_From'])


# In[17]:

df


# In[18]:

df.columns


# In[19]:

#Converting pdf to csv file.
df.to_csv('parsedData.csv',columns = ['SRN','Service_Request_Date','Payment_Mode_Into','Address','Name',
                                     'Service_Type','Service_Description','Type_of_Fee','Amount','Total',
                                      'Received_Payment_Rs','Mode_of_Payment','Received_From',],index=False)

