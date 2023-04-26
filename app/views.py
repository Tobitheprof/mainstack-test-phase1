from django.shortcuts import render
import requests


def home(request):
    url = "https://fe-task-api.mainstack.io/"
    r = requests.get(url)
    answer = r.json()
    # print(answer)

    dates = answer['graph_data']['views']['2022-07-31'],
    print(dates)
    nigeria = answer['top_locations'][0]['country'],
    germany = answer['top_locations'][1]['country'],
    ghana = answer['top_locations'][2]['country'],
    finland = answer['top_locations'][3]['country'],
    united_kingdom = answer['top_locations'][4]['country']


    nigeria_percent = answer['top_locations'][0]['percent']
    germany_percent = answer['top_locations'][1]['percent']
    ghana_percent = answer['top_locations'][2]['percent']
    finland_percent = answer['top_locations'][3]['percent']
    united_percent = answer['top_locations'][4]['percent']

    nigeria_count = answer['top_locations'][0]['count']
    germany_count = answer['top_locations'][1]['count']
    ghana_count = answer['top_locations'][2]['count']
    finland_count = answer['top_locations'][3]['count']
    united_count = answer['top_locations'][4]['count']

    google = answer['top_sources'][0]['source']
    instagram = answer['top_sources'][1]['source']
    facebook = answer['top_sources'][2]['source']
    linkedin = answer['top_sources'][3]['source']

    google_count = answer['top_sources'][0]['count']
    instagram_count = answer['top_sources'][1]['count']
    facebook_count = answer['top_sources'][2]['count']
    linkedin_count = answer['top_sources'][3]['count']

    google_percent = answer['top_sources'][0]['percent']
    instagram_percent = answer['top_sources'][1]['percent']
    facebook_percent = answer['top_sources'][2]['percent']
    linkedin_percent = answer['top_sources'][3]['percent']



    google_fix = google.capitalize()
    instagram_fix = instagram.capitalize()
    facebook_fix = facebook.capitalize()
    linkedin_fix = linkedin.capitalize()



    fixed_ng = str(nigeria)
    fixed_gm = str(germany)
    fixed_gh = str(ghana)
    fixed_fin = str(finland)
    fixed_uk = str(united_kingdom)


    # print(gm_fix)


    ng_fix = fixed_ng[2:-3]
    gm_fix = fixed_gm[2:-3]
    gh_fix = fixed_gh[2:-3]
    fin_fix = fixed_fin[2:-3]
    uk_fix = fixed_uk[2:-3]


    

   
    context = {
        #countries fix start
        'ng_fix' : ng_fix,
        'gm_fix' : gm_fix,
        'gh_fix' : gh_fix,
        'fin_fix' : fin_fix,
        'uk_fix' : uk_fix,
        #end

        #country percent start
        'ng_cent' : nigeria_percent,
        'gm_cent' : germany_percent,
        'gh_cent' : ghana_percent,
        'fin_cent' : finland_percent,
        'united_percent' : united_percent,
        #end

        #country count start
        'ng_count' : nigeria_count,
        'gm_count' : germany_count,
        'gh_count' : ghana_count,
        'fin_count' : finland_count,
        'uk_count' : united_count,
        #end

        #top sources name start
        'google' : google_fix,
        'instagram' : instagram_fix,
        'facebook' : facebook_fix,
        'linkedin' : linkedin_fix,
        #end

        #top sources percent
        'google_percent' : google_percent,
        'instagram_percent' :instagram_percent,
        'facebook_percent' : facebook_percent,
        'linkedin_percent' : linkedin_percent,
        #end

        #top sources count
        'google_count' : google_count,
        'instagram_count' : instagram_count,
        'facebook_count' : facebook_count,
        'linkedin_count' : linkedin_count,

        #end

    }

    return render(request, 'index.html', context)

# Create your views here.
