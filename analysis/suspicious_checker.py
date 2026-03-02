# this is third

import os

DANGEROUS_EXTENSIOS=['.exe','.sh','.js','.cmd','.bat']

def if_suspicious(file_obj):
    reasons=[]
    _,ext=os.path.splitext(file_obj.name.lower())
    if ext in DANGEROUS_EXTENSIOS:
        reasons.append("executable or script file detected")
    if file_obj.size>10*1024*1024:
        reasons.append('file size unusually large')
    return{
        'suspecious':len(reasons)>0,
        'reason':reasons
        }