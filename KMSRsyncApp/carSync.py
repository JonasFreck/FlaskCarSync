import subprocess
import os

source = os.environ.get("source")
dest = os.environ.get("dest")

#path_to_destination = "./destination/directory/"
#path_to_source = "./source/directory/"

#print(path_to_source)
#print(path_to_destination)

command = ["rsync", "-av", source, dest]

# Run the command
result = subprocess.run(command, capture_output=True, text=True)

# Print the standard output and standard error
print(result.stdout)
if result.stderr:
    print(result.stderr)
