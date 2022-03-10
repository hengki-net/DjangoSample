from gettext import NullTranslations
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from api.sample.sample_models import sample_Model
from api.sample.sample_serializers import sample_Serializer
from django.db import connections


@csrf_exempt
def sampleView(request, id=0):

    #############################################
    #
    # 조회
    #
    if request.method == 'GET':

        print('GET')

        pon = request.GET.get("pon")

        params = {
            'P_PON': pon,
        }

        sql = """
                SELECT PON, IN_DATE FROM TEST_HENGKI2 
            """

        #queryset = sample_Model.objects.raw(sql, params)        
        queryset = sample_Model.objects.raw(sql) 
        serializer = sample_Serializer(queryset, many=True)

        return JsonResponse(serializer.data, safe=False)

    #############################################
    #
    # 저장
    #
    elif request.method == 'POST':

        # 파라미터 받기
        pon = request.GET.get("pon")

        # SQL 정의
        sql = """
                INSERT INTO TEST_HENGKI2 (PON, IN_DATE) VALUES ( :PON, SYSDATE)
            """

        # 파라미터 정의
        params = {
            'PON': pon,
        }

        # 쿼리 실행
        cursor = connections['default'].cursor()
        cursor.execute(sql, params)
        rCnt = cursor.rowcount

        return JsonResponse({"insert" : rCnt}, safe=False)

    #############################################
    #
    # 수정
    #
    elif request.method == 'PUT':

        # 파라미터 받기
        pon = request.GET.get("pon")

        # SQL 정의
        sql = """
                UPDATE TEST_HENGKI2 SET SEQ = 2
            """

        # 파라미터 정의
        params = {
        }

        # 쿼리 실행
        cursor = connections['default'].cursor()
        cursor.execute(sql, params)
        rCnt = cursor.rowcount        

        return JsonResponse({"update" : rCnt}, safe=False)

    #############################################
    #
    # 삭제
    #
    elif request.method == 'DELETE':

        # 파라미터 받기
        pon = request.GET.get("pon")

        # SQL 정의
        sql = """
                DELETE FROM TEST_HENGKI2 WHERE PON = :PON
            """

        # 파라미터 정의
        params = {
            'PON': pon,
        }

        # 쿼리 실행
        cursor = connections['default'].cursor()
        cursor.execute(sql, params)
        rCnt = cursor.rowcount        

        return JsonResponse({"delete" : rCnt}, safe=False)
