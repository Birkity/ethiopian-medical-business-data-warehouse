

with base as (
    select 
        channel_name,
        count(message_id) as total_messages,
        max(timestamp) as latest_message
    from {{ ref('transformed_telegram_data') }}
    group by channel_name
)

select * from base;
