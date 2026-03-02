from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io


def generate_forensic_report(data):
    buffer = io.BytesIO()
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Digital Forensics Report", styles['Title']))
    story.append(Spacer(1, 12))

    for key, value in data.items():
        story.append(Paragraph(f"<b>{key}</b>: {value}", styles['Normal']))
        story.append(Spacer(1, 12))

    doc = SimpleDocTemplate(buffer)
    doc.build(story)

    buffer.seek(0)
    return buffer


    '''buffer=io.BytesIO()
    styles=getSampleStyleSheet()
    story=[]

    story.append(Paragraph('digital',styles['title']))
    story.append(Spacer(1,12))

    for key,value in data.items():
        story.append(Paragraph(f"<b>{key}</b>--{value}"),styles['normal'])
        story.append(Spacer(1,12))
    doc=SimpleDocTemplate(buffer)
    doc.build(story)
   as we have stored the value ofdocument in buffer the curser of the buffer is at the end of last text ..
                 to read it and return it we need to move the curser to the first
    buffer.seek(0)
    return buffer'''
