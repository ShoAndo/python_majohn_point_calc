from flask import Flask, render_template, request

app = Flask(__name__)
POINT_TOO_HIGH = 'すみません、よく分かりません'

def calc_point(par_or_ch, tsumo_or_ron, han, hu):
    han = int(han)
    hu = int(hu)
    point = ''
    if par_or_ch == "親":
        if tsumo_or_ron == 'ツモ':
            if han == 1:
                if hu == 30:
                    point = '800オール'
                elif hu == 40:
                    point = '1100オール'
                elif hu == 50:
                    point = '1200オール'
                elif hu == 60:
                    point = '1500オール'
                else:
                    point = POINT_TOO_HIGH
            elif han == 2:
                if hu == 20:
                    point = '1100オール'
                elif hu == 30:
                    point = '1500オール'
                elif hu == 40:
                    point = '2000オール'
                elif hu == 50:
                    point = '2400オール'
                elif hu == 60:
                    point = '3000オール'
                else:
                    point = POINT_TOO_HIGH
            elif han == 3:
                if hu == 20:
                    point = '2000オール'
                elif hu == 25:
                    point = '2400'
                elif hu == 30:
                    point = '3000オール'
                elif hu == 40:
                    point = '3900オール'
                elif hu == 50:
                    point = '4800オール'
                else:
                    point = '6000オール'
            elif han == 4:
                if hu == 20:
                    point = '3900オール'
                elif hu == 25:
                    point = '4800オール'
                else:
                    point = '6000オール'
            elif han == 5:
                point = '6000オール'
            elif 6 <= han <= 7:
                point = '9000オール'
            elif 8 <= han <= 10:
                point = '12000オール'
            elif 11 <= han <= 12:
                point = '18000オール'
            else:
                point = '24000オール'
        else:
            if han == 1:
                if hu == 30:
                    point = '1500'
                elif hu == 40:
                    point = '2000'
                elif hu == 50:
                    point = '2400'
                elif hu == 60:
                    point = '2900'
                else:
                    point = POINT_TOO_HIGH
            elif han == 2:
                if hu == 25:
                    point = '2400'
                elif hu == 30:
                    point = '2900'
                elif hu == 40:
                    point = '3900'
                elif hu == 50:
                    point = '4800'
                elif hu == 60:
                    point = '5800'
                else:
                    point = POINT_TOO_HIGH
            elif han == 3:
                if hu == 20:
                    point = '3900'
                elif hu == 25:
                    point = '4800'
                elif hu == 30:
                    point = '5800'
                elif hu == 40:
                    point = '7700'
                elif hu == 50:
                    point = '9600'
                else:
                    point = '12000'
            elif han == 4:
                if hu == 20:
                    point = '7700'
                elif hu == 25:
                    point = '9600'
                else:
                    point = '12000'
            elif han == 5:
                point = '12000'
            elif 6 <= han <= 7:
                point = '18000'
            elif 8 <= han <= 10:
                point = '24000'
            elif 11 <= han <= 12:
                point = '36000'
            else:
                point = '48000'
    else:
        if tsumo_or_ron == 'ツモ':
            if han == 1:
                if hu == 30:
                    point = '500/700'
                elif hu == 40:
                    point = '600/900'
                elif hu == 50:
                    point = '600/1000'
                elif hu == 60:
                    point = '800/1300'
                else:
                    point = POINT_TOO_HIGH
            elif han == 2:
                if hu == 20:
                    point = '600/900'
                elif hu == 30:
                    point = '800/1300'
                elif hu == 40:
                    point = '1100/1700'
                elif hu == 50:
                    point = '1200/2000'
                elif hu == 60:
                    point = '1500/2500'
                else:
                    point = POINT_TOO_HIGH
            elif han == 3:
                if hu == 20:
                    point = '1100/1700'
                elif hu == 25:
                    point = '1200/2000'
                elif hu == 30:
                    point = '1500/2500'
                elif hu == 40:
                    point = '2000/3300'
                elif hu == 50:
                    point = '2400/4000'
                else:
                    point = '3000/5000'
            elif han == 4:
                if hu == 20:
                    point = '2000/3300'
                elif hu == 25:
                    point = '2400/4000'
                else:
                    point = '3000/5000'
            elif han == 5:
                point = '3000/5000'
            elif 6 <= han <= 7:
                point = '4500/7500'
            elif 8 <= han <= 10:
                point = '6000/10000'
            elif 11 <= han <= 12:
                point = '9000/15000'
            else:
                point = '12000/20000'
        else:
            if han == 1:
                if hu == 30:
                    point = '1000'
                elif hu == 40:
                    point = '1300'
                elif hu == 50:
                    point = '1600'
                elif hu == 60:
                    point = '2000'
                else:
                    point = POINT_TOO_HIGH
            elif han == 2:
                if hu == 25:
                    point = '1600'
                elif hu == 30:
                    point = '2000'
                elif hu == 40:
                    point = '2600'
                elif hu == 50:
                    point = '3200'
                elif hu == 60:
                    point = '3900'
                else:
                    point = POINT_TOO_HIGH
            elif han == 3:
                if hu == 20:
                    point = '2600'
                elif hu == 25:
                    point = '3200'
                elif hu == 30:
                    point = '3900'
                elif hu == 40:
                    point = '5200'
                elif hu == 50:
                    point = '6400'
                else:
                    point = '8000'
            elif han == 4:
                if hu == 20:
                    point = '5200'
                elif hu == 25:
                    point = '6400'
                else:
                    point = '8000'
            elif han == 5:
                point = '8000'
            elif 6 <= han <= 7:
                point = '12000'
            elif 8 <= han <= 10:
                point = '18000'
            elif 11 <= han <= 12:
                point = '24000'
            else:
                point = '32000'
    return point

def validation(name, val):
    err_msg = ''
    if not val:
        err_msg = f'{name}を入力してください'
    return err_msg



@app.route('/' ,methods=["GET", "POST"])
def index():
    if request.method=='POST':
        res = {}
        res["par_or_ch"] = request.form.get('par_or_ch', '')
        res["tsumo_or_ron"] = request.form.get('tsumo_or_ron', '')
        res["han"] = request.form.get('han', '')
        res["hu"] = request.form.get('hu', '')
        res["err_par_or_ch"] = validation("親か子", res["par_or_ch"])
        res["err_tsumo_or_ron"] = validation('ツモかロン', res["tsumo_or_ron"])
        res["err_han"] = validation('翻', res['han'])
        res["err_hu"] = validation('符', res['hu'])

        if not res["err_par_or_ch"] and not res["err_tsumo_or_ron"] and not res["err_han"] and not res["err_hu"]:
            res["point"] = calc_point(res["par_or_ch"], res["tsumo_or_ron"], res["han"], res['hu'])

        return render_template('index13.html', res=res)

    else:
        return render_template('index13.html')

if __name__ == '__main__':
    app.run()