import streamlit as st

# Streamlit アプリのタイトル
st.title('BMI計算アプリ')

# 身長と体重の入力を受け取る
height = st.number_input('身長を入力してください (cm)', min_value=0.0, step=0.1)
weight = st.number_input('体重を入力してください (kg)', min_value=0.0, step=0.1)

# BMIを計算する
if height > 0 and weight > 0:
    height_m = height / 100  # 身長をメートルに変換
    bmi = weight / (height_m ** 2)  # BMIの計算
    st.write(f'あなたのBMIは: {bmi:.2f} です。')

    # BMIに基づいて判定を表示
    if bmi < 18.5:
        st.write("判定: やせ")
    elif 18.5 <= bmi < 25:
        st.write("判定: 普通")
    else:
        st.write("判定: 肥満")
else:
    st.write('身長と体重を入力してください。')
