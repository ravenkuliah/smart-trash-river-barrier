import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Smart Trash River Barrier",
    page_icon="🌊",
    layout="wide"
)

st.title("🌊 Smart Trash River Barrier")
st.caption("Prototype simulasi pemantauan dan kendali sampah sungai berbasis IoT")

# Input simulasi
st.sidebar.header("Input Simulasi Sensor")
st.sidebar.write("Ubah nilai berikut untuk menguji respons sistem.")

water_level = st.sidebar.slider(
    "Ketinggian air (cm)", min_value=0, max_value=200, value=35
)
trash_level = st.sidebar.slider(
    "Penumpukan sampah (%)", min_value=0, max_value=100, value=45
)
flow_rate = st.sidebar.slider(
    "Kecepatan aliran (m/s)", min_value=0.0, max_value=3.0,
    value=0.8, step=0.1
)

st.sidebar.divider()
st.sidebar.subheader("Pengaturan ambang batas")
water_limit = st.sidebar.number_input(
    "Batas ketinggian air (cm)", min_value=1, max_value=200, value=120
)
trash_limit = st.sidebar.slider(
    "Batas penumpukan sampah (%)", min_value=1, max_value=100, value=80
)
flow_limit = st.sidebar.number_input(
    "Batas kecepatan aliran (m/s)", min_value=0.1, max_value=3.0,
    value=2.0, step=0.1
)

# Logika kendali simulasi
if water_level >= water_limit or flow_rate >= flow_limit:
    condition = "MODE KESELAMATAN"
    condition_color = "🔴"
    barrier_status = "Terbuka (simulasi)"
    actuator_position = 90
    alert = "Ketinggian air atau aliran melewati batas. Sistem masuk mode keselamatan."
elif trash_level >= trash_limit:
    condition = "SAMPAH MENUMPUK"
    condition_color = "🟠"
    barrier_status = "Aktif mengarahkan sampah (simulasi)"
    actuator_position = 45
    alert = "Penumpukan sampah melewati ambang batas."
else:
    condition = "NORMAL"
    condition_color = "🟢"
    barrier_status = "Standby"
    actuator_position = 0
    alert = "Kondisi berada dalam batas operasi simulasi."

st.subheader("Ringkasan kondisi sistem")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Ketinggian air", f"{water_level} cm")
c2.metric("Penumpukan sampah", f"{trash_level}%")
c3.metric("Kecepatan aliran", f"{flow_rate:.1f} m/s")
c4.metric("Posisi aktuator", f"{actuator_position}°")

st.divider()

left, right = st.columns([1.2, 1])
with left:
    st.subheader("Status operasi")
    st.markdown(f"### {condition_color} {condition}")
    st.write(f"**Status barrier:** {barrier_status}")
    st.write(f"**Respons aktuator:** {actuator_position}°")
    st.info(alert)

with right:
    st.subheader("Simulasi mekanisme barrier")
    st.write("Ilustrasi posisi aktuator berdasarkan logika kendali:")
    if actuator_position == 0:
        st.success("Barrier: posisi standby")
    elif actuator_position == 45:
        st.warning("Barrier: posisi pengarah sampah")
    else:
        st.error("Barrier: posisi keselamatan")

    st.progress(min(trash_level, 100) / 100, text=f"Penumpukan sampah: {trash_level}%")

st.divider()
st.subheader("Logika kendali yang digunakan")
st.markdown(
    """
    1. **Mode keselamatan:** aktif jika ketinggian air atau kecepatan aliran
       mencapai/melebihi ambang batas. Simulasi mengubah aktuator ke 90°.
    2. **Sampah menumpuk:** aktif jika penumpukan sampah mencapai/melebihi
       ambang batas. Simulasi mengubah aktuator ke 45°.
    3. **Normal:** jika semua parameter di bawah ambang batas, aktuator berada
       pada posisi standby 0°.
    """
)

st.caption(
    "Catatan: seluruh nilai sensor dan gerakan aktuator pada aplikasi ini "
    "merupakan simulasi perangkat lunak. Aplikasi belum terhubung ke sensor "
    "fisik, ESP32, atau mekanisme barrier nyata."
)
st.caption(f"Terakhir diperbarui: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

