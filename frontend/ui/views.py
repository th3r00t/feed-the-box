# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.utils.html import format_html
from django.middleware.csrf import get_token
from .forms import SearchForm
from .forms import DownloadForm
from download import MagnetDownloader
from movinfo import TheMovieDb
import sys

sys.path.insert(0, '/home/raelon/Projects/feed-the-box/')
from config import TmdApi


# Create your views here.


def index(request):
    from search import TorrentSearch
    # rel_list = TheMovieDb()
    template = loader.get_template('index.html')
    context = {'releases': "Insert Trakt Logic"}
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            new_form = SearchForm()
            tor_search = TorrentSearch()
            results = tor_search.do_search(form.data['search'])
            results_array = ""
            alternate = False
            for r in results:
                if alternate:
                    alternate = False
                else:
                    alternate = True
                if alternate:
                    alternate_row = "alternate_row"
                else:
                    alternate_row = ""
                # download_form = DownloadForm()
                csrf_token = get_token(request)
                results_array = results_array + """
                    <div class='search_result %s'>
                    <form action="download" method="post">
                        <span class='result_name'>%s</span>
                        <span class='result_link'>%s</span>
                        <input type='hidden' value='%s' id='magnet' name='magnet'>
                        <input type='hidden' name='csrfmiddlewaretoken' id='csrfmiddlewaretoken' value='%s'>
                        <select name='download_type' id='download_type'>
                            <option value='m'>Movie</option>
                            <option value='t'>Tv Show</option>
                            <option value='o'>Other</option>
                        </select>
                        <span class='download_ui_btns'>
                        <input type='submit' value='Download' />
                        </span>
                    </form>
                    </div> 
                """ % (alternate_row, r['title'], r['url'], r['magnet'], csrf_token)
            results_array = format_html(results_array)
            context = {
                'form': new_form,
                'torrents': results_array,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = SearchForm()
        context = {'releases': "Insert Trakt Logic", 'form': form}
        return HttpResponse(template.render(context, request))


def download(request):
    form = SearchForm()
    if request.method == 'POST':
        download_form = DownloadForm(request.POST)
        magnet = request.POST['magnet']
        dl_type = request.POST['download_type']
        token = request.POST['csrfmiddlewaretoken']
        MagnetDownloader(magnet, dl_type)
        context = {
            'form': form,
            'torrents': 'Download Initiated.',
        }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))
