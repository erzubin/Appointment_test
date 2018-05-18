import dateutil.parser
import json
import datetime
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from appointments_app.models import AppointmentsData


class Home(View):

    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)


class ArticleDetailView(View):

    model = AppointmentsData
    template_name = 'home.html'

    def get_data(self):
        data = self.model.objects.all()
        data_list = []
        for val in data:   
                d = dict()
                d['date'] = val.apmt_datetime.strftime('%b %d')
                d['time'] = val.apmt_datetime.strftime('%H:%I%p')
                d['desc'] = val.description
                data_list.append(d)
        return data_list

    def get(self, request):     
        return HttpResponse(json.dumps(self.get_data()), content_type="application/json")

    def post(self, request):
        date = request.POST['date']
        time = request.POST['time']
        date_time = dateutil.parser.parse(date +' '+time)
        self.model.objects.create(apmt_datetime=date_time, description=request.POST['desc']).save()
        return HttpResponse(json.dumps(self.get_data()),content_type="application/json")



class Search(View):
    def post(self, request):
        data = request.POST['search'].strip()
        res = AppointmentsData.objects.filter(description__icontains=data)
        data_list = []
        for val in res:   
            d = dict()
            d['date'] = val.apmt_datetime.strftime('%b %d')
            d['time'] = val.apmt_datetime.strftime('%H:%I%p')
            d['desc'] = val.description
            data_list.append(d)
        return HttpResponse(json.dumps(data_list), content_type="application/json")


