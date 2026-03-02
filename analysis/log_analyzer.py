# this is fourth
def analyze_log_files(file_obj):
    failed_logins=0
    errors=0
    warnings=0
    for line in file_obj:
        decoded_line=line.decode(errors="ignore").lower()
        if 'failed' in decoded_line:
            failed_logins+=1
        if 'error' in decoded_line:
            errors+=1
        if 'warning' in decoded_line:
            warnings+=1
    file_obj.seek(0)

    return{
        'failed_logins':failed_logins,
        'errors':errors,
        'warnings':warnings
    }