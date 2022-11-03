from django.shortcuts import render


from django.http import HttpResponse

class Dog:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Tyrion', 'teddy bear', 'Needy', 6),
  Dog('Fern', 'mutt', 'Hyper', 3),
  Dog('Vanna', 'black lab', 'Former guide dog', 4),
  Dog('Winston', 'american bulldog', 'Has puppy breath', 0)
]


def home(request):
  return HttpResponse('<h1>Hello Doggies!</h1>')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })
