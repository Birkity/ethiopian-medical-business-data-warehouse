

with source_data as (
    select 
        channel_name,
        channel_handle,
        message_id,
        message_text,
        timestamp,
        media_path,
        header_text
    from {{ source('Telegram_data', 'transformed_telegram_data') }}
)

select * from source_data;
