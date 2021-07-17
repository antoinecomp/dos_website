from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm, QuizForm
from .models import Todo, Perfume
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import json
from dos_website import config
from django.views.generic import ListView
from django.http import JsonResponse
import pandas as pd


def home(request):
    return render(request, 'dos_website/home.html')


def productions(request):
    return render(request, 'dos_website/productions.html')
