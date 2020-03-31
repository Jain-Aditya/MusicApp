from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse
from .models import Song, Artist, Rating
from .forms import AddSongForm, AddArtistForm, UserRegisterForm
from django.db.models import Avg
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def homeView(request):
    songs = Song.objects.annotate(average_stars = Avg('rating__stars')).order_by('-average_stars')[0:10]
    lis = []
    for artist in Artist.objects.all():
        dic = {}
        dic['obj'] = artist
        dic['rate'] = artist.avg_rating()
        lis.append(dic)
    
    sorted_list = sorted(lis, key = lambda i: i['rate'],reverse=True)
    artists=[]
    for artist in sorted_list:
        artists.append(artist['obj'])
    artists = artists[0:10]

    context = {
        'songs': songs,
        'artists': artists
    }
    return render(request,'music/home.html',context)

def addNewSong(request):
    if request.method == 'GET':
        form = AddSongForm()
        form_artist = AddArtistForm()
        return render(request,'music/add_song.html', {'form': form,'artist_form':form_artist})
    else:
        form = AddSongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')

def addNewArtist(request):
    if request.method == 'POST':
        form = AddArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-song')

@login_required
def addRating(request):
    if request.method == 'POST':
        received_song_id = int(request.POST.get('song_id'))
        username = request.POST.get('username')
        number_of_stars = int(request.POST.get('optradio'))
        if len(Rating.objects.filter(user__username=username).filter(song__id=received_song_id))==0:
            song_obj = Song.objects.get(pk=received_song_id)
            user_obj = User.objects.filter(username=username)[0]
            rating = Rating(song=song_obj, user=user_obj, stars=number_of_stars)
            rating.save()
        else:
            rating_obj = Rating.objects.filter(user__username=username).filter(song__id=received_song_id)[0]
            rating_obj.stars = number_of_stars
            rating_obj.save()
    return redirect('home-page')

def userRegister(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = UserRegisterForm()
    return render(request, 'music/register.html', {'form': form})




    
