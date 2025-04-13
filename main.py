import streamlit as st
from streamlit_option_menu import option_menu
import my_pages as mp

menu = ["Trang chủ", "Yêu cầu của doanh nghiệp","Các thuật toán thử nghiệm", "Lựa chọn kết quả","Ứng dụng phân nhóm"]
with st.sidebar:
    selected = option_menu("Menu chính", menu, 
        icons=['house', '1-square', '2-square','3-square','4-square'], menu_icon="cast", default_index=0)
    
if selected == "Trang chủ":
    mp.trang_chu(st)
elif selected=="Yêu cầu của doanh nghiệp":
    mp.yeu_cau_cua_doanh_nghiep(st)    
elif selected=="Các thuật toán thử nghiệm":
    mp.cac_thuat_toan_thu_nghiem(st)
elif selected=="Lựa chọn kết quả":
    mp.lua_chon_ket_qua(st)
elif selected=="Ứng dụng phân nhóm":
    mp.ung_dung_phan_nhom(st)

#-------------------------------------------------------------
st.sidebar.subheader("📒 Nhóm thực hiện:")
st.sidebar.write("* Nguyễn Tuấn Anh")   
st.sidebar.write("* Phan Ngọc Phương Bắc") 
st.sidebar.subheader("👩‍🏫 Giảng viên:")   
st.sidebar.write("- Cô Khuất Thùy Phương")
st.sidebar.write("**📆 Ngày báo cáo: 13/04/2025**")