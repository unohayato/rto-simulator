from django.shortcuts import render
from app.functions.calc_rto import calc_rto

# Create your views here.

def index(request):
  sample_rtt_lst = [10, 12, 7, 8, 15, 20, 24]
  sample_rto = calc_rto(sample_rtt_lst)
  context = {
    "sample_rto": sample_rto,
  }
  template_name = "app/index.html"
  return render(request, template_name, context)