# this was first

import hashlib
def generate_file_hashes(file_obj):
    md5_hash=hashlib.md5()
    sha256_hash=hashlib.sha256()

    for chunk in file_obj.chunks():
        md5_hash.update(chunk)
        sha256_hash.update(chunk)

    return {
        "md5":md5_hash.hexdigest(),
        "sha256": sha256_hash.hexdigest()
    }
