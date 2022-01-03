from django.shortcuts import render

def home(request):
	return render(request, 'home.html')
def reverse(request):
	user_text = request.GET['usertext']
	worlds = user_text.split()
	number_of_worlds = len(worlds)
	reversed_text = user_text[::-1]
	print(user_text)
	return render(request, 'reverse.html', {'usertext': user_text,
		'reversedtext':reversed_text, 'numberofworlds':number_of_worlds})
def information_go(request):
	return render(request, 'inf.html')