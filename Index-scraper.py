import argparse
import requests
import base64 
import json
import urllib
import os

next_page = False
next_page_token = "" 

parser = argparse.ArgumentParser(description='STRM Generator.')
parser.add_argument('-u', '--url', help='url from index', required=True)
parser.add_argument('-o', '--output', help='output folder', required=False)
args = parser.parse_args()

OUTPUT_DIR = args.output if args.output else "STRM"
isExist = os.path.exists(OUTPUT_DIR)
if not isExist:
	os.makedirs(OUTPUT_DIR)
	print(f"\n{OUTPUT_DIR} directory created!")

 
def authorization_token(username, password):
	 user_pass = f"{username}:{password}"
	 token ="Basic "+ base64.b64encode(user_pass.encode()).decode()
	 return token

	 	 
def decrypt(string): 
     return base64.b64decode(string[::-1][24:-20]).decode('utf-8')  

  
def func(payload_input, url, username, password): 
    global next_page 
    global next_page_token
    
    url = url + "/" if  url[-1] != '/' else url
         
    try: headers = {"authorization":authorization_token(username,password)}
    except: return "username/password combination is wrong"
 
    encrypted_response = requests.post(url, data=payload_input, headers=headers)
    if encrypted_response.status_code == 401: return "username/password combination is wrong"
   
    try: decrypted_response = json.loads(decrypt(encrypted_response.text))
    except: return "something went wrong. check index link/username/password field again"
       
    page_token = decrypted_response["nextPageToken"] 
    if page_token == None: 
        next_page = False 
    else: 
        next_page = True 
        next_page_token = page_token 
   
     
    result = ""
   
    if list(decrypted_response.get("data").keys())[0] == "error": pass
    else :
      file_length = len(decrypted_response["data"]["files"])
      for i, _ in enumerate(range(file_length)):
	       
	        files_type   = decrypted_response["data"]["files"][i]["mimeType"] 
	        files_name   = decrypted_response["data"]["files"][i]["name"] 
	      
	
	        if files_type == "application/vnd.google-apps.folder": pass
	        else:
	            direct_download_link = url + urllib.parse.quote(files_name)
	            result += f"{files_name}.strm - Successfully created in {OUTPUT_DIR} Folder.\n"
	            #create strmfiles
	            strmfile = open(f"{OUTPUT_DIR}/{files_name}.strm", "w")
	            strmfile.write(f"{direct_download_link}")
      return result
       
	
def main(url, username="none", password="none"):
	x = 0
	payload = {"page_token":next_page_token, "page_index": x}	
	print(f"\n\nGenerating STRM files from: {url}\n\n")
	print(func(payload, url, username, password))
	
	while next_page == True:
		payload = {"page_token":next_page_token, "page_index": x}
		print(func(payload, url, username, password))
		x += 1
		

index_link = args.url
username = "username-default" #optional
password ="password-default"  #optional
				
main(url=index_link, username=username, password=password)
