import os
import tarfile
import requests
from datetime import datetime
import pytz


# IANA Time Zone Database URL
# IANA_TZDATA_URL = "https://data.iana.org/time-zones/tzdata-latest.tar.gz"
# IANA_TZDATA_URL = "https://data.iana.org/tz/tzdata-latest.tar.gz"
IANA_TZDATA_URL =  'https://www.iana.org/time-zones/repository/tzdata-latest.tar.gz'
OUTPUT_DIR = "iana_tzdata"


def download_iana_tzdata(url, output_file):
    """
    Download the IANA timezone database tarball from the given URL.
    """
    print(f"Downloading IANA timezone data from {url}...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_file, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        print("Download complete!")
    else:
        raise Exception(f"Failed to download file, status code: {response.status_code}")

def extract_tzdata(tar_file, output_dir):
    """
    Extract the downloaded tar.gz file into the output directory.
    """
    print(f"Extracting {tar_file} into {output_dir}...")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with tarfile.open(tar_file, "r:gz") as tar:
        tar.extractall(path=output_dir)
    print(f"Extraction complete! Files are in {output_dir}")

def list_extracted_files(output_dir):
    """
    List all files extracted from the IANA timezone database.
    """
    print("Extracted files:")
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            print(f"- {os.path.join(root, file)}")

def main():
    """
    Main function to download, extract, and list the IANA timezone database files.
    """
    tzdata_tar_file = "tzdata-latest.tar.gz"

    try:
        # Step 1: Download tzdata
        download_iana_tzdata(IANA_TZDATA_URL, tzdata_tar_file)

        # Step 2: Extract the downloaded tzdata archive
        extract_tzdata(tzdata_tar_file, OUTPUT_DIR)

        # Step 3: List extracted files
        list_extracted_files(OUTPUT_DIR)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Cleanup downloaded tar.gz file
        if os.path.exists(tzdata_tar_file):
            os.remove(tzdata_tar_file)
            print("Temporary download file removed.")

# given a timezone, get the dst and utc offsets 

def get_timezone_code_coordinates_TZ_comments():
    with open ('iana_tzdata/zone.tab','r') as f:
        tz_data = []
        for line in f:
            if line.startswith('#'): # comment
                continue
            tz_data.append(line.strip())
    return tz_data

def get_utc_and_dst(timezone_str):
    """Gets the current UTC offset and DST offset for a given timezone."""

    tz = pytz.timezone(timezone_str)
    now = datetime.now(tz)

    utc_offset = now.utcoffset()
    #print(utc_offset.total_seconds()) 
    u = int(utc_offset.total_seconds()) / 3600
    #print(u)
    #if utc_offset.total_seconds() < 0:
        #exit(0)
    dst_offset = get_dst_offset(timezone_str) + utc_offset
    d =  int(dst_offset.total_seconds()) / 3600
    return u, d

def get_dst_offset(country_code):
    """Gets the DST offset for a given country code and datetime."""

    dt = datetime(2020, 5, 17) # set to dst time of year
    timezone = pytz.timezone(country_code)
    localized_dt = timezone.localize(dt)
    return localized_dt.dst()


if __name__ == "__main__":
    main()
    exit(0)
    tz_data = get_timezone_code_coordinates_TZ_comments()
    for line in tz_data:
        line_split = line.split('\t')
        country_code = line_split[2]
        u,d = get_utc_and_dst(country_code)
        print(u,d)

        #line_split.append(str(u))
        #line_split.append(str(d))
        #line_joined = ','.join(line_split)
        #print(line_joined)
    #u,d = get_utc_and_dst('Europe/Berlin')
    #print(u,d)
