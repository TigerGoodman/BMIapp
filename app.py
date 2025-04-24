import streamlit as st

st.title("BMI")
kg= st.number_input("น้ำหนัก (KG.)",value=60.5, min_value=10.0 ,max_value=200.0 ,step=0.5)
cm= st.number_input ("ส่วนสูง (CM.)",value=100, min_value=1 ,max_value=200 ,step=1)

if st.button ("Calculate"):
    bmi=kg/(cm/100)**2
    st.subheader(f"ค่าดัชนีมวลกายของคุณคือ {bmi:.1f}")

    if (bmi) < 18.5:
        st.error("น้ำหนักต่ำกว่าเกณฑ์")
        st.error("เสี่ยงโรคขาดสารอาหาร")    
        st.image("คนฟ้า.png.png","นี้อาจเป็นสภาพของคุณ")

    elif (bmi) < 23:
        st.success("น้ำหนักสมส่วน")
        st.success("โอกาสมีโรคแทรกซ้อนน้อย")
        st.image("คนเขียว.png.png","นี้อาจเป็นสภาพของคุณ")

    elif (bmi) < 25:
        st.warning("น้ำหนักเกินมาตรฐาน")
        st.warning("ภาวะน้ำหนักเกิน ระยะเริ่มต้น")
        st.image("คนเหลือง.png.png","นี้อาจเป็นสภาพของคุณ")

    elif (bmi) < 30:
        st.warning("น้ำหนักเกิน")
        st.warning("ภาวะน้ำหนักเกินมาก ระยะอ้วนเริ่มต้น")
        st.image("คนส้ม.png.png","นี้อาจเป็นสภาพของคุณ")

    elif (bmi) > 30:
        st.error("น้ำหนักเกินมาก")
        st.error("ภาวะน้ำหนักเกินมาก โรคอ้วน")
        st.image("คนแดง.png.png","นี้อาจเป็นสภาพของคุณ")
