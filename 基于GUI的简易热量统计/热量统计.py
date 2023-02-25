import PySimpleGUI as sg


sg.theme('LightBlue2')

layout=[
            [sg.T('食物：',font=('宋体',20))],
            [sg.T('种类：',font=('宋体',15)),sg.In('',10,font=('宋体',15)),sg.In('',10,font=('宋体',15)),sg.T('克重',font=('宋体',15)),sg.B('  热量  ',key='calorie1',font=('宋体',18))],
            [sg.T('种类：',font=('宋体',15)),sg.In('',10,font=('宋体',15)),sg.In('',10,font=('宋体',15)),sg.T('克重',font=('宋体',15))],
            [sg.T('种类：',font=('宋体',15)),sg.In('',10,font=('宋体',15)),sg.In('',10,font=('宋体',15)),sg.T('克重',font=('宋体',15))],
            [sg.T('种类：',font=('宋体',15)),sg.In('',10,font=('宋体',15)),sg.In('',10,font=('宋体',15)),sg.T('克重',font=('宋体',15))],
            [sg.B('  重复  ',key='re1',font=('宋体',18),pad=(130,10))],
            [sg.T('总摄入量：',font=('宋体',20)),sg.T('',font=('宋体',20),key='total1')],
            [sg.T('',font=('宋体',15))],
            [sg.T('',font=('宋体',15))],
            [sg.T('运动：',font=('宋体',20))],
            [sg.T('种类：',font=('宋体',15)),sg.In('',10,font=('宋体',15)),sg.T('时间：',font=('宋体',15)),sg.In('',10,font=('宋体',15)),sg.B('  热量  ',key='calorie2',font=('宋体',18))],
            [sg.B('  重复  ',key='re2',font=('宋体', 18), pad=(130, 10))],
            [sg.T('总消耗量：',font=('宋体', 20)), sg.T('', font=('宋体', 20), key='total2')]

 ]

windows=sg.Window('热量统计',layout)

calories_per_unit = 0
calories_consumed = 0
total_calories = 0
calories_per_min = 0

calories_per_kg = {
    "蔬菜": 0.025,
    "苹果": 0.5,
    "米饭": 1.16,
    "猪肉": 2.71

}

calories_per_minute = {
    "跑步": 10,
    "骑自行车": 8,
    "游泳": 12,
    "篮球": 6,
    "足球": 8,
    "网球": 5
}


while True:
    event,values=windows.read()
    if event == None:
            break
    if event == 'calorie1':
        for i in range(4):
            food=values[i*2]
            if food in calories_per_kg:
                amount=float(values[i*2+1])
                calories_per_unit=calories_per_kg[food]
                calories_consumed=calories_consumed + calories_per_unit * amount
        windows['total1'].update(value=format(calories_consumed,'.3f')+'千卡')

    if event == 'calorie2':
        for i in range(4,5):
            activity=values[i*2]
            if activity in calories_per_minute:
                time_minutes =float(values[i * 2 + 1])
                calories_per_min = calories_per_minute[activity]
                total_calories =total_calories + calories_per_min * time_minutes
        windows['total2'].update(value=format(total_calories,'.3f')+'千卡')

    if event =='re1':
        calories_consumed = 0
        calories_per_unit = 0
        windows['total1'].update(value='')
        windows[0].update(value='')
        windows[1].update(value='')
        windows[2].update(value='')
        windows[3].update(value='')
        windows[4].update(value='')
        windows[5].update(value='')
        windows[6].update(value='')
        windows[7].update(value='')

    if event =='re2':
        total_calories = 0
        calories_per_min = 0
        windows['total2'].update(value='')
        windows[8].update(value='')
        windows[9].update(value='')

windows.close()