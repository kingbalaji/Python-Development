import pandas as pd

# Define keywords and meanings related to set, list, dictionary, array, and hash in Python
data = {
    "Keyword": [
        # Set Keywords
        "set", "add", "remove", "discard", "union", "intersection", "difference", "symmetric_difference",

        # List Keywords
        "list", "append", "extend", "insert", "remove", "pop", "clear", "index", "count", "sort", "reverse",

        # Dictionary Keywords
        "dict", "keys", "values", "items", "get", "update", "pop", "popitem", "clear", "fromkeys", "setdefault",

        # Array (from array module)
        "array", "typecode", "append", "extend", "insert", "remove", "pop", "buffer_info", "byteswap",

        # Hash (general hashing related)
        "hash", "hashlib", "md5", "sha1", "sha256", "sha512", "digest", "hexdigest"
    ],
    "Data Structure": [
        # Set
        "Set", "Set", "Set", "Set", "Set", "Set", "Set", "Set",

        # List
        "List", "List", "List", "List", "List", "List", "List", "List", "List", "List", "List",

        # Dictionary
        "Dictionary", "Dictionary", "Dictionary", "Dictionary", "Dictionary", "Dictionary", "Dictionary", "Dictionary", "Dictionary", "Dictionary", "Dictionary",

        # Array
        "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array", "Array",

        # Hash
        "Hash", "Hash", "Hash", "Hash", "Hash", "Hash", "Hash", "Hash"
    ],
    "Meaning": [
        # Set meanings
        "Creates a set object (unordered collection of unique elements).",
        "Adds an element to a set.",
        "Removes an element from a set; raises KeyError if not present.",
        "Removes an element if present, else does nothing.",
        "Returns the union of sets.",
        "Returns the intersection of sets.",
        "Returns the difference of sets.",
        "Returns the symmetric difference of sets (elements in either set but not both).",

        # List meanings
        "Creates a list object (ordered, mutable collection).",
        "Adds an element to the end of a list.",
        "Extends list by appending elements from an iterable.",
        "Inserts an element at a given position.",
        "Removes the first occurrence of a value.",
        "Removes and returns element at a given index (default last).",
        "Removes all items from the list.",
        "Returns the index of the first item with a specified value.",
        "Counts occurrences of a value.",
        "Sorts the list in ascending order (can be customized).",
        "Reverses the elements of the list in place.",

        # Dictionary meanings
        "Creates a dictionary object (key-value pairs).",
        "Returns a view of dictionary keys.",
        "Returns a view of dictionary values.",
        "Returns a view of dictionary items (key, value pairs).",
        "Returns value for key if key is in dictionary, else default.",
        "Updates dictionary with elements from another dictionary or iterable.",
        "Removes key and returns its value.",
        "Removes and returns an arbitrary (key, value) pair.",
        "Removes all items from the dictionary.",
        "Creates a new dictionary with keys from iterable and a specified value.",
        "Returns the value for key if present, else inserts key with a default value.",

        # Array meanings
        "Creates an array object (compactly stores basic C-style data types).",
        "Typecode indicating data type stored in array.",
        "Adds an element to the end of the array.",
        "Extends array by appending elements from an iterable.",
        "Inserts an element before a given index.",
        "Removes first occurrence of a value.",
        "Removes and returns element at a given index.",
        "Returns tuple (address, length) giving current memory info.",
        "Byteswaps all items of the array (useful for endianness).",

        # Hash meanings
        "Returns the hash value of an object (if it has one).",
        "Python module used for secure hashes and message digests.",
        "MD5 hash algorithm (128-bit).",
        "SHA-1 hash algorithm (160-bit).",
        "SHA-256 hash algorithm (256-bit).",
        "SHA-512 hash algorithm (512-bit).",
        "Returns the raw binary digest of the data.",
        "Returns the hexadecimal representation of the digest."
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel file
file_name = "python_keywords_set_list_dict_array_hash.xlsx"
df.to_excel(file_name, index=False)

print(f"Excel file '{file_name}' has been created successfully.")
