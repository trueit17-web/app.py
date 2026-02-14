import streamlit as st
from openai import OpenAI

# Настройка страницы
st.set_page_config(page_title="BizBooster AI", page_icon="🚀")

# Инициализация клиента OpenAI (берем ключ из Secrets для безопасности)
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except:
    st.error("Ошибка: Ключ API не найден в Secrets!")

VALID_KEYS = ["PREMIUM100", "VIP_ACCESS", "BIZ2026"]

st.title("🚀 BizBooster AI")

# Проверка ключа в боковой панели
with st.sidebar:
    user_key = st.text_input("Введите ваш лицензионный ключ:", type="password")

if user_key in VALID_KEYS:
    st.success("Доступ разрешен!")
    
    tab1, tab2 = st.tabs(["✍️ Генератор рекламы", "💬 Ответы на отзывы"])

    with tab1:
        product = st.text_input("Что рекламируем? (например: Кофейня 'Бодрость')")
        target = st.text_input("Кто ваша аудитория? (например: Студенты и офисные работники)")
        
        if st.button("Сгенерировать рекламный текст"):
            if product and target:
                with st.spinner('ИИ пишет текст...'):
                    # ТУТ ПРОИСХОДИТ РЕАЛЬНЫЙ ЗАПРОС К ИИ
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "Ты эксперт по маркетингу и копирайтингу."},
                            {"role": "user", "content": f"Напиши яркий рекламный пост для {product}, ориентированный на {target}. Добавь эмодзи и призыв к действию."}
                        ]
                    )
                    st.write("### Ваш готовый текст:")
                    st.write(response.choices[0].message.content)
            else:
                st.warning("Заполните все поля!")

    with tab2:
        review_text = st.text_area("Вставьте отзыв клиента сюда:")
        if st.button("Создать идеальный ответ"):
            if review_text:
                with st.spinner('Анализируем отзыв...'):
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "Ты менеджер по работе с клиентами. Напиши вежливый и профессиональный ответ на отзыв."},
                            {"role": "user", "content": review_text}
                        ]
                    )
                    st.write("### Ответ для клиента:")
                    st.success(response.choices[0].message.content)

else:
    st.warning("🔒 Пожалуйста, введите ключ доступа или оформите подписку.")
    st.link_button("🔥 ОФОРМИТЬ ПОДПИСКУ ($19)", "https://bizbooster.lemonsqueezy.com")
