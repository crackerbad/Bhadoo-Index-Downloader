# Bhadoo Google Drive Index Downloader

This script is a Python program that facilitates downloading files from an [Google Drive Index](https://gitlab.com/GoogleDriveIndex/Google-Drive-Index). It interacts with the specified index link, retrieves the file information, and downloads the files using the Aria2c download manager.

### Credits
Credit goes to [sanjit-sinha](https://github.com/sanjit-sinha) for creating the [Bhadoo-Index-Scraper](https://github.com/sanjit-sinha/Bhadoo-Index-Scraper), which served as the basis for this script.

## Prerequisites

Before running the script, ensure that you have the following prerequisites:

- Python 3.x installed on your system.
- Aria2c installed on your system. Or download the executable from [Aria2 Repository](https://github.com/aria2/aria2/releases).

## Usage

To use the Index Downloader script, follow these steps:

1. Clone or download the script to your local machine.

2. Open a terminal or command prompt and navigate to the script's directory.

3. Run the script using the following command:
```
python index_downloader.py -i <index_link> [-o <output_folder>] [-u <username>] [-p <password>]
```

Replace `<index_link>` with the URL of the index you want to download files from.

Optional arguments:
- `-o, --output <output_folder>`: Specify the output folder where the downloaded files will be saved. If not provided, a folder named "Download" will be created in the current directory.
- `-u, --user <username>`: Provide a username for the index if it requires authentication. If not provided, a default username will be used.
- `-p, --password <password>`: Provide a password for the index if it requires authentication. If not provided, a default password will be used.

Example usage:
```
python index_downloader.py -i http://example.workers.dev/0:/folder/ -o OUTPUT_FOLDER/ -u myusername -p mypassword
```

4. The script will start retrieving the file information from the index. It will display the progress and status of the process in the console.

5. Once the file information is retrieved, the script will start downloading the files using Aria2c. The downloaded files will be saved in the specified output folder or the default "Download" folder.
