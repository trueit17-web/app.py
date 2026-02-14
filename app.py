import streamlit as st
from openai import OpenAI

# 1. Настройка страницы
st.set_page_config(page_title="BizBooster AI Pro", page_icon="🚀")

# 2. Инициализация OpenAI (Безопасно)
client = None
if "OPENAI_API_KEY" in st.secrets:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
else:
    st.error("⚠️ Настройте API ключ в Secrets (Settings -> Secrets) на Streamlit Cloud!")
    st.stop()

# 3. База ключей доступа
VALID_KEYS = ["PREMIUM100", "VIP_ACCESS", "BIZ2026"]

st.title("🚀 BizBooster AI: SEO & Marketing")

# 4. Боковая панель для входа
with st.sidebar:
    st.header("Вход в систему")
    user_key = st.text_input("Введите ваш лицензионный ключ:", type="password")
    st.markdown("---")
    if user_key in VALID_KEYS:
        st.success("Доступ активен ✅")
    else:
        st.info("Нужен ключ для работы")

# 5. Основная логика приложения
if user_key in VALID_KEYS:
    # Создаем вкладки, включая SEO
    tab1, tab2, tab3 = st.tabs(["🔍 SEO Статьи", "📢 Реклама", "💬 Отзывы"])

    # --- ВКЛАДКА SEO ---
    with tab1:
        st.subheader("Генератор SEO-оптимизированных статей")
        topic = st.text_input("Тема статьи (например: Почему кофе полезен)")
        keywords = st.text_input("Ключевые слова (через запятую)")
        
        if st.button("Создать SEO-статью"):
            if topic:
                with st.spinner('Пишем SEO-шедевр...'):
                    prompt = f"Напиши SEO-оптимизированную статью на тему: {topic}. Используй ключевые слова: {keywords}. Статья должна иметь заголовок H1, подзаголовки H2 и список преимуществ."
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    st.markdown("---")
                    st.markdown(response.choices[0].message.content)
            else:
                st.warning("Введите тему статьи!")

    # --- ВКЛАДКА РЕКЛАМА ---
    with tab2:
        st.subheader("Креативы для рекламы")
        product = st.text_input("Название продукта/услуги")
        if st.button("Сгенерировать объявление"):
            with st.spinner('Создаем креатив...'):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": f"Напиши 3 варианта рекламного объявления для: {product}"}]
                )
                st.write(response.choices[0].message.content)

    # --- ВКЛАДКА ОТЗЫВЫ ---
    with tab3:
        st.subheader("Работа с репутацией")
        review = st.text_area("Текст отзыва от клиента")
        if st.button("Написать ответ на отзыв"):
            with st.spinner('Подбираем слова...'):
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": f"Напиши вежливый ответ на этот отзыв: {review}"}]
                )
                st.success(response.choices[0].message.content)

else:
    # Экран для тех, кто еще не купил
    st.warning("🔒 Доступ ограничен. Требуется подписка.")
    st.write("### Станьте лидером рынка с помощью AI")
    st.write("Наш сервис генерирует тексты, которые приносят продажи.")
    st.link_button("🔥 ОФОРМИТЬ ПОДПИСКУ ($19)", "https://bizbooster.lemonsqueezy.com")
