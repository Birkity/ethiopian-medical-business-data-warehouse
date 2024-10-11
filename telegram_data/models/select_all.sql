-- models/select_all.sql

with source_data as (
    select * from {{ source('Telegram_data', 'transformed_telegram_data') }}
)

select 
    id,
    channel_name,
    message_text,
    timestamp
from source_data
