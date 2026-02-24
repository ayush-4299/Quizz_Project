from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Subject, Question, QuizAttempt
import json


# ================= REGISTER =================

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password)
            return redirect("login")

    return render(request, "register.html")
# ================= LOGIN =================

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")

    return render(request, "login.html")


# ================= LOGOUT =================

def logout_view(request):
    logout(request)
    return redirect("login")


# ================= DASHBOARD =================

@login_required
def dashboard(request):
    query = request.GET.get("q")

    if query:
        subjects = Subject.objects.filter(name__icontains=query)
    else:
        subjects = Subject.objects.all()

    attempts = QuizAttempt.objects.filter(user=request.user)

    total_coins = attempts.aggregate(Sum("score"))["score__sum"] or 0

    labels = []
    scores = []

    for attempt in attempts:
        labels.append(attempt.subject.name)

        if attempt.total_questions > 0:
            percentage = (attempt.score / attempt.total_questions) * 100
        else:
            percentage = 0

        scores.append(round(percentage, 2))

    return render(request, "dashboard.html", {
        "subjects": subjects,
        "attempts": attempts,
        "coins": total_coins,
        "labels": json.dumps(labels),
        "scores": json.dumps(scores),
        "query": query
    })

# ================= START QUIZ =================

@login_required
def start_quiz(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    questions = Question.objects.filter(subject=subject)

    if request.method == "POST":
        score = 0
        total_questions = questions.count()

        for question in questions:
            selected_option = request.POST.get(str(question.id))

            if selected_option and int(selected_option) == question.correct_option:
                score += 1

        QuizAttempt.objects.create(
            user=request.user,
            subject=subject,
            score=score,
            total_questions=total_questions
        )

        return redirect("dashboard")

    return render(request, "quiz.html", {
        "subject": subject,
        "questions": questions
    })


# ================= LEADERBOARD =================

@login_required
def leaderboard(request):
    top_attempts = QuizAttempt.objects.order_by("-score")[:10]

    return render(request, "leaderboard.html", {
        "top_users": top_attempts
    })