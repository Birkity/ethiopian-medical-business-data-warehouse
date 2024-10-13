
  create view "Telegram_data"."public"."select_all__dbt_tmp"
    
    
  as (
    WITH source_data AS (
    SELECT 
        channel_name,
        channel_handle,
        message_id,
        message_text,
        timestamp,
        media_path,
        header_text
    FROM "Telegram_data"."public"."transformed_telegram_data"
)

SELECT 
    channel_name,
    channel_handle,
    message_id,
    message_text,
    timestamp,
    media_path,
    header_text
FROM source_data
  );