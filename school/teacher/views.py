from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from center.models import *
from django.http import HttpResponse

@csrf_exempt
def attendancefunc(request):
		if(request.method=="GET"):
			return render(request,'frontend/attendanceupdate.html')
		elif(request.method=="POST"):
			Rollno = request.POST.get('rollno')
			Value= request.POST.get('value')
			Subject= request.POST.get('Subject')
			subid=Subjects.objects.get(subject=Subject)
			variable=attendance.objects.all()
			for val in variable:
				if(val.subject==subid):
					val.attended=val.attended+int(Value)
					val.save()
		return HttpResponse("Attendance updated")
@csrf_exempt
def marksfunc(request):
		if(request.method=="GET"):
			return render(request,'frontend/marks.html')
		elif(request.method=="POST"):
			Rollno = request.POST.get('rollno')
			marks= request.POST.get('mark')
			Exam = request.POST.get('Exam')
			Courses= request.POST.get('Course')
			department= request.POST.get('Department')
			Subject= request.POST.get('Subject')
			saveobj=exam(
			Department=Departments.objects.get(Department=department),
			course=Course.objects.get(course=Courses),
			subject=Subjects.objects.get(subject=Subject),
			ExamName=exam.objects.get(ExamName=Exam),
			rollno=Rollno,
			marks=marks
		)
		saveobj.save()
		return HttpResponse("Marks updated ")

@csrf_exempt
def examfunc(request):
	if(request.method=="GET"):
		return render(request,'frontend/exam.html')
	elif(request.method=="POST"):
		Exam = request.POST.get('Exam')
		Courses= request.POST.get('Course')
		department= request.POST.get('Department')
		Subject= request.POST.get('Subject')
		questions= request.POST.get('questions')
		saveobj=exam(
			Department=Departments.objects.get(Department=department),
			course=Course.objects.get(course=Courses),
			subject=Subjects.objects.get(subject=Subject),
			ExamName=Exam,
			question=questions,
		)
		saveobj.save()
		return HttpResponse(" ")
	
