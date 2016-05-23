# -- coding: utf-8 --
from app import app
from flask import render_template, request, jsonify
from nocache import nocache
import json
from langdetect import detect_langs


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

# шифрование
@app.route('/crypt')
def crypting():

    crypt = request.args.get('crypt')
    stepCr = request.args.get('step', 0, type=int)
    # вычисление количества каждого символа в строке
    let = [i for i in crypt]
    couL = [crypt.count(i) for i in let]
    alaP = dict(zip(let, couL))
    alaP = [[a, alaP[a]] for a in sorted(alaP)]
    # добавление значения цвета для реализации чередующихся по цвету стобцов диаграммы
    [i.append("#f44336") for i in alaP[::2]]
    [i.append("#03A9F4") for i in alaP[1::2]]
    #смещение символа i на шаг step
    def rotChr(i, step):
        if i.isalpha():
            if ord(i) in range(65, 91):

                if (ord(i) + step) in range(65, 91):
                    i = chr(ord(i) + step)
                else:
                    i = chr(64 + (ord(i) + step) - 90)
            else:
                if (ord(i) + step) in range(97, 123):
                    i = chr(ord(i) + step)
                else:
                    i = chr(96 + (ord(i) + step) - 122)

        return i
    #смещение каждого символа в строке a на шаг stepCr
    def strRot(a):

        return ("".join([rotChr(i, stepCr) for i in a]))
    #запись данных в файл
    fo = open('data', 'a')
    fo.write(json.dumps(
        {"input": crypt, "step": stepCr, "output": strRot(crypt)}) + "\n")
    fo.close()
    return jsonify(result=strRot(crypt), cou=alaP)

# расшифровывание
@app.route('/decrypt')
def deCrypting():

    crypt = request.args.get('crypt')
    stepCr = request.args.get('step', 0, type=int)
    # вычисление количества каждого символа в строке
    let = [i for i in crypt]
    couL = [crypt.count(i) for i in let]
    alaP = dict(zip(let, couL))
    alaP = [[a, alaP[a]] for a in sorted(alaP)]
    # добавление значения цвета для реализации чередующихся по цвету стобцов диаграммы
    [i.append("#f44336") for i in alaP[::2]]
    [i.append("#03A9F4") for i in alaP[1::2]]
    #смещение символа i на шаг step
    def rotChr(i, step):
        if i.isalpha():
            if ord(i) in range(65, 91):

                if (ord(i) - step) in range(65, 91):
                    i = chr(ord(i) - step)
                else:
                    i = chr(91 - (65 - (ord(i) - step)))
            else:
                if (ord(i) - step) in range(97, 123):
                    i = chr(ord(i) - step)
                else:
                    i = chr(123 - (97 - (ord(i) - step)))

        return i
    #смещение каждого символа в строке a на шаг stepCr
    def strRot(a):

        return ("".join([rotChr(i, stepCr) for i in a]))
    return jsonify(result=strRot(crypt), cou=alaP)


@app.route('/')
def index():
    return render_template('index.html')

# определение шага шифрования
@app.route('/whatstep')
def whatstep():
    crypt = request.args.get('crypt')
    stepCr = 26
    #смещение символа i на шаг step
    def rotChr(i, step):
        if i.isalpha():
            if ord(i) in range(65, 91):

                if (ord(i) - step) in range(65, 91):
                    i = chr(ord(i) - step)
                else:
                    i = chr(91 - (65 - (ord(i) - step)))
            else:
                if (ord(i) - step) in range(97, 123):
                    i = chr(ord(i) - step)
                else:
                    i = chr(123 - (97 - (ord(i) - step)))

        return i
    #смещение каждого символа в строке a на шаг stepCr
    def strRot(a):
        return ("".join([rotChr(i, stepCr) for i in a]))
    #определение языка строки a
    def detectLang(a):
        det = detect_langs(a)
        # извлечение процентного значения принадлежность строки к английскому языку
        det = [str(i).split(":") for i in det]
        det = [y for z, y in det if z == "en"]
        if det:
            det = float(det[0])
        else:
            det = 0
        return det

    detect = detectLang(strRot(crypt))
    #смещения символов строки происходят пока вероятность того что строка на английском
    # языке не станет больше 90%
    while stepCr > 0:
        stepCr -= 1
        detect = detectLang(strRot(crypt))
        if detect >= 0.90:
            return jsonify(result="Caesar said that the text is encrypted with ROTN = " + str(stepCr))
            break
    return jsonify(result="Caesar said that the text is not encrypted")



if __name__=="__main__":
    app.run()
