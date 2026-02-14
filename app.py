import streamlit as st
import time

# Конфигурация страницы для солидного вида
st.set_page_config(
    page_title="BizBooster AI | Маркетинг на автопилоте",
    page_icon="🚀",
    layout="centered"
)

# Стилизация через CSS (чтобы сайт не выглядел как стандартный скрипт)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #007BFF; color: white; }
    .stTextInput>div>div>input { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Список ключей (можете менять их здесь сами)
VALID_KEYS = ["PREMIUM100", "VIP_ACCESS", "BIZ2026"]

st.title("🚀 BizBooster AI")
st.subheader("Ваш отдел маркетинга в одном окне")

# Боковая панель
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1998/1998664.png", width=100)
    st.title("Личный кабинет")
    user_key = st.text_input("Введите ключ доступа:", type="password", help="Ключ приходит на почту после оплаты")
    
    st.markdown("---")
    st.write("🆘 Поддержка:")
    st.write("admin@bizbooster.ai")

# Проверка доступа
if user_key in VALID_KEYS:
    st.success("✨ Доступ активирован. Добро пожаловать!")
    
    tab1, tab2, tab3 = st.tabs(["✍️ Тексты", "💬 Отзывы", "📈 Реклама"])
    
    with tab1:
        topic = st.text_input("О чем написать пост для соцсетей?")
        tone = st.select_slider("Тон текста:", options=["Дружелюбный", "Профессиональный", "Дерзкий"])
        if st.button("Сгенерировать пост"):
            with st.spinner('ИИ создает шедевр...'):
                time.sleep(1.5)
                st.info(f"Тут будет ваш готовый {tone} пост про {topic}...")
                
    with tab2:
        review = st.text_area("Вставьте отзыв клиента:")
        if st.button("Написать ответ"):
            st.success("Ответ готов! (Тут будет текст ответа)")

else:
    # Блок продажи
    st.info("💡 BizBooster AI экономит владельцу бизнеса до 150 часов работы в год.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Тариф 'Прорыв'")
        st.write("- ✅ Все инструменты")
        st.write("- ✅ Безлимитная генерация")
        st.write("- ✅ SEO-оптимизация")
        st.write("### $19 / мес")
    
    with col2:
        st.write("### Как это работает?")
        st.write("1. Оплачиваете доступ")
        st.write("2. Получаете ключ на почту")
        st.write("3. Вводите его слева и работаете")

    st.markdown("---")
    # ЗАМЕНИТЕ ЭТУ ССЫЛКУ НА ВАШУ ИЗ LEMONSQUEEZY
    st.link_button("🔥 ОФОРМИТЬ ПОДПИСКУ СЕЙЧАС", "https://bizbooster.lemonsqueezy.com")
    
    st.image("https://img.freepik.com/free-vector/digital-marketing-abstract-concept-vector-illustration_335657-4884.jpg", caption="Развивайте бизнес, пока ИИ работает за вас")

