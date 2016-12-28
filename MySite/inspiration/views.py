from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from .models import Author_Name, Author_text, Author_url, Author_pic, Full_text

# Create your views here.

#Index page view
def index(request):
	authors = Author_Name.objects.all()
	
	quote_dict = {
		"Sun Tzu": "The supreme art of war is to subdue...", 
		"Mandela": "I learned that courage was not the absence of fear...", 
		"Gandhi": "Strength does not come from..."}
	
	author_pics_dict = {
		"Sun Tzu": "http://larrygeorges-productions.co.nf/Website%20Experience/image/sun%20tzu.jpg", 
		"Mandela": "http://larrygeorges-productions.co.nf/Website%20Experience/image/mandela.png", 
		"Gandhi": "http://larrygeorges-productions.co.nf/Website%20Experience/image/gandhi_2.jpg"}
	
	context = {
		'authors': authors,
		'author_pics_dict': author_pics_dict,
		'quote_dict': quote_dict
	}
	
	return render(request, 'inspiration/index.html', context)


#Detail page view
def detail(request, author_id):
	
	authors = Author_Name.objects.all()
		
	author_detail = get_object_or_404(Author_Name, pk=author_id)
	
	author_url_detail = get_object_or_404(Author_url, pk=author_id)
		
	author_full_text_detail = get_object_or_404(Full_text, pk=author_id)
		
	author_pic_detail = get_object_or_404(Author_pic, pk=author_id)
	
	
	
	author_pics_dict = {
		"Sun Tzu": "http://larrygeorges-productions.co.nf/Website%20Experience/image/sun%20tzu.jpg", 
		"Mandela": "http://larrygeorges-productions.co.nf/Website%20Experience/image/mandela.png", 
		"Gandhi": "http://larrygeorges-productions.co.nf/Website%20Experience/image/gandhi_2.jpg"
	}
	
	author_pics_list = ["http://larrygeorges-productions.co.nf/Website%20Experience/image/mandela.png", "http://larrygeorges-productions.co.nf/Website%20Experience/image/sun%20tzu.jpg", "http://larrygeorges-productions.co.nf/Website%20Experience/image/gandhi_2.jpg"]
	
	quote_dict_detail = {
		"Sun Tzu": "The supreme art of war is to subdue the enemy without fighting.", 
		"Mandela": "I learned that courage was not the absence of fear, but the triumph over it. The brave man is not he who does not feel afraid, but he who conquers that fear.", 
		"Gandhi": "Strength does not come from physical capacity. It comes from an indomitable will."}
	
	context = {
		'author_detail': author_detail,
		'author_pics_dict': author_pics_dict,
		'quote_dict_detail': quote_dict_detail,
		'author_url_detail': author_url_detail,
		'author_pic_detail': author_pic_detail,
		'author_full_text_detail': author_full_text_detail
	}
	
	return render(request, 'inspiration/detail.html', context)
	

#About page view
def about(request):

	authors = Author_Name.objects.all()
	
	author_dict = {
		"Sun Tzu": "The supreme art of war is to subdue the enemy without fighting.", 
		"Mandela": "I learned that courage was not the absence of fear, but the triumph over it. The brave man is not he who does not feel afraid, but he who conquers that fear.", 
		"Gandhi": "Strength does not come from physical capacity. It comes from an indomitable will."}
		
	author_pics_dict = {
		"Sun Tzu": "http://larrygeorges-productions.co.nf/Website%20Experience/image/sun%20tzu.jpg", 
		"Mandela": "http://larrygeorges-productions.co.nf/Website%20Experience/image/mandela.png", 
		"Gandhi": "http://larrygeorges-productions.co.nf/Website%20Experience/image/gandhi_2.jpg"}
	
	context = {
		'authors': authors,
		'author_dict': author_dict,
		'author_pics_dict': author_pics_dict
	}
	
	return render(request, 'inspiration/about.html', context)

