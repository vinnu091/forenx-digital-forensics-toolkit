from django.shortcuts import render
from .serializer import FileUploadSerializer
from rest_framework.response import Response
from rest_framework import status
from .hash_utils import generate_file_hashes
from rest_framework.views import APIView
from .metadata_utils import extract_file_metadata
from .suspicious_checker import if_suspicious
from .log_analyzer import analyze_log_files
from rest_framework.permissions import IsAuthenticated
from .anti_spoof import detect_spoofing
from .malware_checker import check_malware_hash
from .background_tasks import start_background_scan
from .task_store import tasks
from django.http import FileResponse
from .report_generator import generate_forensic_report
from .virustotal_checker import check_virustotal
# Create your views here.

class FileHashView(APIView):
    permission_classes=[IsAuthenticated]
    def post (self,request):
        serializer=FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            file_obj=serializer.validated_data['file']
            hashes=generate_file_hashes(file_obj)
            vt_result = check_virustotal(hashes["md5"])
            metadata=extract_file_metadata(file_obj)
            suspicious=if_suspicious(file_obj)
            log_analyze=analyze_log_files(file_obj)
            spoofed=detect_spoofing(file_obj)
            md5_value = hashes["md5"]
            malware_result = check_malware_hash(md5_value)
            task_id=start_background_scan(file_obj)

            return Response({
                'filename':file_obj.name,
                'hashes':hashes,
                'metadata':metadata,
                'suspicious':suspicious,
                'log_analyze':log_analyze,
                'spoofed':spoofed,
                'malware_result':malware_result,
                'task_id':task_id,
                'status':'processing',
                "virustotal_analysis": vt_result,
            })
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



class ScanStatusView(APIView):
    def get(self, request, task_id):
        return Response(tasks.get(task_id, {"error": "Task not found"}))
    
class ForensicReportView(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):        
        data=request.data
        pdf_buffer=generate_forensic_report(data)

        return FileResponse(

            pdf_buffer,
            as_attachment=True,
            # Forces browser to download the file instead of opening inline.
            filename='forensic_report.pdf'
        )