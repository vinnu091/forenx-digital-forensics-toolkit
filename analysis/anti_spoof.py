
# this is fifth
import os
import magic

def detect_spoofing(file_obj):
    _,ext=os.path.splitext(file_obj.name.lower())
    real_type=magic.from_buffer(file_obj.read(2048),mime=True)
    file_obj.seek(0)

    spoofed=False
    reason='everything is fine nothings wrong'
    if ext in ['.jpg','.jpeg','.png'] and not real_type.startswith("image/"):
        spoofed=True
        reason='extracted file says image but content is different'
    if ext in ['.txt'] and not real_type.startswith('text'):
        spoofed=True
        reason='extracted files says text but content is different'
    return{
        'spoof_detected':spoofed,
        'reason':reason,
        'real_mime _type':real_type
    }