from dicttoxml import dicttoxml
from lxml import etree
import json
import requests

from product.models import *

from django.views           import View
from django.http            import JsonResponse

# Create your views here.


# 함수단위로 작동여부 확인

ELEVEN_API_ENDPOINT = 'http://api.11st.co.kr/rest/prodservices/product'
ELEVEN_API_KEY = 'cb435700cf301a83634d1ee9b72fdd11'


class ElevenRegister(View):
    def get(self, request):
        product_id = 9

        headers = {
            'openapikey': ELEVEN_API_KEY
        }

        # 1. product_id로 db에서 검색
        product = Products.objects.get(id = product_id)

        # 2. db산출물을 data로 정의
        root = etree.Element('Product')

        child = etree.Element('selMthdCd')
        child.text = "01"
        root.append(child)

        child = etree.Element('dispCtgrNo')
        child.text = "1010178"
        root.append(child)

        child = etree.Element('prdTypCd')
        child.text = "01"
        root.append(child)

        child = etree.Element('hsCode')
        child.text = ""
        root.append(child)

        child = etree.Element('prdNm')
        child.text = product.product_name
        root.append(child)

        child = etree.Element('brand')
        child.text = "알수없음"
        root.append(child)

        child = etree.Element('rmaterialTypCd')
        child.text = "04"
        root.append(child)

        child = etree.Element('beefTraceStat')
        child.text = "02"
        root.append(child)

        child = etree.Element('suplDtyfrPrdClfCd')
        child.text = "01"
        root.append(child)

        child = etree.Element('dlvCst1')
        child.text = "2500"
        root.append(child)

        child = etree.Element('prdSelQty')
        child.text = "2500"
        root.append(child)

        # doroduct.product_tax

        child = etree.Element('forAbrdBuyClf')
        child.text = "01"
        root.append(child)

        child = etree.Element('prdStatCd')
        child.text = "01"
        root.append(child)

        child = etree.Element('minorSelCnYn')
        child.text = "Y"
        root.append(child)

        child = etree.Element('prdImage01')
        child.text = "https://django-justsell-s3.s3.us-east-2.amazonaws.com/%EC%95%BC%EB%82%98%EB%91%90.png"
        root.append(child)

        child = etree.Element('htmlDetail')
        child.text = "<![CDATA[<TABLE cellSpacing=0 cellPadding=0 border=0><TBODY><TR><TD align=middle><img src=\"http://gi.esmplus.com/nornza1212/C/C01007%EC%83%81%EC%84%B8.jpg\" alt=\"\"><br><br><img src=\"http://gi.esmplus.com/nornza1212/b2b/B2B%20%EC%95%88%EB%82%B4%EB%AC%B8.jpg\" alt=\"\"></TD></TR></TBODY></TABLE><img src=\"http://winwintech.cafe24.com/%B9%E8%BC%DB%B9%E8%B3%CA/%C6%F7%C4%CF%C0%CE.jpg\" />]]>"
        root.append(child)

        child = etree.Element('selPrc')
        child.text = str(product.sale_price)
        root.append(child)

        child = etree.Element('gblDlvYn')
        child.text = ""
        root.append(child)

        child = etree.Element('dlvCnAreaCd')
        child.text = "01"
        root.append(child)

        child = etree.Element('dlvWyCd')
        child.text = "01"
        root.append(child)

        # child = etree.Element('dlvSendCloseTmpltNo')
        # child.text = "691011"
        # root.append(child)

        child = etree.Element('dlvCstInstBasiCd')
        child.text = "02"
        root.append(child)

        child = etree.Element('bndlDlvCnYn')
        child.text = "N"
        root.append(child)

        child = etree.Element('dlvCstPayTypCd')
        child.text = "03"
        root.append(child)

        child = etree.Element('jejuDlvCst')
        child.text = "2000"
        root.append(child)

        child = etree.Element('islandDlvCst')
        child.text = "3000"
        root.append(child)

        child = etree.Element('addrSeqOut')
        child.text = ""
        root.append(child)

        child = etree.Element('addrSeqIn')
        child.text = ""
        root.append(child)

        child = etree.Element('rtngdDlvCst')
        child.text = "3000"
        root.append(child)

        child = etree.Element('exchDlvCst')
        child.text = "3000"
        root.append(child)

        child = etree.Element('asDetail')
        child.text = "."
        root.append(child)

        child = etree.Element('rtngExchDetail')
        child.text = "."
        root.append(child)

        child = etree.Element('dlvClf')
        child.text = "02"
        root.append(child)

        child = etree.Element('abrdInCd')
        child.text = "02"
        root.append(child)

        child = etree.Element('prdWght')
        child.text = "30"
        root.append(child)

        child = etree.Element('selTermUseYn')
        child.text = "N"
        root.append(child)

        child = etree.Element('orgnTypCd')
        child.text = "01"
        root.append(child)

        child = etree.Element('ProductNotification')
        subchild = etree.Element('type')
        subchild.text = "891045"
        child.append(subchild)

        subchild = etree.Element('item')
        subsubchild = etree.Element('code')
        subsubchild.text = "23759100"
        subchild.append(subsubchild)
        subsubchild = etree.Element('name')
        subsubchild.text = "상세페이지참조"
        subchild.append(subsubchild)
        child.append(subchild)

        subchild = etree.Element('item')
        subsubchild = etree.Element('code')
        subsubchild.text = "23756033"
        subchild.append(subsubchild)
        subsubchild = etree.Element('name')
        subsubchild.text = "상세페이지참조"
        subchild.append(subsubchild)
        child.append(subchild)

        subchild = etree.Element('item')
        subsubchild = etree.Element('code')
        subsubchild.text = "11905"
        subchild.append(subsubchild)
        subsubchild = etree.Element('name')
        subsubchild.text = "상세페이지참조"
        subchild.append(subsubchild)
        child.append(subchild)

        subchild = etree.Element('item')
        subsubchild = etree.Element('code')
        subsubchild.text = "23760413"
        subchild.append(subsubchild)
        subsubchild = etree.Element('name')
        subsubchild.text = "상세페이지참조"
        subchild.append(subsubchild)
        child.append(subchild)

        subchild = etree.Element('item')
        subsubchild = etree.Element('code')
        subsubchild.text = "11800"
        subchild.append(subsubchild)
        subsubchild = etree.Element('name')
        subsubchild.text = "상세페이지참조"
        subchild.append(subsubchild)
        child.append(subchild)

        root.append(child)

        # 3. xml로 적당히 변환
        xml = etree.tostring(root, pretty_print=True)

        # 4. 11번가로 전송
        response = requests.post(ELEVEN_API_ENDPOINT, headers=headers, data=xml)

        return JsonResponse({'message':'SUCCESS', 'response': response.text}, status = 200)
