from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import *
import random
from django.db.models import Q


# Load Table Page
def ldsp(request):
    return render(request, 'ldsp/index.html')


# Load Table Data
def ldspData(request):
    # Get the data from request
    search_value = request.GET['search[value]'].strip()
    startLimit = int(request.GET['start'])
    endLimit = startLimit + int(request.GET['length'])
    data_array = []

    # Count the total length
    totalLength = DataSet.objects.count()

    # if search parameter is passed
    if search_value != '':
        # Querying dataset
        dataList = DataSet.objects.filter(Q(text__contains=search_value) | Q(random__contains=search_value)).order_by(
            'id')

        # Filtering dataset
        dataFilter = dataList[startLimit:endLimit]

        # Get the filter length
        filterLength = dataList.count()
    else:
        # Querying dataset
        dataList = DataSet.objects.all().order_by('id')

        # Filtering dataset
        dataFilter = dataList[startLimit:endLimit]

        # Get the filter length
        filterLength = totalLength

    # Processing the data for table
    for key, item in enumerate(dataFilter):
        row_array = [str(key + 1), item.text, item.random, item.created_at]
        data_array.append(row_array)

    # Preparing the response
    response = {
        "draw": request.GET['draw'],
        "recordsTotal": totalLength,
        "recordsFiltered": filterLength,
        "data": data_array
    }

    # Returning json response
    return JsonResponse(response)


def ldspSeed(request):
    # 1 Lakh Data Seed
    for i in range(1, 100000):
        # Creating dataset object
        DataSet.objects.create(
            text='This is text %s' % str(i),
            random=random.randint(10000000000, 99999999999)
        )
    return HttpResponse("Done")
