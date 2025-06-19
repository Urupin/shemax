# Проект: Коннектор Odoo 17 — Ysell.pro

## 1. Описание задачи

Реализовать односторонний коннектор между Odoo 17 и Ysell.pro для автоматизации передачи подтверждённых заказов, отслеживания их доставки и создания складских перемещений.

---

## 2. Техническое задание

**Основная логика:**
- Заказ передаётся в Ysell только после подтверждения (статус "sale").
- Передаются все необходимые для доставки поля: детали клиента-получателя, товары, количество, серийные номера, комментарии.
- Серийные номера передаются при создании заказа.
- В заказе указывается ID товара Odoo и ID товара Ysell (маппинг хранится в Odoo).
- Ежечасно (cron) проверяется статус доставки всех заказов, отправленных в Ysell.
- Обрабатывается только статус "Done" (доставлен).
- При получении статуса "Done" в Odoo создаётся складское перемещение ShemaxGlobal → Покупатель в состоянии Draft.
- Возвраты и частичные доставки не учитываются.
- Справочники продуктов и вариантов не синхронизируются, используются только существующие ID.
- Все обмены с Ysell логируются.
- Ошибки интеграции отображаются пользователю через уведомления.

**Технические детали:**
- Аутентификация через API-ключ Ysell, хранится в ir.config_parameter.
- Методы Ysell API:
    - POST `/api/orders/create` — создание заказа
    - GET `/api/orders/status?id=...` — проверка статуса заказа
    - Работа с серийными номерами — согласно [API Ysell](https://wiki.ysell.pro/doku.php?id=ru:serialnum)
- Структура модуля:
    - `models/sale_order.py` — расширение sale.order для интеграции с Ysell
    - `services/ysell_client.py` — клиент для работы с Ysell API
    - `data/ir_cron.xml` — задачи по расписанию
    - `models/stock_picking.py` — создание складских перемещений

---

## 3. Таблица маппинга полей

См. файл [`field_mapping.csv`](field_mapping.csv):

Odoo Field | Description | Ysell Field | Required | Notes
--- | --- | --- | --- | ---
sale_order.id | ID заказа Odoo | order_id | Да | Внутренний идентификатор Odoo (для связи)
sale_order.partner_id.name | Имя получателя | client_name | Да |
sale_order.partner_id.phone | Телефон получателя | client_phone | Да |
sale_order.partner_id.email | Email получателя | client_email | Нет |
sale_order.partner_id.street | Улица | client_address_street | Да |
sale_order.partner_id.city | Город | client_address_city | Да |
sale_order.partner_id.zip | Почтовый индекс | client_address_zip | Нет |
sale_order.partner_id.country_id.name | Страна | client_address_country | Нет |
sale_order.note | Комментарий к заказу | comment | Нет |
sale_order.order_line.product_id.id | ID товара Odoo | product_odoo_id | Да | Для внутренней связи
sale_order.order_line.product_id.ysell_id | ID товара Ysell | product_id | Да | Маппинг хранится в Odoo
sale_order.order_line.product_uom_qty | Количество | quantity | Да |
sale_order.order_line.serial_numbers | Серийные номера | serial_numbers | Нет | Список через запятую
sale_order.order_line.price_unit | Цена за единицу | price | Нет | Если требуется
sale_order.order_line.name | Название товара | product_name | Нет |
sale_order.date_order | Дата заказа | order_date | Нет |
sale_order.state | Статус заказа | status | Нет | Для внутреннего контроля
ysell_order_id | ID заказа Ysell | ysell_order_id | Да | Хранится в Odoo после создания заказа
ysell_delivery_status | Статус доставки Ysell | ysell_delivery_status | Да | Обновляется по API

---

## 4. Внешние источники

- [Ysell API: Работа с заказами](https://wiki.ysell.pro/doku.php?id=ru:api_start#order)
- [Ysell API: Серийные номера](https://wiki.ysell.pro/doku.php?id=ru:serialnum)

---

## 5. Вопросы и уточнения

- Заказ создаётся в Ysell только после подтверждения (статус "sale").
- Передаются все необходимые поля для доставки.
- Обрабатывается только статус доставки "Done".
- Перемещения создаются только для доставленных заказов.
- Возвраты и частичные доставки не учитываются.
- Серийные номера передаются при создании заказа.
- Маппинг продуктов ведётся по ID Odoo и Ysell.
- Ошибки отображаются через уведомления, все обмены логируются.
- Права доступа и тестовый аккаунт настраиваются отдельно.

---

**Данный prompt отражает текущее состояние проекта и может быть расширен по мере развития интеграции.**