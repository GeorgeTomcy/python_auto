import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)
 
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data        
    except:
        return {}
    

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved.")

    elif command == "load":
        key = input("Enter key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")

    elif command == "list":
        print(data)

    elif command == "delete":
        key = input("Enter key: ")
        with open(SAVED_DATA, 'r') as f:
            data = json.load(f)

        if key in data:
            del data[key]
        else:
            print("Key does not exist.")

        with open(SAVED_DATA, 'w') as f:
            json.dump(data, f)

    elif command == "clear":
        with open(SAVED_DATA, "r+") as f:
            f.truncate(0)

    else:
        print("Unknown command")

else:
    print("Error")
# print(sys.argv[1:])
# clipboard.copy("abc")
# data = clipboard.paste()
# print(data)