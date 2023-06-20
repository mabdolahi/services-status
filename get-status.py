import requests as r
import argparse
import sys

def get_status(url:str):
    try:
        # Get data from URL
        response = r.get(url).text
        # Create a list of lines from the response
        lines = response.strip().split('\n')
        # loop over the each line and check for the status
        for line in lines:
            # if the line is empty, skip it.
            if line:
                # extract the service name and status
                service, status = line.split(':')
                # Remove extra empty spaces
                if status.strip() != 'OK':
                    print("The Service " + service.strip() + " is " + status.strip())

    except r.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)



def main():
    parser = argparse.ArgumentParser()

    parser. add_argument("URL", help="URL of the payload")

    args = parser.parse_args()

    get_status(args.URL)

if __name__ == "__main__":
    main()







