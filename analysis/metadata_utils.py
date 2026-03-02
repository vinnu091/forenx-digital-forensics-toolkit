# this was second

import os 
import magic

def extract_file_metadata(file_obj):

    file_size=file_obj.size

    file_obj.seek(0)
    file_type=magic.from_buffer(file_obj.read(2048),mime=True)
    file_obj.seek(0)
    return{
        "file_size_bytes":file_size,
        "file_type":file_type
    }