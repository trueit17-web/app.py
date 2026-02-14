import streamlit as st
import time

# Настройка страницы
st.set_page_config(page_title="BizBoost Pro", layout="centered")

# --- ИМИТАЦИЯ БАЗЫ ДАННЫХ КЛЮЧЕЙ (В реальности это ваш список оплативших) ---
VALID_KEYS = ["PREMIUM100", "BIZ_GROWTH_2024", "STARTUP_OWNER"]

st.title("🚀 BizBoost Pro: Генератор прибыли")
st.subheader("Автоматизация маркетинга для малого бизнеса")

# Боковая панель для управления доступом
st.sidebar.header("🔑 Доступ")
user_key = st.sidebar.text_input("Введите ваш лицензионный ключ:", type="password")

# Проверка оплаты
if user_key in VALID_KEYS:
    st.sidebar.success("Доступ разрешен! Тариф: Безлимитный")
    
    # ОСНОВНОЙ ФУНКЦИОНАЛ
    option = st.selectbox(
        'Выберите инструмент:',
        ['Идеальный ответ на отзыв (SEO)', 'Продающий пост в Instagram', 'Сценарий для Reels/TikTok']
    )
    
    context = st.text_area("Введите детали (о чем писать?):")
    
    if st.button("Сгенерировать магию ✨"):
        with st.spinner('ИИ создает контент, который приносит деньги...'):
            time.sleep(2) # Имитация работы
            st.success("Готово!")
            st.info(f"Здесь будет результат для: {context}")
            st.button("Скачать в PDF")

else:
    # ЭКРАН ПРОДАЖИ (То, что видит бесплатный пользователь)
    st.warning("🔒 Функционал заблокирован. Требуется активная подписка.")
    st.write("### Почему вам нужен BizBoost Pro?")
    st.write("- ✅ Экономия 20+ часов в неделю на копирайтинге.")
    st.write("- ✅ Увеличение конверсии продаж на 30%.")
    st.write("- ✅ Профессиональные ответы на отзывы за 5 секунд.")
    
    st.markdown("---")
    st.write("#### Стоимость: $19 / месяц")
    
    # Ссылка на оплату (сюда вы вставите ссылку из платежной системы)
    st.link_button("👉 Оформить подписку и получить ключ", "https://your-payment-link.com")

st.sidebar.markdown("---")
st.sidebar.info("Поддержка: support@bizboost.ai")