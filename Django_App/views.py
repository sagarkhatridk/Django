# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.options import Options

import json

# import chromedriver_autoinstaller
import xmltodict
from django.shortcuts import render
from django.http import HttpResponse
import requests
# from sqlalchemy_utils.types.json import json

from django.http import JsonResponse
# Create your views here.

def Greetings(request):
    return HttpResponse("<div style='text-align:center;background-color:yellow;'><h1>API'S Django<h1></div>")
    

def flydreamzz(request):


    param_json = {
        "origin": "IXB",
        "destination": "CCU",
        "is_return": '',
        "flight_class": "",
        "depart_date": "2022-11-29",  # "01-09-2022"
        "return_date": "",
        "adult": "1",
        "child": "0",
        "infant": "0",
        "domain": "Flydreamzz.in",
        "key": "test-xbyte"
    }

    response=dict()
    response.update(flydreamzz_json(param_json))

    return JsonResponse(response,safe=False)

def Makevoyage(request):

    param_json = {
        "origin": "GAU",
        "destination": "BLR",
        "is_return": '',
        "flight_class": "",
        "depart_date": "2022-12-01",  # "01-09-2022"
        "return_date": "",
        "adult": "1",
        "child": "0",
        "infant": "0",
        "domain": "makevoyage",
        "key": "test-xbyte"
    }

    response=dict()
    response.update(makevoyage_json(param_json,12345))

    return JsonResponse(response,safe=False)


flight_code_json = [{"places": "Agartala", "airport_code": "IXA"}, {"places": "Ahmedabad", "airport_code": "AMD"}, {"places": "Aizawl", "airport_code": "AJL"}, {"places": "Aurangabad", "airport_code": "IXU"}, {"places": "Amritsar", "airport_code": "ATQ"}, {"places": "Bagdogra", "airport_code": "IXB"}, {"places": "Bengaluru", "airport_code": "BLR"}, {"places": "Bhubaneswar", "airport_code": "BBI"}, {"places": "Bhopal", "airport_code": "BHO"}, {"places": "Chandigarh", "airport_code": "IXC"}, {"places": "Chennai", "airport_code": "MAA"}, {"places": "Coimbatore", "airport_code": "CJB"}, {"places": "Dehradun", "airport_code": "DED"}, {"places": "Delhi", "airport_code": "DEL"}, {"places": "Dibrugarh", "airport_code": "DIB"}, {"places": "Dimapur", "airport_code": "DMU"}, {"places": "Durgapur", "airport_code": "RDP"}, {"places": "Gaya", "airport_code": "GAY"}, {"places": "Goa", "airport_code": "GOI"}, {"places": "Gorakhpur", "airport_code": "GOP"}, {"places": "Guwahati", "airport_code": "GAU"}, {"places": "Hubli", "airport_code": "HBX"}, {"places": "Hyderabad", "airport_code": "HYD"}, {"places": "Imphal", "airport_code": "IMF"}, {"places": "Indore", "airport_code": "IDR"}, {"places": "Jabalpur", "airport_code": "JLR"}, {"places": "Jaipur", "airport_code": "JAI"}, {"places": "Jammu", "airport_code": "IXJ"}, {"places": "Jodhpur", "airport_code": "JDH"}, {"places": "Jorhat", "airport_code": "JRH"}, {"places": "Kannur", "airport_code": "CNN"}, {"places": "Kurnool", "airport_code": "KJB"}, {"places": "Kochi", "airport_code": "COK"}, {"places": "Kolhapur", "airport_code": "KLH"}, {"places": "Kolkata", "airport_code": "CCU"}, {"places": "Kozhikode", "airport_code": "CCJ"}, {"places": "Lucknow", "airport_code": "LKO"}, {"places": "Madurai", "airport_code": "IXM"}, {"places": "Mangaluru", "airport_code": "IXE"}, {"places": "Mumbai", "airport_code": "BOM"}, {"places": "Mysuru", "airport_code": "MYQ"}, {"places": "Nagpur", "airport_code": "NAG"}, {"places": "Patna", "airport_code": "PAT"}, {"places": "Prayagraj", "airport_code": "IXD"}, {"places": "Pune", "airport_code": "PNQ"}, {"places": "Portblair", "airport_code": "IXZ"}, {"places": "Raipur", "airport_code": "RPR"}, {"places": "Rajahmundry", "airport_code": "RJA"}, {"places": "Ranchi", "airport_code": "IXR"}, {"places": "Shillong", "airport_code": "SHL"}, {"places": "Shirdi", "airport_code": "SAG"}, {"places": "Silchar", "airport_code": "IXS"}, {"places": "Srinagar", "airport_code": "SXR"}, {"places": "Surat", "airport_code": "STV"}, {"places": "Thiruvananthapuram", "airport_code": "TRV"}, {"places": "Tiruchirappalli", "airport_code": "TRZ"}, {"places": "Tirupati", "airport_code": "TIR"}, {"places": "Tuticorin", "airport_code": "TCR"}, {"places": "Udaipur", "airport_code": "UDR"}, {"places": "Vadodara", "airport_code": "BDQ"}, {"places": "Varanasi", "airport_code": "VNS"}, {"places": "Vijayawada", "airport_code": "VGA"}, {"places": "Visakhapatnam", "airport_code": "VTZ"}, {"places": "Kannur", "airport_code": "CNN"}, {"places": "Agartala", "airport_code": "IXA"}, {"places": "Ahmedabad", "airport_code": "AMD"}, {"places": "Amritsar", "airport_code": "ATQ"}, {"places": "Bagdogra", "airport_code": "IXB"}, {"places": "Bengaluru", "airport_code": "BLR"}, {"places": "Bhubaneswar", "airport_code": "BBI"}, {"places": "Bhopal", "airport_code": "BHO"}, {"places": "Chandigarh", "airport_code": "IXC"}, {"places": "Chennai", "airport_code": "MAA"}, {"places": "Coimbatore", "airport_code": "CJB"}, {"places": "Dehradun", "airport_code": "DED"}, {"places": "Delhi", "airport_code": "DEL"}, {"places": "Dimapur", "airport_code": "DMU"}, {"places": "Goa", "airport_code": "GOI"}, {"places": "Gorakhpur", "airport_code": "GOP"}, {"places": "Guwahati", "airport_code": "GAU"}, {"places": "Hubli", "airport_code": "HBX"}, {"places": "Hyderabad", "airport_code": "HYD"}, {"places": "Imphal", "airport_code": "IMF"}, {"places": "Indore", "airport_code": "IDR"}, {"places": "Jabalpur", "airport_code": "JLR"}, {"places": "Jaipur", "airport_code": "JAI"}, {"places": "Jammu", "airport_code": "IXJ"}, {"places": "Kolkata", "airport_code": "CCU"}, {"places": "Kozhikode", "airport_code": "CCJ"}, {"places": "Lucknow", "airport_code": "LKO"}, {"places": "Madurai", "airport_code": "IXM"}, {"places": "Mangaluru", "airport_code": "IXE"}, {"places": "Mumbai", "airport_code": "BOM"}, {"places": "Nagpur", "airport_code": "NAG"}, {"places": "Patna", "airport_code": "PAT"}, {"places": "Pune", "airport_code": "PNQ"}, {"places": "Raipur", "airport_code": "RPR"}, {"places": "Rajahmundry", "airport_code": "RJA"}, {"places": "Ranchi", "airport_code": "IXR"}, {"places": "Srinagar", "airport_code": "SXR"}, {"places": "Surat", "airport_code": "STV"}, {"places": "Thiruvananthapuram", "airport_code": "TRV"}, {"places": "Tiruchirappalli", "airport_code": "TRZ"}, {"places": "Tuticorin", "airport_code": "TCR"}, {"places": "Udaipur", "airport_code": "UDR"}, {"places": "Vadodara", "airport_code": "BDQ"}, {"places": "Varanasi", "airport_code": "VNS"}, {"places": "Vijayawada", "airport_code": "VGA"}, {"places": "Visakhapatnam", "airport_code": "VTZ"}, {"places": "Gaya", "airport_code": "GAY"}, {"places": "Jodhpur", "airport_code": "JDH"}, {"places": "Silchar", "airport_code": "IXS"}, {"places": "Belagavi", "airport_code": "IXG"}]


def login_site():
    session = requests.Session()

    url = "https://www.makevoyage.com/dispatch.jsp?nonce=84.44047970198821"

    payload = "userid=9382207002&password=Sumit%4012356&opid=AU001&usertype=GenericClient&agencycode="
    headers = {
        'Accept-Language': 'en-US,en;q=0.9,de;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '86',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.makevoyage.com',
        'Referer': 'https://www.makevoyage.com/indexpage.jsp',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',

    }
    session.post(url=url, headers=headers, data=payload)
    jsessionid = session.cookies.get_dict()['JSESSIONID']

    return jsessionid

    #comment : For selenium prefer below code



    # try:
    #     username = "9382207002"
    #     password = "Sumit@12356"
    #
    #     options = Options()
    #     # driver = Firefox(options=opts)
    #
    #     options.add_argument('--headless')
    #
    #     driver = webdriver.Chrome(chromedriver_autoinstaller.install(), options=options)
    #     # driver = webdriver.Chrome("D:\X-Byte(Projects)\chromedriver.exe", options=options)
    #
    #     # head to github login page
    #     driver.get("https://www.makevoyage.com/indexpage.jsp")
    #     # find username/email field and send the username itself to the input field
    #     driver.find_element_by_id("username").send_keys(username)
    #     # find password input field and insert password as well
    #     driver.find_element_by_id("password").send_keys(password)
    #     # click login button
    #     driver.find_element_by_id("loginbutton").click()
    #     jsessionid = driver.get_cookies()[0]['value']
    #     # print(jsessionid)
    #
    #     # wait the ready state to be complete
    #     WebDriverWait(driver=driver, timeout=10).until(lambda x: x.execute_script("return document.readyState === 'complete'"))
    #     error_message = "Incorrect username or password."
    #     # get the errors (if there are)
    #     errors = driver.find_elements_by_class_name("flash-error")
    #     # print the errors optionally
    #     # for e in errors:
    #     #     print(e.text)
    #     # if we find that error message within errors, then login is failed
    #     if any(error_message in e.text for e in errors):
    #         print("Login failed")
    #     else:
    #         print("Login successful")
    #
    #     driver.close()
    #     return  jsessionid
    # except Exception as e:
    #     print("Error in login :",e)
    #     jsessionid = ''
    #     return jsessionid


def makevoyage_json(param_json, hashId):
  ls1 = {"results": dict()}

  list_ori_des = []
  for data in flight_code_json:
      list_ori_des.append(data['airport_code'])
  # print(list_ori_des)

  jsessionid = login_site()

  if jsessionid == '':
      ls1['results'] = {"status": 400, "msg": "Internal Server Error"}
      return ls1

  Origin = str(param_json['origin'])
  # print(Origin)

  Destination = str(param_json['destination'])
  # print(Destination)

  if Origin not in list_ori_des:
      # ls1['results'] = 'Invalid origin or destination entered.'
      ls1['results'] = {"status":400,"msg":"Invalid origin or destination entered."}
      return ls1

  elif Destination not in list_ori_des:
      ls1['results'] = {"status":400,"msg":"Invalid origin or destination entered."}
      return ls1

  else:

      # for i in flight_code_json:
      #
      #       if  i['places'] == Origin.capitalize():
      #           Origin = i['airport_code']
      #
      # for j in flight_code_json:
      #
      #       if j['places'] == Destination.capitalize():
      #           Destination = j['airport_code']

      DepartDate = param_json['depart_date']
      Adult = param_json['adult']
      Child = param_json['child']
      Infant = param_json['infant']




      url = "https://www.makevoyage.com/dispatch.jsp?nonce=0.5898738475848477"

      payload = f"opid=FS000&actioncode=SEARCHCOUPONFARES&agentid=MV24858&origin={Origin}&destination={Destination}&jdate={DepartDate}&numadults={Adult}&numchildren={Child}&numinfants={Infant}".replace("-","")

      headers = {
          'accept': 'text/html, */*; q=0.01',
          # 'accept-encoding': 'gzip, deflate, br',
          'accept-language': 'en-US,en;q=0.9,de;q=0.8',
          'connection': 'keep-alive',
          'content-length': '136',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          # 'cookie': b,
          'cookie': f'JSESSIONID={jsessionid}',
          'host': 'www.makevoyage.com',
          'origin': 'https://www.makevoyage.com',
          'referer': f'https://www.makevoyage.com/series-fare-search.jsp?org={Origin}&des={Destination}',
          'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
          'x-requested-with': 'XMLHttpRequest'
      }

      response = requests.request("POST",url, headers=headers, data=payload)
      a = response.text
      print()

      my_xml = response.text
      dict_data = xmltodict.parse(my_xml)

      json_data = json.dumps(dict_data)
      json_data = json.loads(json_data)
      json_data = json_data['Root']['Result']


      if json_data == 'RRRRRR':
          ls1['results'] =  {"status":200,"HasResults":False,"data":list()}
          return ls1

      if json_data == None:
          ls1['results'] = {"status": 200, "HasResults": False, "data": list()}
          return ls1


      # ls = {"results": list()}
      res_json = dict()
      main_result_list = list()

      if ':::' in json_data:
        b = json_data.split(':::')


        for info in b:
          result = {"Departure_Sector": None, "Arrival_Sector": None,
                    "Airlines": None, "Flight_number": None,
                    "No_of_stops": None, "Departure_Date_&_time": None,
                    "Arrival_Date_&_time": None,"No_of_available_seats": None,
                    "Price_per_seat": {}, "Domain": {}}
          c = str(info).split(",")

          result["Departure_Sector"] = str(c[3])
          result["Arrival_Sector"] = str(c[4])
          result["Airlines"] = ''
          result["Flight_number"] = str(c[0] + "-" + c[1])
          result["No_of_stops"] = "Non Stop"
          result["Departure_Date_&_time"] = str(c[7]) + str(c[5])
          # result["Departure_Time"] = str(c[5])
          result["Arrival_Date_&_time"] = str(c[8]) + str(c[6])
          # result["Arrival_Time"] = str(c[6])
          result["No_of_available_seats"] = str(c[21])
          result["Price_per_seat"]["adult"] = str(c[28])
          result["Price_per_seat"]["child"] = str(c[29])
          result["Price_per_seat"]["infant"] = str(c[30])
          result["Domain"] = 'makevoyage'
          main_result_list.append(result)
          # ls["results"].append(result)
          res_json['results'] = {"status":200,"HasResults":True,"data":main_result_list}

        return res_json

      else:
        result = {"Departure_Sector": None, "Arrival_Sector": None,
                    "Airlines": None, "Flight_number": None,
                    "No_of_stops": None, "Departure_Date_&_time": None,
                    "Arrival_Date_&_time": None, "No_of_available_seats": None,
                    "Price_per_seat": {}, "Domain": {}}

        c = json_data.split(",")
        result["Departure_Sector"] = str(c[3])
        for i in flight_code_json:

            if i['airport_code'] == result["Departure_Sector"]:
                result["Departure_Sector"] = i['places']
        result["Arrival_Sector"] = str(c[4])

        for j in flight_code_json:

            if j['airport_code'] == result['Arrival_Sector']:
                result['Arrival_Sector'] = j['places']
        result["Airlines"] = ''
        result["Flight_number"] = str(c[0] + "-" + c[1])
        result["No_of_stops"] = "Non Stop"
        Departure_Date = str(c[7])
        Departure_Date = Departure_Date[:4] + "-" + Departure_Date[4:6] + "-" + Departure_Date[6:]
        Departure_Time = str(c[5])
        Departure_Time = Departure_Time[:2] + ":" + Departure_Time[2:]
        result["Departure_Date_&_time"] = Departure_Date + " " + Departure_Time

        Arrival_Date = str(c[8])
        Arrival_Date = Arrival_Date[:4] + "-" +  Arrival_Date[4:6] + "-" + Arrival_Date[6:]

        Arrival_Time = str(c[6])
        Arrival_Time= Arrival_Time[:2] + ":" + Arrival_Time[2:]

        result['Arrival_Date_&_time'] = Arrival_Date + " " + Arrival_Time
        result["No_of_available_seats"] = str(c[21])
        result["Price_per_seat"]["adult"] = str(c[28])
        if result["Price_per_seat"]["adult"] == '0.0':
            result["Price_per_seat"]["adult"] = None

        result["Price_per_seat"]["child"] = str(c[29])
        if result["Price_per_seat"]["child"] == "0.0":
            result["Price_per_seat"]["child"] = None

        result["Price_per_seat"]["infant"] = str(c[30])
        if result["Price_per_seat"]["infant"] == '0.0':
            result["Price_per_seat"]["infant"] = None
        result["Domain"] = 'makevoyage'
        main_result_list.append(result)

        res_json['results'] = {"status": 200, "HasResults": True, "data": main_result_list}


        return res_json


def flydreamzz_json(param_json):
    origin = param_json['origin']
    destination = param_json['destination']
    depart_date = param_json['depart_date']

    ls1 = {"results": dict()}


    flight_code_json = [{"places": "Agartala", "airport_code": "IXA"}, {"places": "Ahmedabad", "airport_code": "AMD"},
                        {"places": "Aizawl", "airport_code": "AJL"}, {"places": "Aurangabad", "airport_code": "IXU"},
                        {"places": "Amritsar", "airport_code": "ATQ"}, {"places": "Bagdogra", "airport_code": "IXB"},
                        {"places": "Bengaluru", "airport_code": "BLR"},
                        {"places": "Bhubaneswar", "airport_code": "BBI"}, {"places": "Bhopal", "airport_code": "BHO"},
                        {"places": "Chandigarh", "airport_code": "IXC"}, {"places": "Chennai", "airport_code": "MAA"},
                        {"places": "Coimbatore", "airport_code": "CJB"}, {"places": "Dehradun", "airport_code": "DED"},
                        {"places": "Delhi", "airport_code": "DEL"}, {"places": "Dibrugarh", "airport_code": "DIB"},
                        {"places": "Dimapur", "airport_code": "DMU"}, {"places": "Durgapur", "airport_code": "RDP"},
                        {"places": "Gaya", "airport_code": "GAY"}, {"places": "Goa", "airport_code": "GOI"},
                        {"places": "Gorakhpur", "airport_code": "GOP"}, {"places": "Guwahati", "airport_code": "GAU"},
                        {"places": "Hubli", "airport_code": "HBX"}, {"places": "Hyderabad", "airport_code": "HYD"},
                        {"places": "Imphal", "airport_code": "IMF"}, {"places": "Indore", "airport_code": "IDR"},
                        {"places": "Jabalpur", "airport_code": "JLR"}, {"places": "Jaipur", "airport_code": "JAI"},
                        {"places": "Jammu", "airport_code": "IXJ"}, {"places": "Jodhpur", "airport_code": "JDH"},
                        {"places": "Jorhat", "airport_code": "JRH"}, {"places": "Kannur", "airport_code": "CNN"},
                        {"places": "Kurnool", "airport_code": "KJB"}, {"places": "Kochi", "airport_code": "COK"},
                        {"places": "Kolhapur", "airport_code": "KLH"}, {"places": "Kolkata", "airport_code": "CCU"},
                        {"places": "Kozhikode", "airport_code": "CCJ"}, {"places": "Lucknow", "airport_code": "LKO"},
                        {"places": "Madurai", "airport_code": "IXM"}, {"places": "Mangaluru", "airport_code": "IXE"},
                        {"places": "Mumbai", "airport_code": "BOM"}, {"places": "Mysuru", "airport_code": "MYQ"},
                        {"places": "Nagpur", "airport_code": "NAG"}, {"places": "Patna", "airport_code": "PAT"},
                        {"places": "Prayagraj", "airport_code": "IXD"}, {"places": "Pune", "airport_code": "PNQ"},
                        {"places": "Portblair", "airport_code": "IXZ"}, {"places": "Raipur", "airport_code": "RPR"},
                        {"places": "Rajahmundry", "airport_code": "RJA"}, {"places": "Ranchi", "airport_code": "IXR"},
                        {"places": "Shillong", "airport_code": "SHL"}, {"places": "Shirdi", "airport_code": "SAG"},
                        {"places": "Silchar", "airport_code": "IXS"}, {"places": "Srinagar", "airport_code": "SXR"},
                        {"places": "Surat", "airport_code": "STV"},
                        {"places": "Thiruvananthapuram", "airport_code": "TRV"},
                        {"places": "Tiruchirappalli", "airport_code": "TRZ"},
                        {"places": "Tirupati", "airport_code": "TIR"}, {"places": "Tuticorin", "airport_code": "TCR"},
                        {"places": "Udaipur", "airport_code": "UDR"}, {"places": "Vadodara", "airport_code": "BDQ"},
                        {"places": "Varanasi", "airport_code": "VNS"}, {"places": "Vijayawada", "airport_code": "VGA"},
                        {"places": "Visakhapatnam", "airport_code": "VTZ"}, {"places": "Kannur", "airport_code": "CNN"},
                        {"places": "Agartala", "airport_code": "IXA"}, {"places": "Ahmedabad", "airport_code": "AMD"},
                        {"places": "Amritsar", "airport_code": "ATQ"}, {"places": "Bagdogra", "airport_code": "IXB"},
                        {"places": "Bengaluru", "airport_code": "BLR"},
                        {"places": "Bhubaneswar", "airport_code": "BBI"}, {"places": "Bhopal", "airport_code": "BHO"},
                        {"places": "Chandigarh", "airport_code": "IXC"}, {"places": "Chennai", "airport_code": "MAA"},
                        {"places": "Coimbatore", "airport_code": "CJB"}, {"places": "Dehradun", "airport_code": "DED"},
                        {"places": "Delhi", "airport_code": "DEL"}, {"places": "Dimapur", "airport_code": "DMU"},
                        {"places": "Goa", "airport_code": "GOI"}, {"places": "Gorakhpur", "airport_code": "GOP"},
                        {"places": "Guwahati", "airport_code": "GAU"}, {"places": "Hubli", "airport_code": "HBX"},
                        {"places": "Hyderabad", "airport_code": "HYD"}, {"places": "Imphal", "airport_code": "IMF"},
                        {"places": "Indore", "airport_code": "IDR"}, {"places": "Jabalpur", "airport_code": "JLR"},
                        {"places": "Jaipur", "airport_code": "JAI"}, {"places": "Jammu", "airport_code": "IXJ"},
                        {"places": "Kolkata", "airport_code": "CCU"}, {"places": "Kozhikode", "airport_code": "CCJ"},
                        {"places": "Lucknow", "airport_code": "LKO"}, {"places": "Madurai", "airport_code": "IXM"},
                        {"places": "Mangaluru", "airport_code": "IXE"}, {"places": "Mumbai", "airport_code": "BOM"},
                        {"places": "Nagpur", "airport_code": "NAG"}, {"places": "Patna", "airport_code": "PAT"},
                        {"places": "Pune", "airport_code": "PNQ"}, {"places": "Raipur", "airport_code": "RPR"},
                        {"places": "Rajahmundry", "airport_code": "RJA"}, {"places": "Ranchi", "airport_code": "IXR"},
                        {"places": "Srinagar", "airport_code": "SXR"}, {"places": "Surat", "airport_code": "STV"},
                        {"places": "Thiruvananthapuram", "airport_code": "TRV"},
                        {"places": "Tiruchirappalli", "airport_code": "TRZ"},
                        {"places": "Tuticorin", "airport_code": "TCR"}, {"places": "Udaipur", "airport_code": "UDR"},
                        {"places": "Vadodara", "airport_code": "BDQ"}, {"places": "Varanasi", "airport_code": "VNS"},
                        {"places": "Vijayawada", "airport_code": "VGA"},
                        {"places": "Visakhapatnam", "airport_code": "VTZ"}, {"places": "Gaya", "airport_code": "GAY"},
                        {"places": "Jodhpur", "airport_code": "JDH"}, {"places": "Silchar", "airport_code": "IXS"},
                        {"places": "Belagavi", "airport_code": "IXG"}]

    url = "https://api.flydreamzz.in/getDashboard/"

    payload = "{\"filters\":{\"traveldate__contains\":\""+depart_date+"\",\"airportfrom__name\":\""+origin+"\",\"airportto__name\":\""+destination+"\"},\"username\":\"agent.sneha14\"}"

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,de;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://www.flydreamzz.in',
        'Referer': 'https://www.flydreamzz.in/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    a = response.text
    print()


    res_json = dict()
    try:
        json_data = json.loads(response.text)

        if json_data['data'] == []:
            res_json['result'] = {"status": 200, "HasResults": True, "data": 'No data Available'}
            return res_json
        try:
            for data in json_data['data']:



                if len(json_data['data']) == 1:

                    if data['bookingtype'] == 'online':
                        # data[0].bookingtype
                        result = {"Departure_Sector": None, "Arrival_Sector": None,
                                  "Airlines": None, "Flight_number": None,
                                  "No_of_stops": None, "Departure_Date_&_time": None,
                                  "Arrival_Date_&_time": None, "No_of_available_seats": None,
                                  "Price_per_seat": {'adult': None, 'child': None, 'infant': None}, "Domain": {}}

                        result["Departure_Sector"] = data['destination'].split(" ")[0]
                        # print(result["Departure_Sector"])

                        for i in flight_code_json:

                            if i['airport_code'] == result["Departure_Sector"]:
                                result["Departure_Sector"] = i['places']

                        result['Arrival_Sector'] = data['destination'].split(" ")[2]

                        for j in flight_code_json:

                            if j['airport_code'] == result['Arrival_Sector']:
                                result['Arrival_Sector'] = j['places']

                        try:
                            result['Airlines'] = data['airlines']
                        except:
                            result['Airlines'] = data = None
                        try:
                            result['Flight_number'] = data['flightno']
                        except:
                            result['Flight_number'] = data = None
                        try:
                            result['Departure_Date_&_time'] = data['traveldate'] + " " + data['departure']
                        except:
                            result['Departure_Date_&_time'] = None
                        try:
                            result['Arrival_Date_&_time'] = data['traveldate'] + " " + data['arrival']
                        except:
                            result['Arrival_Date_&_time'] = None
                        result['No_of_stops'] = ''
                        try:
                            result['No_of_available_seats'] = data['availableseats']
                        except:
                            result['No_of_available_seats'] = None
                        try:
                            result['Price_per_seat']['adult'] = data['deal']
                        except:
                            result['Price_per_seat']['adult'] = None

                        result['Price_per_seat']['child'] = None

                        result['Price_per_seat']['infant'] = None

                        result['Domain'] = 'flydreamzz.in'

                        res_json['result'] = {"status": 200, "HasResults": True, "data": result}
                        return res_json
                    else:
                        result = []
                        res_json['result'] = {"status": 200, "HasResults": True, "data": result}
                        return res_json['result']
                else:
                    ls = []
                    if data['bookingtype'] == 'online':
                        # data[0].bookingtype
                        result = {"Departure_Sector": None, "Arrival_Sector": None,
                                  "Airlines": None, "Flight_number": None,
                                  "No_of_stops": None, "Departure_Date_&_time": None,
                                  "Arrival_Date_&_time": None, "No_of_available_seats": None,
                                  "Price_per_seat": {'adult': None, 'child': None, 'infant': None}, "Domain": {}}

                        result["Departure_Sector"] = data['destination'].split(" ")[0]
                        print(result["Departure_Sector"])

                        for i in flight_code_json:

                            if i['airport_code'] == result["Departure_Sector"]:
                                result["Departure_Sector"] = i['places']

                        result['Arrival_Sector'] = data['destination'].split(" ")[2]

                        for j in flight_code_json:

                            if j['airport_code'] == result['Arrival_Sector']:
                                result['Arrival_Sector'] = j['places']

                        try:
                            result['Airlines'] = data['airlines']
                        except:
                            result['Airlines'] = data = None
                        try:
                            result['Flight_number'] = data['flightno']
                        except:
                            result['Flight_number'] = data = None
                        try:
                            result['Departure_Date_&_time'] = data['traveldate'] + " " + data['departure']
                        except:
                            result['Departure_Date_&_time'] = None
                        try:
                            result['Arrival_Date_&_time'] = data['traveldate'] + " " + data['arrival']
                        except:
                            result['Arrival_Date_&_time'] = None
                        result['No_of_stops'] = ''
                        try:
                            result['No_of_available_seats'] = data['availableseats']
                        except:
                            result['No_of_available_seats'] = None
                        try:
                            result['Price_per_seat']['adult'] = data['deal']
                        except:
                            result['Price_per_seat']['adult'] = None
                        try:
                            result['Price_per_seat']['child'] = data['deal']
                        except:
                            result['Price_per_seat']['child'] = None
                        try:
                            result['Price_per_seat']['infant'] = data['deal']
                        except:
                            result['Price_per_seat']['infant'] = None
                        result['Domain'] = 'flydreamzz.in'

                        ls.append(result)

                    res_json['result'] = {"status": 200, "HasResults": True, "data": ls}
                    return res_json
        except Exception as e:
            print(e)
            res_json['result'] = {"status": 200, "HasResults": True, "data": "Data not available on site"}
    except Exception as e:
        print(e)

        res_json['result'] = {"status": 200, "HasResults": True, "data": "Data not available on site"}
        return res_json

