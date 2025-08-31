import sys
import urllib.request
import io, hashlib

try:
    # Check command line arguments
    if len(sys.argv) < 2:
        print("Error: Missing record ID argument")
        print("Usage: python check_zenodo.py <record_id>")
        sys.exit(1)

    record = sys.argv[1]
    print(f"Checking Zenodo record: {record}")

    # Initialize test variables
    test1 = False
    test2 = False
    test3 = False

    # Download file
    url = "https://sandbox.zenodo.org/records/" + record + "/files/hal-03281732.pdf"
    print(f"Attempting to download from: {url}")

    try:
        urllib.request.urlretrieve(url, filename="zenodo_test.pdf")
        print("File downloaded successfully")
        
        # Verify hash (only if download succeeded)
        target = '5db59521d85a536eba963c9a7ca3620b0d391ee16c592e7d7b1fb8bb3573ce44'
        print("Verifying file hash...")

        try:
            with open("zenodo_test.pdf", "rb") as f:
                digest = hashlib.file_digest(f, "sha256")
            file_hash = digest.hexdigest()
            print(f"Expected hash: {target}")
            print(f"Actual hash: {file_hash}")
            test1 = file_hash == target
            print(f"Hash check: {'Passed' if test1 else 'Failed'}")
        except Exception as e:
            print(f"Error checking file hash: {e}")
            test1 = False

    except Exception as e:
        print(f"Error downloading file: {e}")
        test1 = False

    # Check record metadata
    url = "https://sandbox.zenodo.org/records/" + record
    print(f"Checking record page: {url}")

    try:
        with urllib.request.urlopen(url) as f:
            top_part = f.read(1000).decode('utf-8')

        test2 = '<meta name="citation_title" content="An exercise of the MOOC RR2" />' in top_part
        test3 = '<meta name="description" content="This is a sandbox repository for testing my ability to upload a file on zenodo." />' in top_part

        print(f"Title check: {'Passed' if test2 else 'Failed'}")
        print(f"Description check: {'Passed' if test3 else 'Failed'}")
    except Exception as e:
        print(f"Error checking record page: {e}")
        test2, test3 = False, False

    # Print final result
    if test1 and test2 and test3:
        print('83117999910111511533')
    else:
        print('709710510811711410133')

except Exception as e:
    print(f"Unexpected error: {e}")
